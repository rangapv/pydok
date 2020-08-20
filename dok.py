#!/usr/bin/env python

import os
import subprocess


from subprocess import PIPE


class Prin(object):
  def __init__(self):
    self.x = "Docker";
  
  def New1(a):
    print ("Hello " + a.x);

  def New2(a,b):
    t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
    print("stdout is" + "\n" + t1.stdout)
    print("returncode is" + str(t1.returncode))
    if ( t1.returncode == 0 ):
      print ("the output is successful :" )
    else:
      print ("the command failed :" + str(t1))


if __name__ == '__main__':
  y = Prin()
  y.New2("docker image ls")
 
# Get the Conatiner output
  y.New2("docker container ls")  

 
#for 3.5  tg = subprocess.run(['docker', 'image', 'ls'], stdout=PIPE, stderr=PIPE)
