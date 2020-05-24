#!/bin/bash

docker pull racedetection/rds:romp-tool
cd /flask && python3 server.py
