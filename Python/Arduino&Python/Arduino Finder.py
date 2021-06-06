# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:53:55 2021

@author: ettor
"""

import serial

class mainer():
    def __init__(self):
        print("Devices Founder Program")
        print()
        self.check_for_serial()
    def check_for_serial(self):
        fuonded = 0
        a = [0,0,0,0,0,0,0,0,0]
        for i in range(1,100):
            name = 'COM'+str(i)
            try:
                machine = serial.Serial(name)
                print(machine.name)
                a[i]=1
                fuonded = 1
                #exit()
                self.starting()
            except Exception as e:
                #print(e,"-->",i)
                if fuonded == 0:
                        
                    if i == 99:
                        print("No serial device found")
                        #input("Press any key...")
                        self.starting()
                    else:
                        pass
    
    def starting(self):
        
        a = input("Redo the process?(Y/N) ")
        if a == "Y" :
            self.check_for_serial()
        else:
            exit()
mainer()