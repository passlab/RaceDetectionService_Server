import json
import re
import sys

file = open(sys.argv[1],"r")
Lines = file.readlines()
jsAry = []
content = [line.strip() for line in Lines]
for i in range(0,len(content)):
	x = re.search("^Write",content[i])
	if (x):
		y = content[i].split()
		index = y.index('at')
		js = {}
		js["Memory Address"] = y[index+1]
		index1 = y.index('by')
		Thread = re.split(":",y[index1+2])
		js1 = {}
		js1["thread"] = y[index1+1] + ' ' + Thread[0]
		y1 = content[i+1].split()
		for item in y1:
			if(re.search("^/",item)):
				file = item.rsplit("/",1)
				#js1["file loaction"] = file[0]
				location = file[1].split(":")
				list = []
				list.append(location[0])
				list.append(location[1])
				if len(location) >= 3:
					list.append(location[2])
				else:
					list.append("-1")
				js1["location"] = list
		js["Write"] = js1
		jsAry.append(js)
	x = re.search("^Previous read",content[i])
	if (x):
		y = content[i].split()
		index = y.index('at')
		for item in jsAry:
			if (item["Memory Address"] == y[index+1]):
				index1= y.index('by')
				Thread = re.split(":",y[index1+2])
				js1 = {}
				js1["thread"] = y[index1+1] + ' ' + Thread[0]
				y1 = content[i+1].split()
				for item1 in y1:
					if(re.search("^/",item1)):
						file = item1.rsplit("/",1)
						location = file[1].split(":")
						list = []
						list.append(location[0])
						list.append(location[1])
						if len(location) >= 3:
							list.append(location[2])
						else:
							list.append("-1")
						js1["location"] = list
						item["Read"] = js1
						item["tool"] = "ThreadSanitier"
		
	x = re.search("^Read",content[i])
	if (x):
		y = content[i].split()
		index = y.index('at')
		js = {}
		js["Memory Address"] = y[index+1]
		index1 = y.index('by')
		Thread = re.split(":",y[index1+2])
		js1 = {}
		js1["thread"] = y[index1+1] + ' ' + Thread[0]
		y1 = content[i+1].split()
		for item in y1:
			if(re.search("^/",item)):
				file = item.rsplit("/",1)
				#js["file loaction"] = file[0]
				location = file[1].split(":")
				list = []
				list.append(location[0])
				list.append(location[1])
				if len(location) >= 3:
					list.append(location[2])
				else:
					list.append("-1")
				js1["location"] = list
		js["Read"] = js1
		jsAry.append(js)
	x = re.search("^Previous write",content[i])
	if (x):
		y = content[i].split()
		index = y.index('at')
		for item in jsAry:
			if item.get("Write","") is not None:
				if (item["Memory Address"] == y[index+1]):
					index1 = y.index('by')
					Thread = re.split(":",y[index+2])
					js1 = {}
					js1["thread"] = y[index+1] + ' ' + Thread[0]
					y1 = content[i+1].split()
					for item1 in y1:
						if(re.search("^/",item1)):
							file = item1.rsplit("/",1)
							location = file[1].split(":")
							list = []
							list.append(location[0])
							list.append(location[1])
							if len(location) >= 3:
								list.append(location[2])
							else:
								list.append("-1")
							js1["location"] = list
							item["Write"] = js1
							item["tool"] = "ThreadSanitier"
			elif (item["Memory Address"] == y[index+1]):
				index1 = y.index('by')
				Thread = re.split(":",y[index1+2])
				js1 = {}
				js1["thread"] = y[index1+1] + ' ' + Thread[0]
				y1 = content[i+1].split()
				for item1 in y1:
					if(re.search("^/",item1)):
						file = item1.rsplit("/",1)
						location = file[1].split(":")
						list = []
						list.append(location[0])
						list.append(location[1])
						if len(location) >= 3:
							list.append(location[2])
						else:
							list.append("-1")
						js1["location"] = list
						item["Write"] = js1
						item["tool"] = "ThreadSanitier"

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
