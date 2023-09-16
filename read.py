#!/usr/bin/python3
import sys
import time
import os
import array as arr

rowA=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 
rowB=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 

def print_display(row1, row2):
    os.system("clear")
    for i in range(0,16):
        print(row1[i],end='')
    print("")
    for i in range(0,16):
        print(row2[i],end='')
    print("")

##########################################

x=0
while True:
    
    c=sys.stdin.read(1)
    time.sleep(0.2)

    if c.isalpha(): 
        rowB[x]=c
    elif c.isdigit():
        rowB[x]=c
    else:
        rowB[x]="~"

    x=x+1

    if x>15: 
        x=0
        for i in range(0,16):
            rowA[i]=rowB[i]
            rowB[i]="_"

    print_display(rowA, rowB) 

