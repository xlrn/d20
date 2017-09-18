#!/usr/bin/env python

import argparse
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('-th', 
	default=False, 
	dest='threshold',
	help='entering any value will give you a threshold')
parser.add_argument('-t',  
	dest='task',
	help='the task that must be completed')
parser.add_argument('-s',
	dest='stat',
	help='stat being used')

args = parser.parse_args()


roll = randint(1, 20)
print 'roll: {}'.format(roll)

if args.threshold:
	num = randint(1, 20)
	print 'threshold: {}'.format(num)

if args.task is not None:
	print 'task: {}'.format(args.task)

if args.stat is not None:
	print 'stat: {}'.format(args.stat)