#!/usr/bin/python

import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import LST2 as LST
import time

def JDtoGregorian(JD):
    f=JD+1401-38+int(int((4*JD+274277)/146097)*3/4)
    e=4*f+3
    g=int((e%1461)/4)
    h=5*g+2
    if (JD-int(JD) >= 0.5 and JD-int(JD) < 0.75):
        addday=1
    else:
        addday=0
    D=int((h%153)/5)+1+addday
    M=((int(h/153)+2)%12)+1
    Y=int(e/1461)-4716+int((12+2-M)/12)
    #Next 4 line not finished yet, at 2022/5/21 3 A.M
    seconds=(JD-int(JD))*24*60*60
    S=int(round(seconds%(60)))
    mm=(int(seconds/60))%60
    H=int(LST.normalize0toN(seconds/3600-12,24))
    return Y,M,D,H,mm,S



def leapYear(year):
    if year%4 ==  0:                    # 如果除以 4 能整除
        if year%100 == 0:              # 如果除以 100 能整除
            if year%400 == 0:          # 如果除以 400 能整除，就是閏年
                leapyear=1
                #print(f'{year} 是閏年')a
            else:
                leapyear=0
                #print(f'{year} 是平年')
        else:
          leapyear=1
          #print(f'{year} 是閏年')
    else:
        leapyear=0
    return leapyear
        #print(f'{year} 是平年')

year=1990
month=1
day=1
hour=3
mins=0
second=0
JD=LST.
for i in range(0,801,1): 
    leapyear=leapYear(year)

    if hour >=24:
        hour=hour-24
        day=day+1

    if (day==29 and month==2 and leapyear==0):
        day=1
        month=3
    if (day==30 and month==2 and leapyear==1):
        daay=1
        month=3
    # move to next month if month 31 in 4,6,9,11
    if (day==31 and (month in[4,6,9,11])):
        day=1
        month=month+1

    if (day==32 and (month in[1,3,5,7,8,10])):
        day=1
        month=month+1

    if (day==2 and month==12):
        day=1
        month=1
        year=year+1
    print(year,month,day,hour)
    hour=hour+3

'''
for days in np.arange(0.1,0.6,0.05):
    JD=2459720.217+days
    f=JD+1401-38+int(int((4*JD+274277)/146097)*3/4)
    e=4*f+3
    g=int((e%1461)/4)
    h=5*g+2
    if (JD-int(JD) >= 0.5 and JD-int(JD) < 0.75):
        addday=1
    else:
        addday=0
    D=int((h%153)/5)+1+addday
    M=((int(h/153)+2)%12)+1
    Y=int(e/1461)-4716+int((12+2-M)/12)
    JD_float = "{:.6f}".format(JD)
    #print(JD_float,Y,M,D,int((4*JD+274277)/146097),int(int((4*JD+274277)/146097)*3/4),\
    #  h,h%153,(h%153)/5)
    #print(JD_float,Y,M,D)
'''

'''
for i in range(1,29):
    for j in range(0,23):
        year=2021
        month=6
        day=i
        hour=j
        mins=59
        secs=59
        res=JDtoGregorian(LST.CaltoJD(year,month,day,hour,mins,secs))
        #print(year,month,day,hour,mins,secs,res)
        if day != res[2]:
            print("Not Equal")
            print(year,month,day,hour,mins,secs,res)

'''

'''
while True:
    utcn=datetime.datetime.utcnow()
    year=utcn.year
    month=utcn.month
    day=utcn.day
    hour=utcn.hour
    minute=utcn.minute
    second=utcn.second
    JD=LST.CaltoJD(year,month,day,hour,minute,second)
    res=JDtoGregorian(JD)
    print("JD=",JD)
    print(year,month,day,hour,minute,second,res)
    time.sleep(1)
'''

'''
for i in range(20,22):
    for j in range(0,24):
        JD=LST.CaltoJD(2022,5,i,j,0,0)
        Sun=LST.SunRaDec(JD)
        print(i,j,"RA:",LST.dectodms(Sun[0]),"DEC:",LST.dectodms(Sun[1]))
        res1=LST.getAzEL(Sun[0],Sun[1],JD,LAT,LON)
        print(i,j,"The az=",res1[0],"EL=",res1[1],"HA=",res1[2])
print("End")
'''

