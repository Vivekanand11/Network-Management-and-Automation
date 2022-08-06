from napalm import get_network_driver
import datetime, time

def Router1():
  driver=get_network_driver('ios')                          
  iosv12=driver('198.51.100.5', 'vivek', 'vivek456')        
  iosv12.open()                                         
  ios_output =iosv12.get_config()['running'] 
  area=time.gmtime()
  area1=time.strftime("%Y-%m-%d %H:%M:%S", area) 
  area2=(f'Router1 {area1}.txt')            
  with open(area2,'w') as f:
    f.write(ios_output)
  iosv12.close()
  return area2
def Router2():
  driver=get_network_driver('ios')                          
  iosv12=driver('198.51.100.6', 'vivek', 'vivek456')        
  iosv12.open()                                         
  ios_output =iosv12.get_config()['running'] 
  area3=time.gmtime()
  area4=time.strftime("%Y-%m-%d %H:%M:%S", area3) 
  area5=(f'Router1 {area4}.txt')            
  with open(area5,'w') as f:
    f.write(ios_output)
  iosv12.close()
  return area5
def Router3():
  driver=get_network_driver('ios')                          
  iosv12=driver('198.51.100.7', 'vivek', 'vivek456')        
  iosv12.open()                                         
  ios_output =iosv12.get_config()['running'] 
  area6=time.gmtime()
  area7=time.strftime("%Y-%m-%d %H:%M:%S", area6) 
  area8=(f'Router1 {area7}.txt')            
  with open(area8,'w') as f:
    f.write(ios_output)
  iosv12.close()
  return area8
def Router4():
  driver=get_network_driver('ios')                          
  iosv12=driver('198.51.100.8', 'vivek', 'vivek456')        
  iosv12.open()                                         
  ios_output =iosv12.get_config()['running'] 
  area9=time.gmtime()
  area10=time.strftime("%Y-%m-%d %H:%M:%S", area9) 
  area11=(f'Router1 {area10}.txt')            
  with open(area11,'w') as f:
    f.write(ios_output)
  iosv12.close()
  return area11

def main():
  v1=Router1()
  v2=Router2()
  v3=Router3()
  v4=Router4()
  return(v1, v2, v3, v4)             

if __name__ =="__main__":
  main()                             