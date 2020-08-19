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
    t1 = os.system(b)
    if ( t1 == 0 ):
      print ("the output is successful :" + str(t1))
    else:
      print ("the command failed :" + str(t1))


if __name__ == '__main__':
  y = Prin()
  y.New2("docker image ls")
  y.New2("docker container ls")
  y.New2("docker image ls")
  
  tg = subprocess.run(['docker', 'image', 'ls'], stdout=PIPE, stderr=PIPE)
