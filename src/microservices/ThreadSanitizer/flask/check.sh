#!/bin/bash

! docker container inspect tsan-sandbox > /dev/null 2>&1 || docker stop tsan-sandbox
! docker container inspect tsan-sandbox > /dev/null 2>&1 || docker rm tsan-sandbox
docker run -it -d --network none --name tsan-sandbox racedetectionservice/rds:tsan-tool bash
docker cp /tmp/task/$1 tsan-sandbox:/home/rds/dataracebench/micro-benchmarks/.
rm -rf /tmp/task/*
docker exec -u root tsan-sandbox chown rds:rds /home/rds/dataracebench/micro-benchmarks/$1
docker exec tsan-sandbox /home/rds/run.sh
docker cp tsan-sandbox:/home/rds/dataracebench/results /tmp/task/results
docker stop tsan-sandbox
docker rm tsan-sandbox
