import json
import re
import sys
import random


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

###Majority vote

if Voteflag >= 2:
	print("RDS detected a data race by majority!")
else:
	print("No data race find")

###Weight vote

Tsanweight = 0.25

Archerweight= 0.25

Inspectorweight = 0.25

Rompweight = 0.25

WeightFlag = Tsanweight * TsanVote + Archerweight * ArcherVote + Inspectorweight * InsepctorVote + Rompweight * RompVote

if WeightFlag >= 0.5:
	print("RDS detected a data race by weight vote!")
else:
	print("No data race find")

###Random vote

RandomFlag = random.randint(1, 4)

if RandomFlag == 1:
	if ArcherVote == 1:
		print("RDS detected a data race by random vote!")
	else:
		print("No data race find")

if RandomFlag == 2:
	if TsanVote == 1:
		print("RDS detected a data race by random vote!")
	else:
		print("No data race find")

if RandomFlag == 3:
	if InsepctorVote == 1:
		print("RDS detected a data race by random vote!")
	else:
		print("No data race find")

if RandomFlag == 4:
	if RompVote == 1:
		print("RDS detected a data race by random vote!")
	else:
		print("No data race find")
###information need to dispaly
