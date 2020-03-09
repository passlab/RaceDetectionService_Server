import json
import re
import sys


with open("archerOutput.json") as test:
	data = test.read();

d = json.loads(data)

with open("inspectorOutput.json") as test:
	data = test.read();

d1 = json.loads(data)

with open("TsanOutput.json") as test:
	data = test.read();

d2 = json.loads(data)

with open("rompOutput.json") as test:
    data = test.read();

d3 = json.loads(data)

Voteflag = 0

for i in range(len(d)):
    if i is None:
        ArcherVote = 0
    else:
        ArcherVote = 1
        Voteflag += 1
        
for i in range(len(d1)):
    if i is None:
        InsepctorVote = 0
    else:
        InsepctorVote = 1
        Voteflag += 1

for i in range(len(d2)):
    if i is None:
        TsanVote = 0
    else:
        TsanVote = 1
        Voteflag += 1

for i in range(len(d3)):
    if i is None:
        RompVote = 0
    else:
        RompVote = 1
        Voteflag += 1

if Voteflag >= 2:
    print("RDS detected a data race!")

###information need to dispaly
