import json
import re
import sys

file = open(sys.argv[1],"r")
Lines = file.readlines()
jsAry = []
content = [line.strip() for line in Lines]
for item in content:
	jsAry.append(item)

file = open(sys.argv[2],"r")
Lines = file.readlines()
content = [line.strip() for line in Lines]
for item in content:
	jsAry.append(item)

file = open(sys.argv[3],"r")
Lines = file.readlines()
content = [line.strip() for line in Lines]
for item in content:
	jsAry.append(item)

for item in jsAry:
	print(item)
