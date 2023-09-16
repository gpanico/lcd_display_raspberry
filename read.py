#!/usr/bin/python3
import sys
import time
import os
import array as arr

disp_col=20
disp_row=4

rowA=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 
rowB=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 
rowC=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 
rowD=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 

def print_display(row1, row2, row3, row4):
    os.system("clear")
    for i in range(disp_col):
        print(row1[i],end='')
    print("")
    for i in range(disp_col):
        print(row2[i],end='')
    print("")
    for i in range(disp_col):
        print(row3[i],end='')
    print("")
    for i in range(disp_col):
        print(row4[i],end='')
    print("")

##########################################

x=0
while True:
    
    c=sys.stdin.read(1)
    time.sleep(0.2)

    if c.isalpha(): 
        rowD[x]=c
    elif c.isdigit():
        rowD[x]=c
    else:
        rowD[x]="~"

    x=x+1

    if x>(disp_col-1): 
        x=0
        for i in range(disp_col):
            rowA[i]=rowB[i]
            rowB[i]=rowC[i]
            rowC[i]=rowD[i] 
            rowD[i]="_"

    print_display(rowA, rowB, rowC, rowD) 

