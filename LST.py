#!/usr/bin/python

import datetime
import numpy as np


def normalize0toN(angle,limit):
    limit=float(limit)
    while angle >= limit:
        angle -= limit
    while angle < 0.0:
        angle += limit
    return angle


def dmstodec(dd,mm,ss,Dir="N"):
   dec=np.abs(dd)+(np.abs(mm)/60.)+(np.abs(ss)/3600.)
   if Dir == "S" or Dir == "W":
       sign=-1.0
   else:
       if dd<0 or mm<0 or ss<0:
           sign=-1.
       else:
          sign=1
   return dec*sign


def dectodms(dec):
   mm = (dec - int(dec))*60 #convert fraction hours to minutes
   ss = (mm - int(mm))*60   #convert fractional minutes to seconds
   dd = int(dec)
   mm = int(mm)
   ss = int(ss)
   return [dd,mm,ss]

def hmstodec(hh,mm,ss):
   #carefule using this one  RA should in 24 hours and rad(for cal) only 
   totalhh=np.abs(hh)+(np.abs(mm)/60.)+(np.abs(ss)/3600.)
   return totalhh/24.0*360

def dectohms(dec):
   #caurefule RA shouls only in rad and 24 hours. 
   hh=dec*24/360.
   if hh<0:
       hh=hh+24.0
   if 24.0<hh:
       hh=hh-24.0
   mm = (hh - int(hh))*60       #convert fraction hours to minutes
   ss = (mm - int(mm))*60       #convert fractional minutes to seconds
   hh = int(hh)
   mm = int(mm)
   ss = int(ss)
   return [hh,mm,ss]

def CaltoJD(year=0,month=0,day=0,hour=0,minute=0,second=0,now=""):
    #DUT1=-0.153  #2019,Sep,30
    #DUT1=-0.09952 #2022,Mar,18 UT1-UTC(sec).
    DUT1=-0.098 #2022,May,20.
    if now == "now":
       utcn=datetime.datetime.utcnow()
       year=utcn.year
       month=utcn.month
       day=utcn.day
       hour=utcn.hour
       minute=utcn.minute
       second=utcn.second+DUT1
    ut=float(hour)+float(minute)/60.+float(second)/3600.
    JD = (367*year) - int((7*(year+int((month+9)/12)))/4)+int((275*month)/9)+day + 1721013.5 + (ut/24)
    return JD


def getLST2(LAT,LON,JD):
    GMST = 18.697374558 + 24.06570982441908*(JD - 2451545)
    GMST = GMST % 24
    LON=LON/15.0   # degree to hours
    LST=GMST+LON
    if LST < 0:
        LST= LST+24
    return LST

def getLST(LAT,LON,JD):
    JD0=np.floor(JD)
    uth=(JD-JD0)*86400
    T=(JD-2451545.)/36525.
    T0=(JD0-2451545.)/36525.
    GMST=24110.54841+8640184.812866*T0+1.00273*uth+0.093104*T*T-0.0000062*T*T*T
    GMST=(GMST/3600.+12) % 24
    LON=LON/15.0   # degree to hours
    LST=GMST+LON
    if LST < 0:
        LST= LST+24
    return LST

def getHA(LAT,LON,JD,RA):
    LST=getLST(LAT,LON,JD)
    HA=(LST-RA+24.0) % 24
    if HA > 12.0:
        HA=HA-24.0
    return HA

def getAzEL(RA,DEC,JD,LAT,LON):
    HA=getHA(LAT,LON,JD,RA)
    HAD=HA*360./24.
    sinEL=np.sin(DEC*np.pi/180.)*np.sin(LAT*np.pi/180.)+np.cos(DEC*np.pi/180.)*np.cos(LAT*np.pi/180.)*np.cos(HAD*np.pi/180.)
    EL=np.arcsin(sinEL)
    cosaz=(np.sin(DEC*np.pi/180.)-(sinEL*np.sin(LAT*np.pi/180.)))/np.cos(EL)/np.cos(LAT*np.pi/180.0)
    Az=np.arccos(cosaz)
    #The Az is from cosaz, need change to 2pi-az if in west sky (HA >0).
    #not sure if thing are o.k if at very big -el
    if ( HA > 0):
        Az=2*np.pi-Az
    #Az=2*np.pi-Az
    return Az*180./np.pi,EL*180/np.pi,HA

def getAzEL2(RA,DEC,JD,LAT,LON):
    HA=getHA(LAT,LON,JD,RA)
    HAD=HA*360./24.
    x = np.cos(HAD * (np.pi / 180.0)) * np.cos(DEC* (np.pi / 180.0))
    y = np.sin(HAD * (np.pi / 180.0)) * np.cos(DEC* (np.pi / 180.0))
    z = np.sin(DEC * (np.pi / 180.0))
    xhor= x*np.cos((90.-LAT)*(np.pi/180.0))-z*np.sin((90.-LAT)*(np.pi/180.0))
    yhor= y
    zhor= x*np.sin((90.-LAT)*(np.pi/180.0))+z*np.cos((90.-LAT)*(np.pi/180.0))
    az = np.arctan2(yhor, xhor) * (180.0/np.pi)+180.
    alt = np.arcsin(zhor) * (180.0/np.pi)
    return az,alt,HA
#print dmstodec(155,28,40.8,"W")
#print dectodms(23.8)



def SunRaDec(JD):
    EJulianDays = JD-2451545.0
    Omega=2.1429-0.0010394594*EJulianDays
    MeanLongitude = 4.8950630+ 0.017202791698*EJulianDays #Radians
    MeanAnomaly = 6.2400600+ 0.0172019699*EJulianDays
    EclipticLongitude = MeanLongitude + 0.03341607*np.sin(MeanAnomaly) +\
        0.00034894*np.sin( 2*MeanAnomaly )-0.0001134 -0.0000203*np.sin(Omega)
    EclipticObliquity=0.4090928-6.2140e-9*EJulianDays+0.0000396*np.cos(Omega)
    Sin_EclipticLongitude=np.sin(EclipticLongitude)
    Y=np.cos(EclipticObliquity) * Sin_EclipticLongitude
    X=np.cos(EclipticLongitude)
    RightAscension =np.arctan2( Y, X )
    if ( RightAscension < 0.0 ):
        RightAscension = RightAscension + 2*np.pi
    Declination =np.arcsin( np.sin( EclipticObliquity )* Sin_EclipticLongitude)
    #return RA in 24 hours(*180/pi*24/360), Dec in Degree
    return RightAscension*12/np.pi,Declination*180/np.pi
