# Practical skills with docker and Dockerfile
## 1. docker 

#### Show all docker images and containers
`docker images` and `docker ps -a`

#### Delete a docker image or container
`docker rm <container-id-or-name>` or `docker rmi <image-id>`

#### Pull docker image from Docker Hub
`docker pull <image-name>:<image-tag>`

#### Create a named docker volume or a docker network

`docker volume create <volume-name>` or `docker network create <network-name>`

### Run a docker container
- -v - add an anonymous (/volume-path) or named (volume-name:/volume-path) volumes or bind mount from a host dir (./relative/or/absolute/path:/volume-path) 
- -d - detach 
- -e SOME_ENV=data or --env-file host/path/to/env/file
- --name container-name - Give the container a name
- --network my-network - Add container none/host/bridge (bridge by default)  or its own network to isolate and share the same network with other containers
- -p \<host-port>:\<container-port> - Connect host and container via tcp/udp (pointless with none and host networks)

`docker run -d -v named_volume:/container/path -env-file .env --name some-container --network special-network -p 8080:80 image-name:image-tag`

### Stop a docker container
`docker container stop <container-id-or-name>`

## 2. Dockerfile
#### Build an image from Dockerfile
-f /path/to/Dockerfile if it is not in the current dir <br/>
"." specify the context where the Dockerfile will be searching for files (to copy in the image for example) <br/>
So in this case it will be the current dir <br/> 
`docker build -t <image-name>:<image-tag> .`

#### Dockerfile instructions
```Dockerfile
FROM <parent-docker-image>:<tag> # A new Docker image has to be based from some other image

COPY dir/from/host dir/in/container

RUN some shell command # A command which needs to be run when the image is building

WORKDIR /other/path # Change a working directory for a container (like cd for us)

VOLUME /volume-path # Create an anonymous volume in docker volume to save results after stopping the container (can be overwrited with -v or any other volume connected option in docker run)

ENTRYPOINT ["some", "shell", "command"] # A command which needs to be run every time when container starts (can't be overwrited with docker run command)

CMD ["some", "shell", "command"] # Same as ENTRYPOINT but it can be overwrited with docker run
```
