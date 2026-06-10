import subprocess
from time import sleep
from datetime import date
import logging

WORKDIR = 'week2/day2/db'
def set_logger() -> logging.Logger:     
    LOG_DIR = 'logs'
    LOG_PATH = f'{WORKDIR}/{LOG_DIR}'
    res = subprocess.run(
        ('find', f'{WORKDIR}', '-type', 'd', '-name', f'{LOG_DIR}'), 
        text=True, capture_output=True
        )   
    if res.stderr:
        raise Exception(res.stderr)
    if not res.stdout:
        res = subprocess.run(
        ('mkdir', f'{LOG_PATH}'), text=True, capture_output=True
        )   
        if res.stderr:
            raise Exception(res.stderr)
    logger = logging.getLogger()
    file_handler = logging.FileHandler(filename=f'{LOG_PATH}/backup.log', mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger

logger: logging.Logger = set_logger() 


def _is_container_running(container_name: str) -> bool:
    res = subprocess.run(
        ['bash', '-c', f'docker ps | grep -w {container_name} | wc -l'],
        capture_output=True, text=True
        )
    if res.stderr:
        raise Exception(subprocess.stderr)
    return bool(int(res.stdout.strip('\n')[0]))


def _run_container_with_db(
        container_name: str, port: str | int, env: str, db_name: str, volume_path
        ) -> None:
    logging.info('Starting running the container')
    if not _is_container_running(container_name):
        commands = [
            ['docker', 'run', '-d', '-p', f'{port}:5432', 
                '--rm', '--env-file', f'{env}', '-v', f'{volume_path}:/backup', 
                '--name', f'{container_name}', 'postgres:15-bookworm'
                ],
            ['sleep', '1'],
            ['docker', 'exec', '-it', f'{container_name}', 
             'psql', '-c', f'CREATE DATABASE {db_name};'],
        ]
        for command in commands:
            res = subprocess.run(
                command, capture_output=True, text=True
            )
            sleep(1)
            if res.stderr:
                raise Exception(res.stderr)
        logging.info('The container is running')
        logging.info('The db is created')


def _stop_container(container_name: str) -> None:
    logging.info('Stoping the container')
    if _is_container_running(container_name):
        res = subprocess.run(
            ['docker', 'stop', f'{container_name}'],
            capture_output=True, text=True
        )
        if res.stderr:
            raise Exception(res.stderr)
        if _is_container_running(container_name):
            raise Exception('Container didn\'t stop')
    logging.info('The container is stoped')


def backup_db(
        container_name: str, username: str, host: str, 
        port: str, db_name: str, dump_name: str, backup_dir: str
        ):
    try:
        logging.info('Starting the program')
        _run_container_with_db(
            port=port,
            db_name=db_name,
            container_name=container_name,
            env='week2/day2/db/.env',
            volume_path=backup_dir
        )

        res = subprocess.run([
            'docker', 'exec', '-it', f'{container_name}',
            'pg_dump', '-U', username, '-F', 'c', '-h', host, 
            '-d', db_name, '-f', f'/backup/{dump_name}'
        ], text=True, capture_output=True)
        if res.stderr:
            raise Exception(res.stderr)
        
        _stop_container(container_name=container_name)
        logging.info('The program successfully finished')
    except Exception as e:
        logging.error(e)


db_name='test'

backup_db(
    container_name='some_uniq_postg',
    port='5402',
    host='localhost',
    username='root',
    db_name=db_name,
    dump_name=f'{db_name}-{date.today()}.dump',
    backup_dir=f'./{WORKDIR}'
    )