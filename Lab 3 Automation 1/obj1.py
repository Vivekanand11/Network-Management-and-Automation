#!usr/bin/env python3
import csv
def Parse_file():    #define a function
 try:
    with open ("sshInfo.csv", newline='') as mycsvfile:   #open csv file
       reader=csv.DictReader(mycsvfile)                   #use dict reader to raed a csv file as a dictionary
       ordered_list=(list(reader))[0]                     #conert dict to list
    l1=dict(ordered_list)                                 #convert list to dict
       
    with open ("sshInfo.csv", newline='') as mycsvfile:
       reader=csv.DictReader(mycsvfile)
       ordered_list=(list(reader))[1]
    l2=dict(ordered_list)
   
    with open("sshInfo.csv", newline='') as mycsvfile:      #opena csv file
       reader=csv.DictReader(mycsvfile)                      #read csv file as a dict
       ip=[]                                                  #take empty list
       for row in reader:                          
        ip.append(row['ip'])                                  #append to the empty list
    return(l1,l2,ip)                                          #return dict, and devices ip
 except:
    return(-1,-1)                                             #if error return -1, -1
def main():
    a,b,c=Parse_file()                                 
    print(a,',',b,',',c)

if __name__=="__main__":                                      #namespace check
    main()
