#!/usr/bin/env python

import os
import subprocess
import sys

import io
import re

from subprocess import PIPE


class Prin(object):
  def __init__(self):
    self.x = "Docker";
  
  def New1(a):
    print ("Hello " + a.x);

  def New2(a,b):
    t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
    print("returncode is" + str(t1.returncode))
    if ( t1.returncode == 0 ):
      print("stdout is" + "\n" + t1.stdout)
      print ("the output is successful :" )
    else:
      print ("the command failed :" + str(t1))


  def Ancestor(a,b):
    t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line) 
      ki = "1ebbaebd9704"
      pa = subprocess.run("docker inspect --format='{{{{.Parent}}}}' {}".format(r[2]), capture_output=True, shell=True, text=True, check=False)
      print(len(pa.stdout)) 
      if (len(pa.stdout) > 1 ):
        print ("Image with ID:"+  r[2] + "is a CHILD")
      else:
        print ("Image with ID:"+  r[2] + "is a PARENT") 

  def New3(a,b):
    t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
    t2 = io.TextIOWrapper(t1)
    while True:
      line = t2.readline()
      if line != '':
        os.write(1, line)
      else:
        break 

if __name__ == '__main__':
  y = Prin()
  y.New2("docker image ls")
 
# Get the Conatiner output
  y.New2("docker container ls")  

  len1 = len(sys.argv)
  print("the length is" + str(len1))


  if ( len1 > 1):
    if (sys.argv[1] == "-a" ):
      y.Ancestor("docker image ls")
    else:
      print("No command line")
  else:
    print("No COmamnd line")
#for 3.5  tg = subprocess.run(['docker', 'image', 'ls'], stdout=PIPE, stderr=PIPE)
