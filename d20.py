#!/usr/bin/env python

import argparse
from random import randint

#initialize parser
parser = argparse.ArgumentParser()

#arguments
parser.add_argument('-th', 
	default=False, 
	dest='threshold',
	help='entering any value will give you a threshold')
parser.add_argument('-t',  
	dest='task',
	help='the task that must be completed')
parser.add_argument('-st',
	dest='stat',
	help='stat being used')
parser.add_argument('-d',
	dest='dice',
	help='number of dice')
parser.add_argument('-s',
	dest='sides',
	help='number of sides for dice')

args = parser.parse_args()

#functions
def rollType(sides):
	return randint(1, sides)

def roll(n = 1, sides = 20):
	return tuple(rollType(sides) for _ in range(n))	

#shit
if args.dice and args.sides:
	dice = roll(n = int(args.dice), sides = int(args.sides))
	print 'roll: {}, sum: {}'.format(dice, sum(dice))
elif args.sides: 
	dice = roll(sides = int(args.sides))
	print 'roll: {}, sum: {}'.format(dice, sum(dice))
elif args.dice:
	dice = roll(n = int(args.dice))
	print 'roll: {}, sum: {}'.format(dice, sum(dice))
else:
	dice = randint(1, 20)
	print 'roll: {}'.format(dice)

if args.threshold and args.dice:
	num = roll(n = int(args.dice))
	print 'threshold: {}'.format(sum(num))
elif args.threshold:
	num = randint(1, 20)
	print 'threshold: {}'.format(num)

if args.task is not None:
	print 'task: {}'.format(args.task)

if args.stat is not None:
	print 'stat: {}'.format(args.stat)