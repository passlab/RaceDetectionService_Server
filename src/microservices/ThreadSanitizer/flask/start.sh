#!/bin/bash

docker pull racedetectionservice/rds:tsan-tool
cd /flask && python3 server.py
