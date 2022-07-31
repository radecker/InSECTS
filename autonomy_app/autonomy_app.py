#!/usr/bin/env python3

#from TCPClient import TCPClient
#from UDPClient import UDPClient
#from BaseApp import BaseApp
#import message_pb2 as proto
import time

# Autonomy Rules
#
# initial: fan speed @ 25%
# initial: baffle = closed
#
# if average temp >95C @ 25% speed, increase fan speed to 50%
# if single temp is >100C @25% speed, increase fan speed to 50%

# if average temp >100C @ 50% speed, increase fan speed to 75%
# if single tmep is >105C @25% speed, increase fan speed to 50%

# if average temp >105C @ 75% speed, increase fan speed to 100%
# if single tmep is >110C @25% speed, increase fan speed to 50%
#
# if average temp <95C @50% speed, decrease fan speed to 25%
#bla

# if average temp <100C @75% speed, decrease fan speed to 50%
#

# if average temp <105C @100% speed, decrease fan speed to 75%
#

# if fan (0) OR servomotor (1) temp >50C @ baffle = closed, set baffle = half-open
# if fan OR servomotor temp >50C @ baffle = half-open, set baffle = full-open
#
# if fan OR servomotor temp <0C @ baffle = full-open, set baffle = half-open
# if fan OR servomotor temp <0C @ baffle = half-open, set baffle = closed

# CSV Formate (FOR CODE TO WORK)
# X axis sensor 0 to sensor 5 
# Y axis sensor temp time taken 
# 1 output every second from each sensor 1 through 5



import csv
import numpy as np

class AutonomyApp ():
    def __init__(self) -> None:
        #super().__init__("vehicle.autonomy_app")
        self.baffle = 0 #0 is closed 1 is half 2 is open
        self.fanspeed = 1 # 0 is off 1 is 25% 2 is 50% 3 is 75% 4 is 100%
        self.csv = r"C:\Users\skido\OneDrive\Desktop\Grad School\DRAGONFLYCUBE-SAT\Autonomy_Script_Test.csv"
        
    def read_tempSensors(self): 
        tempSensors = []
        AveSingeSensorTemp = []
        with open(self.csv,mode = 'r')as file:
            csvFile = csv.reader(file)
            counter =0 
            for lines in csvFile:
                if counter ==0:
                    counter =1 
                else : # Takes last 5 seconds of data for max & average
                    l=len(lines)
                    AveSingeSensorTemp.append(int(lines[l-5]))
                    AveSingeSensorTemp.append(int(lines[l-4]))
                    AveSingeSensorTemp.append(int(lines[l-3]))
                    AveSingeSensorTemp.append(int(lines[l-2]))
                    AveSingeSensorTemp.append(int(lines[l-1]))
                    tempSensors.append(np.mean (AveSingeSensorTemp))
                    AveSingeSensorTemp = []
            return tempSensors #return array 
        
    def send_fanspeed_and_baffle(self):
        if self.fanspeed ==1 :
            #Function to send 1 to ardunio (xxx volts)
            print(self.fanspeed)
        elif self.fanspeed ==2 :
            #Function to send 2 to ardunio (xxx volts)
            print(self.fanspeed)
        elif self.fanspeed ==3 :
            #Function to send 3 to ardunio (xxx volts)
            print(self.fanspeed)
        elif self.fanspeed ==4 :
            #Function to send 4 to ardunio (xxx volts)
            print(self.fanspeed)
            
        if self.baffle == 0:
            #Function to send 0 to baffle XXX
            print(self.baffle)
        elif self.baffle ==1:
            #Function to send 1 to baffle XXX
            print(self.baffle)
        elif self.baffle ==2:
            #Function to send 2 to baffle XXX
            print(self.baffle)
            
    def run(self):
        print("Autonomy System Online")
        self.send_fanspeed_and_baffle()
        time.sleep (10)
        while True:
            allTemps =self.read_tempSensors() #value return stored in all temps
            if np.mean(allTemps) > 95 and self.fanspeed==1: 
                self.fanspeed=2
            elif np.mean(allTemps) > 100 and self.fanspeed==2: 
                self.fanspeed=3
            elif np.mean(allTemps) > 105 and self.fanspeed==3: 
                self.fanspeed=4
            elif np.mean(allTemps) < 95 and self.fanspeed >=2: 
                self.fanspeed=1
            elif np.mean(allTemps) < 100 and self.fanspeed >=3: 
                self.fanspeed=2
            elif np.mean(allTemps) < 105 and self.fanspeed ==4: 
                self.fanspeed=3
                     
            if np.max(allTemps) > 100 and self.fanspeed==1:
                self.fanspeed=2
            elif np.max(allTemps) > 105 and self.fanspeed==2:
                self.fanspeed=3
            elif np.max(allTemps) > 110 and self.fanspeed==3:
                self.fanspeed=4
            elif np.max(allTemps) < 100 and self.fanspeed >=2:
                self.fanspeed=1
            elif np.max(allTemps) < 105 and self.fanspeed >=3:
                self.fanspeed=2
            elif np.max(allTemps) < 110 and self.fanspeed ==4:
                self.fanspeed=3
    
            if (allTemps[0] > 50 or allTemps[1] > 50) and self.baffle ==0: 
                self.baffle =1
            elif (allTemps[0] > 55 or allTemps[1] > 55) and self.baffle ==1: 
                self.baffle =2
            elif (allTemps[0] < 50 or allTemps[1] < 50) and self.baffle >=1: 
                 self.baffle =0
            elif (allTemps[0] < 55 or allTemps[1] < 55) and self.baffle ==2: 
                 self.baffle =1
                 
            self.send_fanspeed_and_baffle()
            time.sleep(30)
            


if __name__ == "__main__":
    a= AutonomyApp()
    a.run() # Runs the app
    
