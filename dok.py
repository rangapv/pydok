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
      if (len(pa.stdout) > 1 ):
        print ("Image with ID:"+  r[2] + "is a CHILD")
      else:
        print ("Image with ID:"+  r[2] + "is a PARENT") 


  def Imageid(a):
    t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
    l = []
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      l.append(r[2])
    return(l)

  def ImageRepo(a):
    t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
    l = [] 
    t = ()
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      t = (r[2],r[0]) 
      l.append(t)
    return(l)


  def Containerid(a):
    t1 = subprocess.run("docker container ls", capture_output=True, shell=True, text=True, check=True)
    l = []
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      l.append(t)
    return(l)

  def ContainerCheck(a,x):
    count = 0
    t1 = subprocess.run("docker container ls", capture_output=True, shell=True, text=True, check=True)
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      r1 = re.search(r[1],x[0])
      r2 = re.search(r[1],x[1])
      if (r1 or r2):
       count = count + 1
    if (count == 0):
      print("The iamge with ID: {}".format(x[0]) +  "is dangling")
    else:
      print("The iamge with ID: {}".format(x[0]) + " is in use")


  def Dangle(a):
    li = y.Imageid()
#    for i in l:
#      print("The imageID is : {}".format(i)) 

    l = y.ImageRepo()
    for x in l:
      y.ContainerCheck(x)

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
#  y.New2("docker image ls")
 
# Get the Conatiner output
#  y.New2("docker container ls")  

  len1 = len(sys.argv)


  if ( len1 > 1):
    if (sys.argv[1] == "-a" ):
      y.Ancestor("docker image ls")
    elif (sys.argv[1] == "-d" ):
      y.Dangle()
    else:
      print("No command line")
  else:
    print("No comamnd line")
#for 3.5  tg = subprocess.run(['docker', 'image', 'ls'], stdout=PIPE, stderr=PIPE)
