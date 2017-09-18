#!/usr/bin/env python

import argparse
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('-th', '--threshold', default=False, dest='threshold')
parser.add_argument('-t', '--task', default=None, dest='task')
parser.add_argument('-s', '--stat', default=None, dest='stat')
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