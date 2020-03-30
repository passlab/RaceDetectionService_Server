import json
import re
import sys
import random

def majorityVote(obj):
	VoteNum = 0
	jsAry = []
	finalAry = []
	for i in range(len(obj)):
		if obj[i] != None :
			js = {}
			VoteNum += 1
			for key in obj[i].keys():
				if obj[i][key] == {}:
					js[i] = "no race"
				for key1 in obj[i][key].keys():
					if obj[i][key][key1] != {}:
						js[i] = obj[i][key][key1]
						break;
					else:
						js[i] = 'no race'
			jsAry.append(js)
	vote = 0
	for item in jsAry:
		for key in item.keys():
			 vote += 1
	if vote/VoteNum >= 0.5:
		print("RDS detected a data race by majority vote!")
		for item in jsAry:
			for key in item.keys():
				if item[key] != 'no race':
					js = {}
					js['race'] = "true"
					js['method'] = "Majority Vote"
					js['race information'] = item[key]
					finalAry.append(js)
	else:
		print("No data race find")
	js = {}
	for i in range(len(finalAry)):
		js[i] = finalAry[i]

	return(js)

def weightVote(obj):

	finalAry = []

	Tsanweight = 0.881

	Archerweight= 0.755

	Inspectorweight = 0.723

	Rompweight = 0.911

	Archer = 0

	Inspector = 0

	Tsan = 0

	Romp = 0

	ArcherVote = 0

	InsepctorVote = 0

	TsanVote = 0

	RompVote = 0

	jsAry = []
	for i in range(len(obj)):
		if obj[i] != None :
			js = {}
			for key in obj[i].keys():
				if obj[i][key] == {}:
					js[i] = "no race"
				for key1 in obj[i][key].keys():
					if obj[i][key][key1] != {}:
						js[i] = obj[i][key][key1]
						break;
					else:
						js[i] = 'no race'
			jsAry.append(js)
	WeightFlag = 0
	x = []
	for item in jsAry:
		for key in item.keys():
			x.append(key)
			if key == 0:
				if item[key] != 'no race':
					ArcherVote = 1
				else:
					ArcherVote = 0
			if key == 1:
				if item[key] != 'no race':
					InsepctorVote = 1
				else:
					InsepctorVote = 0
			if key == 2:
				if item[key] != 'no race':
					TsanVote = 1
				else:
					TsanVote = 0
			if key == 3:
				if item[key] != 'no race':
					RompVote = 1
				else:
					RompVote = 0

	for item in x:
		if item == 0:
			Archer = 1
		if item == 1:
			Inspector = 1
		if item == 2:
			Tsan = 1
		if item == 3:
			Romp = 1

	Tsanweight = Tsanweight * Tsan

	Archerweight = Archerweight * Archer

	Inspectorweight = Inspectorweight * Inspector

	Rompweight = Rompweight * Romp

	Sumweight = Tsanweight + Archerweight + Inspectorweight + Rompweight

	WeightFlag = (Tsanweight/Sumweight) * TsanVote + (Archerweight/Sumweight) * ArcherVote + (Inspectorweight/Sumweight) * InsepctorVote + (Rompweight/Sumweight) * RompVote

	if WeightFlag >= 0.5:
		print("RDS detected a data race by weight vote!")
		for item in jsAry:
			for key in item.keys():
				if item[key] != 'no race':
					js = {}
					js['race'] = "true"
					js['method'] = "Weight Vote"
					js['race information'] = item[key]
					finalAry.append(js)
	else:
		print("No data race find")
	js = {}
	for i in range(len(finalAry)):
		js[i] = finalAry[i]

	return(js)

def randomVote(obj):
	finalAry = []
	VoteNum = 0
	jsAry = []
	for i in range(len(obj)):
		if obj[i] != None :
			js = {}
			VoteNum += 1
			for key in obj[i].keys():
				if obj[i][key] == {}:
					js[i] = "no race"
				for key1 in obj[i][key].keys():
					if obj[i][key][key1] != {}:
						js[i] = obj[i][key][key1]
						break;
					else:
						js[i] = 'no race'
			jsAry.append(js)
	
	RandomFlag = random.randint(0, VoteNum-1)
	
	for key in jsAry[RandomFlag].keys():
		if jsAry[RandomFlag][key] != 'no race':
			print("RDS detected a data race by random vote!")
			js = {}
			js['race'] = "true"
			js['method'] = "Random Vote"
			js['race information'] = jsAry[RandomFlag][key]
			finalAry.append(js)
		else:
			print("No data race find")
		js = {}
	for i in range(len(finalAry)):
		js[i] = finalAry[i]

	return(js)

