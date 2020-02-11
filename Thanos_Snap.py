#!/bin/python3
# Thanos snapping script
# Created by Nick Lueth
# Last edited: 2/11/2020

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
	old_dead = []
	old_alive = []
	for name in names:
		if name not in alive and name not in dead:
			new_names.append(name)
		elif name in alive:
			old_alive.append(name)
		else:
			old_dead.append(name)
	return new_names, old_alive, old_dead


def thanos_snap(new_names, old_alive, old_dead):
	# Coin flip whether someone dies from the snap or lives
	we_lived = old_alive
	we_died = old_dead
	for name in new_names:
		coin = random.randint(0, 1)
		if name == "":
			continue
		elif coin == 0:
			dead_file = open("dead.txt", "a+")
			we_died.append(name)
			dead_file.write(name + "\n")
			dead_file.close()
		elif coin == 1:
			alive_file = open("alive.txt", "a+")
			we_lived.append(name)
			alive_file.write(name + "\n")
			alive_file.close()
	return we_lived, we_died

def print_results(alive, dead):
	# Make to print the results in a appealing way
    	print("Alive:")
    	for name in alive:
        	print("{{*}} {name}".format(name=name))
    	print("\nDead:")
    	for name in dead:
        	print("{{*}} {name}".format(name=name))

dead, alive = load_names()
names = get_new()
nn, oa, od = finalize_list(dead, alive, names)
new_alive, new_dead = thanos_snap(nn, oa, od)
print_results(new_alive, new_dead)


