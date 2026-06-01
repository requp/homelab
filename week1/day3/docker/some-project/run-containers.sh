#!/bin/bash
docker run -d --rm -p 5432:5432 --name proj-posgr --network host -v test-posgr:/var/lib/postgresql/data -e POSTGRES_USER=root -e POSTGRES_PASSWORD=password -e POSTGRES_DB=myt postgres:15-alpine > /dev/null
sleep 10
docker run -d --rm -p 8001:80 --name proj-django --network host some-project:v1 > /dev/null
echo 'To delete containers run: sudo docker stop proj-django proj-posgr'
