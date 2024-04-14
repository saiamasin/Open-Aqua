import time
import os
import glob

os.system('modprobe w1-gpio') 
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close() 
  return lines

def read_temp():
  lines = read_temp_raw()
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string) / 1000.0
    return temp_c

while True:
  temp = read_temp()
  
  with open('temperature.txt', 'w') as log: # open file in write mode
    log.write(str(temp) + '\n') # write temperature as string

  time.sleep(0.6) # delay between readings
