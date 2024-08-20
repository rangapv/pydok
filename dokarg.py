#!/usr/bin/env python3
#author:rangapv@yahoo.com

import os
import subprocess
import sys

import io
import re
import argparse
import shutil

from subprocess import PIPE

class Dangle1(argparse.Action):
  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Dangle1, self).__init__(option_strings, dest, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
    t1 = subprocess.run("ls -l", capture_output=True, shell=True, text=True, check=True)
    l = []
    count = 0
    dest=t1
    values=t1
    setattr(namespace, self.dest, values)

#@Action2(argparse.Action)
def findsh4(self):
    values=5
    return values

class docklist(argparse.Action):
   def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(docklist, self).__init__(option_strings, dest, **kwargs)

   def __call__(self, parser, namespace, values, option_string=None):
      t1 = subprocess.run("docker ps", capture_output=True, shell=True, text=True, check=True)
      #print("returncode is" + str(t1.returncode))
      if ( t1.returncode == 0 ):
       print ("the output is successful :" )
      else:
       print ("the command failed :" + str(t1))
      values=t1
      setattr(namespace, self.dest, values)

class Imagelist(argparse.Action):
   def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Imagelist, self).__init__(option_strings, dest, **kwargs)

   def __call__(self, parser, namespace, values, option_string=None):
     t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
     l = []
     for line in t1.stdout.splitlines():
       r = re.findall(r'\S+',line)
       l.append(r[2])
     #print("li " , l)
     values=l
     setattr(namespace, self.dest, values)

class ImageRepo(argparse.Action):
   def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(ImageRepo, self).__init__(option_strings, dest, **kwargs)

   def __call__(self, parser, namespace, values, option_string=None):
     t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
     l = []
     t = ()
     for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      t = (r[2],r[0])
      l.append(t)
     values=l
     setattr(namespace, self.dest, values)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='A python code to display argparse capability', fromfile_prefix_chars='@', epilog='Hope you like this program')
  parser.add_argument('-id', action=Dangle1) 
  
  parser.add_argument('-s', type=findsh4)
  parser.add_argument('-ld', action=docklist, help='to display the list of containers running')
  parser.add_argument('-il', action=Imagelist, help='to display the list of container iamges in this box')
  parser.add_argument('-ir', action=ImageRepo, help='to display the list of container iamges repo details')
 
  args = parser.parse_args()

  print(args) 
