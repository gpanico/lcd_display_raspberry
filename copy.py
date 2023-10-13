#!/usr/bin/python3

import sys
from time import sleep
from os import system

fp=open("bulletin.txt","a")

##########################################

while True:
    c=sys.stdin.read(1)
    print(c,file=fp,end='',flush=True)
    print(c,end='',flush=True)
    # sys.stdout.flush()

