#!usr/bin/env python3
import csv
import ipaddress                      #ipaddress module to check if the IP address is valid
def student_name():
    return #VivekanandDhondji
def IsValid(b):
   try:
       if ipaddress.ip_address(b): #returns an IPv4/6 address depending upon the type of IP address passed as argument.
         return True
   except:
      return False
def Val_IP(b):
   list=[]
   for i in range(len(b)): 
      if IsValid(b[i]):                  #checks if IP is valid
       list.append(b[i])                  #append ips to the list
   return(list)

def main():
   with open("sshInfo.csv", newline='') as mycsvfile:    
       reader=csv.DictReader(mycsvfile)
       ip=[]
       for row in reader:
        ip.append(row['ip'])
   v=Val_IP(ip)
   print(v)

if __name__=="__main__":                         #namespace check
    main()

