#!/usr/bin/python

import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import LST as LST

#           name ra ram ras +-dec

class JD():
    def __init__(self,year,month,day,hour,mins,sec):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hour = int (hour)
        self.mins = int (mins)
        self.sec = float (sec)
        self.JD=LST.CaltoJD(year,month,day,hour,mins,sec)
        print (year,month,day,hour,mins,sec,"JD=",self.JD)
        self.nighList=np.linspace(self.JD-1,self.JD+1,500)
        self.yearList=np.zeros(shape=(11,500))
        for i in range(11) :
            #print(i-5,month+i-5)
            year2=year
            month2=month+i-5
            if (month+i-5) <=0:
                year2=year-1
                month2=month+i-5+12
            elif (month+i-5)>12:
                year2= year+1
                month2=month+i-5-12
            JD2=LST.CaltoJD(year2,month2,1,0,0,0)
            self.yearList[i,:]=np.linspace(JD2-1,JD2+1,500)
    def toJD(name):
        return 30

source=[]
with open('3c_catalog', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        d=row[0].split()
        for i in range (1,7):
            d[i]=float(d[i])
        #name=d[0]
        source.append([d[0],d[1],d[2],d[3],d[4],d[5],d[6]])
        #print(namelist[0],namelist[1],namelist[2])


#The Position of Nobeyama
#LAT=LST.dmstodec(35,56,30,"N")
#LON=LST.dmstodec(138,28,33,"E")
#timezone=+9

#The Location of Honolulu
LAT=LST.dmstodec(19,49,27)
LON=LST.dmstodec(155,28,41,"W")
timezone=-10

#Loation  of Lulin
#LAT=LST.dmstodec(23,28,9,"N")
#LON=LST.dmstodec(120,52,22,"E")
#timezone=+8

tz=timezone
time=LST.CaltoJD(now="now")

print ("The observator position is LAT=",LAT,"LON=",LON)
print ("JD now is",time)

Az=[]
El=[]
for so in source:
    RA=LST.dmstodec(so[1],so[2],so[3])
    DEC=LST.dmstodec(so[4],so[5],so[6])
    #print(so[1],so[2])
    #print ("The", so[0], "position is RA =",RA," DEC =",DEC)
    #print ("\tHA is", LST.getHA(LAT,LON,time,RA))
    #print ("\tAZ",LST.getAzEL(RA,DEC,time,LAT,LON)[0])
    #print ("\tEL",LST.getAzEL(RA,DEC,time,LAT,LON)[1])
    Az.append(LST.getAzEL(RA,DEC,time,LAT,LON)[0])
    El.append(LST.getAzEL(RA,DEC,time,LAT,LON)[1])

SunPos=LST.getAzEL(LST.SunRaDec(time)[0],LST.SunRaDec(time)[1],time,LAT,LON)
print(SunPos)

Azser=[]
ELser=[]
for ts in np.arange(time-0.1,time+1.,0.01):
    Azser.append(LST.getAzEL(LST.SunRaDec(ts)[0],LST.SunRaDec(ts)[1],ts,LAT,LON)[0])
    ELser.append(LST.getAzEL(LST.SunRaDec(ts)[0],LST.SunRaDec(ts)[1],ts,LAT,LON)[1])

fig, ax = plt.subplots()
#ax.plot(position,c='green')
ax.plot(Az,El,c='red', marker="o",ls="")
ax.plot(Azser,ELser,c='green')
ax.plot(SunPos[0],SunPos[1],c='yellow',marker="o",ls="")

ax.set_xlabel('Azimuth')
ax.set_ylabel('EL')
ax.set_xlim(0,360)
#ax.axvline(x=-12-tz)
#ax.axvline(x=12-tz)
#range(0,360,10)
ax.set_xticks(range(0,361,10))
xt=['N']+['']*8+['E']+['']*8+['S']+['']*8+['W']+['']*8+['N']
ax.set_xticklabels(xt)

#ax.set_xticks(range(0,370,10),minor="True")
#ax.set_xticks([0,90,180,270,360],labels=['N','E','S','W','N'])

ax.set_ylim(-10,90)
ax.axhline(y=0)

ax.set_yticks(range(-10,91,5))
yt=['','','0','','10','','20','','30','','40','','50','','60','','70','','80','','90']
ax.set_yticklabels(yt)
#ax.grid('on', which='major', axis='x')
#ax.grid('on', which='major', axis='y')

plt.show()
#print(position)
