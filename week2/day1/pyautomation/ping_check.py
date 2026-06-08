import subprocess
hosts = ["ya.ru", "google.com", "8.8.8.8", "requp.com"]
for host in hosts:
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True)
    print(f"{host} - {'OK' if result.returncode == 0 else 'FAIL'}")
