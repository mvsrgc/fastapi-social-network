#!/bin/bash
docker run --detach --name my-postgres-server --env POSTGRES_PASSWORD=mysecretpassword --publish 5432:5432 postgres:latest