#!/bin/bash

! docker container inspect archer-sandbox > /dev/null 2>&1 || docker stop archer-sandbox
! docker container inspect archer-sandbox > /dev/null 2>&1 || docker rm archer-sandbox
docker run -it -d --network none --name archer-sandbox racedetection/rds:archer-tool bash
docker cp /tmp/task/$1 archer-sandbox:/home/rds/dataracebench/micro-benchmarks/.
rm -rf /tmp/task/*
docker exec -u root archer-sandbox chown rds:rds /home/rds/dataracebench/micro-benchmarks/$1
docker exec archer-sandbox /home/rds/run.sh
docker cp archer-sandbox:/home/rds/dataracebench/results /tmp/task/results
docker stop archer-sandbox
docker rm archer-sandbox
