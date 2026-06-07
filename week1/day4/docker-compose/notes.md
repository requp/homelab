# Practical skills for day 4
## docker compose
```yaml
services: # Declare a top level element to give instructions to new containers
    container1: # Give container a name (can be pinged by container1 name  in the same network). in docker ps it would be "<container-compose-dir>-<container1>-<num>"
        image: <image-name>:<image-tag>
        volumes: 
            - some_volume:/path/in/docker/container # Save all data from the container dir in a docker volume even when the container stops
        env-file:
            - path/to/host/env # Add env data to container
        restart: always # Restart the container until its removal
        networks:
            - inner-network # Add a new inner-network to isolate containers from others  
        ports:
            - <host-port>:<container-port> # Open a specific ports between the host and the container
        depends_on:
            - container2 # Show docker that this container should be started after container2
            
    container2:
        container_name: <container-name> # Give container name outside inner network (docker ps)
        pull_policy: never # Never let docker to pull the container from outside image repositories
        build: # make a container from specific Dockerfle
            context: /path/to/context/for/Dockerfile
            dockerfile: <Dockerfile-name>
            target: <target-name> # When the Dockerfile has multi-stages
        volumes:
            - ./path/from/host:/path/in/docker/container # The same saving data but it writes in the host dir (mount bind)
        networks:
            - inner-network
            - outside-network # add existed network

networks:
    - inner-network: # Declare inner network (at least with default params)
        name: <network-name> # Add the network a specific name
    - outside-network:
        external: true # Specify that this network exists outside the compose (can ping containers from other compose files)

volumes:
    - volume: # Declare docker volume with default params
```


