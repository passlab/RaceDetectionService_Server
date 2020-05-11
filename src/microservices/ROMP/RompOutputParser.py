import json
import re
import sys

file = open(sys.argv[1],"r")
Lines = file.readlines()
jsAry = []
content = [line.strip() for line in Lines]
for i in range(0,len(content)):
	x = re.search("RAW",content[i])
	if (x):
		y = content[i].split()
		index = y.index('addr:')
		js = {}
		js["Memory Address"] = y[index+1]
		y = content[i+1].split()
		for i in range(len(y)):
			file = y[0].rsplit("/",1)
			#js["file loaction"] = file[0]
			location = file[1].split(":")
			filename=location[0].split('@')
			list = []
			list.append(filename[0])
			list.append(location[1])
			col = y[1].split(":")
			list.append(col[1])
			js1 = {}
			js1["location"] = list
			js["Write"] = js1
			file = y[3].rsplit("/",1)
			#js["file loaction"] = file[0]
			location = file[1].split(":")
			list = []
			list.append(filename[0])
			list.append(location[1])
			col = y[4].split(":")
			list.append(col[1])
			js1 = {}
			js1["location"] = list
			js["Read"] = js1
			js["tool"] = "Romp"
		jsAry.append(js)
js = {}
jsAry1 = []
writelocation = []
readlocation = []

for item in jsAry:
	Cwritelocation = item['Write']['location']
	Creadlocation = item['Read']['location']
	if writelocation != Cwritelocation or readlocation != Creadlocation:
		jsAry1.append(item)
		writelocation = Cwritelocation
		readlocation = Creadlocation


for i in range(len(jsAry1)):
	js[i] = jsAry1[i]

r = json.dumps(js)
print(r)

