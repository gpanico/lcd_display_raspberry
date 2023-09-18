#!/usr/bin/python3
import sys
import time
import os
import array as arr
import I2C_LCD_driver

disp_col=20
disp_row=4
#mylcd=I2C_LCD_driver.lcd()

rowA=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 
rowB=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 
rowC=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 
rowD=arr.array('u', ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]) 

def print_display(row1, row2, row3, row4):
    os.system("clear")
    for i in range(disp_col):
        print(row1[i],'',end='')
        #mylcd.lcd_display_string(row1[i], 4, i) 
    print("")
    for i in range(disp_col):
        print(row2[i],'',end='')
        #mylcd.lcd_display_string(row2[i], 4, i) 
    print("")
    for i in range(disp_col):
        print(row3[i],'',end='')
        #mylcd.lcd_display_string(row3[i], 4, i) 
    print("")
    for i in range(disp_col):
        print(row4[i],'',end='')
        #mylcd.lcd_display_string(row4[i], 4, i) 
    print("")

##########################################

print_display(rowA, rowB, rowC, rowD) 
x=0
while True:
    
    c=sys.stdin.read(1)
    time.sleep(0.15)

    if c.isalpha(): 
        rowD[x]=c
    elif c.isdigit():
        rowD[x]=c
    else:
        rowD[x]="~"

    # print new char on the last line of display
    # lcd_display_string(self, rowD[x], 4, x) 

    x=x+1
    if x>(disp_col-1): 
        x=0
        for i in range(disp_col):
            rowA[i]=rowB[i]
            rowB[i]=rowC[i]
            rowC[i]=rowD[i] 
            rowD[i]="_"

    print_display(rowA, rowB, rowC, rowD) 

