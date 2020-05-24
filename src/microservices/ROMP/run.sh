#!/bin/bash
source /home/rds/.bashrc
cd /home/rds/dataracebench
scripts/test-harness.sh -d 32 -x romp
