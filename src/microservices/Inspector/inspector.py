import json
import re
import sys

file = open(sys.argv[1],"r")
Lines = file.readlines()
jsAry = []
content = [line.strip() for line in Lines]
for i in range(0,len(content)):
	x = re.search("Write",content[i])
	if (x):
		y = content[i].split()
		js = {}
		if(re.search("^/",y[0])):
			file = y[0].rsplit("/",1)
			location = file[1].split(":")
			f = location[0].split("(")
			list = []
			list.append(f[0])
			line = f[1].split(")")
			list.append(line[0])
			js1 = {}
			js1["location"] = list
			js["Write"] = js1
		x = re.search("Read",content[i+1])
		if (x):
			y = content[i+1].split()
			if(re.search("^/",y[0])):
				file = y[0].rsplit("/",1)
				location = file[1].split(":")
				f = location[0].split("(")
				list = []
				list.append(f[0])
				line = f[1].split(")")
				list.append(line[0])
				js1 = {}
				js1["location"] = list
				js["Read"] = js1
			js["tool"] = "Intel-instpector"
			jsAry.append(js)
	x = re.search("Read",content[i])
	if (x):
		y = content[i].split()
		js = {}
		if(re.search("^/",y[0])):
			file = y[0].rsplit("/",1)
			location = file[1].split(":")
			f = location[0].split("(")
			list = []
			list.append(f[0])
			line = f[1].split(")")
			list.append(line[0])
			js1 = {}
			js1["location"] = list
			js["Read"] = js1
		x = re.search("Write",content[i+1])
		if (x):
			y = content[i+1].split()
			if(re.search("^/",y[0])):
				file = y[0].rsplit("/",1)
				location = file[1].split(":")
				f = location[0].split("(")
				list = []
				list.append(f[0])
				line = f[1].split(")")
				list.append(line[0])
				js1 = {}
				js1["location"] = list
				js["Write"] = js1
			js["tool"] = "intel-instpector"
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