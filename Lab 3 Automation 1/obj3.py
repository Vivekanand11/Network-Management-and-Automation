#!usr/bin/env python3
from pythonping import ping                #pythonping to check connectivity
import csv
def student_name():
    return #VivekanandDhondji
def Is_Connected(b):
   try:
       cassey=ping(b,verbose=True)               #ping function that will be used to check conncetivity
       if cassey:
         return True
   except:
      return False
def Connected_Devices(b):    
 try:                    #function for connected devices
   list=[]
   for i in range(len(b)):
      if Is_Connected(b[i]):
       list.append(b[i])
   return(list)
 except:
    return(-1,-1)

def main():
   with open("sshInfo.csv", newline='') as mycsvfile:
       reader=csv.DictReader(mycsvfile)
       ip=[]
       for row in reader:
        ip.append(row['ip'])
   neistat=Connected_Devices(ip)
   print(neistat)

if __name__=="__main__":                     #namespace check
    main()
