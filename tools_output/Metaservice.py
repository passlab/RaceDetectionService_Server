import json
import re
import sys


with open("archerOutput.json") as test:
	data = test.read();

d = json.loads(data)

with open("inspectorOutput.json") as test:
	data = test.read();

d2 = json.loads(data)

with open("TsanOutput.json") as test:
	data = test.read();

d3 = json.loads(data)
print(d)
print(d2)
print(d3)
print(d['1']["tool"])
print(d2['1']["tool"])
print(d3['1']["tool"])

#need a function to analysis the input
