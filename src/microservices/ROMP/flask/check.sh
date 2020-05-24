#!/bin/bash

! docker container inspect romp-sandbox > /dev/null 2>&1 || docker stop romp-sandbox
! docker container inspect romp-sandbox > /dev/null 2>&1 || docker rm romp-sandbox
docker run -it -d --network none --name romp-sandbox racedetection/rds:romp-tool bash
docker cp /tmp/task/$1 romp-sandbox:/home/rds/dataracebench/micro-benchmarks/.
rm -rf /tmp/task/*
docker exec -u root romp-sandbox chown rds:rds /home/rds/dataracebench/micro-benchmarks/$1
docker exec romp-sandbox /home/rds/run.sh
docker cp romp-sandbox:/home/rds/dataracebench/results /tmp/task/results
docker stop romp-sandbox
docker rm romp-sandbox
