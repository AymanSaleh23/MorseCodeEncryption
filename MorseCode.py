# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:59:17 2022

@author: as292
"""
import winsound
import time

def enCrypt(Name):
    Name = Name.upper()
    Name = Name.replace(' ',"       ")
    Name = Name.replace('A',".- ")
    Name = Name.replace('B',"-... ")
    Name = Name.replace('C',"-.-. ")
    Name = Name.replace('D',"-.. ")
    Name = Name.replace('E',". ")
    Name = Name.replace('F',"..-. ")
    Name = Name.replace('G',"--. ")
    Name = Name.replace('H',".... ")
    Name = Name.replace('I',".. ")
    Name = Name.replace('J',".--- ")
    Name = Name.replace('K',"-.- ")
    Name = Name.replace('L',".-.. ")
    Name = Name.replace('M',"-- ")
    Name = Name.replace('N',"-. ")
    Name = Name.replace('O',"--- ")
    Name = Name.replace('P',".--. ")
    Name = Name.replace('Q',"--.- ")
    Name = Name.replace('R',".-. ")
    Name = Name.replace('S',"... ")
    Name = Name.replace('T',"- ")
    Name = Name.replace('U',"..- ")
    Name = Name.replace('V',"...- ")
    Name = Name.replace('W',".-- ")
    Name = Name.replace('X',"-..- ")
    Name = Name.replace('Y',"-.-- ")
    Name = Name.replace('Z',"--.. ")
    Name = Name.replace('1',".---- ")
    Name = Name.replace('2',"..--- ")
    Name = Name.replace('3',"...-- ")
    Name = Name.replace('4',"....- ")
    Name = Name.replace('5',"..... ")
    Name = Name.replace('6',"-.... ")
    Name = Name.replace('7',"--... ")
    Name = Name.replace('8',"---.. ")
    Name = Name.replace('9',"----. ")
    Name = Name.replace('0',"----- ")
    print(Name)
    return Name
    
def palySoundBeep (code):
    for index in code:
        if index == '.':
            winsound.Beep(750,50)
        elif index == '-':
            winsound.Beep(750,150)
        elif index == ' ':
            pass
        time.sleep(0.05)
    
while True: 
    inputs = str(input("to encrypt: "))
    
    if inputs != "-1":
        codex = enCrypt(inputs)
        palySoundBeep(codex)
    else :
        break;
        
print ("Done")