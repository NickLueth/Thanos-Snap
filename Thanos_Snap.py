#!/bin/python3
# Thanos snapping script
# Created by Nick Lueth
# Last edited: 1/30/2020

import random

def load_names():
	# Load names of people from 2 files
	dead = []
	alive = []
	dead_file = open("dead.txt", "a+")
	alive_file = open("alive.txt", "a+")
	with open("dead.txt") as dead_file:
		for name in dead_file:
			dead.append(name[:-1])
	with open("alive.txt") as alive_file:
		for name in alive_file:
			alive.append(name[:-1])
	dead_file.close()
	alive_file.close()
	return dead, alive

def get_new():
	# Get's a list of new names by the user
	print("SEPARATE NAMES BY COMMAS!")
	names = input("Enter the name(s): ").lower().split(",")
	for i in range(len(names)):
		names[i] = names[i].strip()
	names = list(dict.fromkeys(names))
	return names

def finalize_list(dead, alive, names):
	new_names = []
	for name in names:
		if name not in alive and name not in dead:
			new_names.append(name)
		elif name in alive:
			print(name, "survived the snap!")
		else:
			print(name, "died after the snap!")
	return new_names


def thanos_snap(new_names):
	# Coin flip whether someone dies from the snap or lives
	for name in new_names:
		coin = random.randint(0, 1)
		if name == "":
			continue
		elif coin == 0:
			dead_file = open("dead.txt", "a+")
			print(name, "died after the snap!")
			dead_file.write(name + "\n")
			dead_file.close()
		elif coin == 1:
			alive_file = open("alive.txt", "a+")
			print(name, "survived the snap!")
			alive_file.write(name + "\n")
			alive_file.close()

def results():
	# Make to print the results in a appealing way
	pass

dead, alive = load_names()
names = get_new()
thanos_snap(finalize_list(dead, alive, names))
