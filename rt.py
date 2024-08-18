#!/usr/bin/env python

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
  #def Dangle1(a,string):
    #value = int(string)

    t1 = subprocess.run("ls -l", capture_output=True, shell=True, text=True, check=True)
    l = []
    count = 0
    dest=t1
    #print(t1)
    values=t1
    setattr(namespace, self.dest, values)
    #return(t1)

#@Action2(argparse.Action)
def findsh4(self):
    values=5
    return values

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='A python code to display argparse capability', fromfile_prefix_chars='@', epilog='Hope you like this program')
  parser.add_argument('-id', action=Dangle1) 
  
  parser.add_argument('-s', type=findsh4)
  
  args = parser.parse_args()
 
  print(args.id)
  print(args.s)
