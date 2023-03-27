#!/usr/bin/python

import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import LST as LST


LAT=LST.dmstodec(19,49,27)
LON=LST.dmstodec(155,28,41,"W")
timezone=-10

#Loation  of Lulin
#LAT=LST.dmstodec(23,28,9,"N")
#LON=LST.dmstodec(120,52,22,"E")
#timezone=+8


#JD=LST.CaltoJD(now="now")
JD=LST.CaltoJD(2022,5,20,6,0,0)
print ("The observator position is LAT=",LAT,"LON=",LON)
print ("JD is",JD)

# UTC date and time
   #MAY 18, 2022        3:42: 2        19:39:44
   #MAY 19, 2022        3:46: 2        19:52:36
   #MAY 20, 2022        3:50: 2        20: 5: 7
Sun=LST.SunRaDec(JD)
print("The sun at  RA: ",Sun[0],"DEC: ",Sun[1])


print("Lat",LAT,"Lon",LON)
res1=LST.getAzEL(Sun[0],Sun[1],JD,LAT,LON)
print("The az=",res1[0],"EL=",res1[1],"HA=",res1[2])
res2=LST.getAzEL2(Sun[0],Sun[1],JD,LAT,LON)
print("The az=",res2[0],"EL=",res2[1],"HA=",res2[2])



print("Start")
for i in range(20,22):
    for j in range(0,24):
        JD=LST.CaltoJD(2022,5,i,j,0,0)
        Sun=LST.SunRaDec(JD)
        print(i,j,"RA:",LST.dectodms(Sun[0]),"DEC:",LST.dectodms(Sun[1]))
        res1=LST.getAzEL(Sun[0],Sun[1],JD,LAT,LON)
        print(i,j,"The az=",res1[0],"EL=",res1[1],"HA=",res1[2])
print("End")


