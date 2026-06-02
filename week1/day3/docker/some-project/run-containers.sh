#!/bin/bash
docker run -d --rm -p 5432:5432 --name proj-posgr --network proj-lan -v test-posgr:/var/lib/postgresql/data --env-file .docker.env postgres:15-alpine > /dev/null
sleep 5
docker run -d --rm -p 8001:80 --name proj-django --network proj-lan some-project:v1 > /dev/null
echo 'To delete containers run: sudo docker stop proj-django proj-posgr'
