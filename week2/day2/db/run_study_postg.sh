#!/bin/bash
docker run -p 5400:5432 --env-file .env -d --rm -v study-postg:/var/lib/postgresql/data --name study-postg postgres:15-bookworm
