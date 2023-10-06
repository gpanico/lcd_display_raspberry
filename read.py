#!/usr/bin/python3

import sys
from time import sleep
from os import system
import I2C_LCD_driver

disp_col=20
disp_row=4

fp=open("bulletin.txt","a")

mylcd=I2C_LCD_driver.lcd()

row = [ [ "`" for y in range(disp_row+1) ] for x in range(disp_col+1) ] 

def print_display(row):
    system("clear")
    for j in range(disp_row):
    	for i in range(disp_col):
        	print(row[i][j],end='')
        	mylcd.lcd_display_string(row[i][j], j+1, i)
    	print("")

##########################################

print_display(row)

x=0
while True:
    c=sys.stdin.read(1)
    sleep(0.1)
    print(c,file=fp,end='')

    if c.isprintable():
        row[x][disp_row]=c
    elif ord(c)==10:
        x=disp_col
        row[x][disp_row]=">"
    else:
        row[x][disp_row]="~"
    
    # print new char on the last line of display
    mylcd.lcd_display_string(row[x][disp_row], disp_row, x)

    x=x+1
    if x>=(disp_col):
        x=0
        for i in range(disp_col):
            for k in (range(disp_row)): 
                row[i][k]=row[i][k+1]
            row[i][disp_row]="_"

        print_display(row)

