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


def count1(self):
    t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
    contlen = t1.stdout
    #print(contlen)
    len1 = len(contlen.splitlines())
    print("**********************")
    print(f'total images are {len1-1}')
  #  t1 = subprocess.run("docker xxximage ls", capture_output=True, shell=True, text=True, check=True)

def count2(self):
    t1 = subprocess.run("docker container ps", capture_output=True, shell=True, text=True, check=True)
    contlen = t1.stdout
    #print(contlen)
    len1 = len(contlen.splitlines())
    print("**********************")
    print(f'total containers are {len1-1}')
    print("***********************")


class docklist(argparse.Action):
   def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(docklist, self).__init__(option_strings, dest, **kwargs)

   def __call__(self, parser, namespace, values, option_string=None):
      t1 = subprocess.run("docker stats --no-stream", capture_output=True, shell=True, text=True, check=True)
      t2 = subprocess.run("docker -v", capture_output=True, shell=True, text=True, check=True)
      t3 = subprocess.run("which docker", capture_output=True, shell=True, text=True, check=True)
      #print("returncode is" + str(t1.returncode))
      if ( t1.returncode == 0 ):
       print ("the output is successful :" + t1.stdout )
       print (f'the Docker version installed is \"{t2.stdout}\" and install directory is \"{t3.stdout}\"') 
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
 
     c1 = subprocess.run("docker container ps", capture_output=True, shell=True, text=True, check=True)
     cl = {}
     for line in c1.stdout.splitlines():
       r = re.findall(r'\S+',line)
       if (r[0] != "CONTAINER"):
         c2 = subprocess.run("docker inspect --format='{{{{.Config.Image}}}}' {}".format(r[0]), capture_output=True, shell=True, text=True, check=True)
         #print(t2)
         if ((c2.stdout) == "\n"):
          c2.stdout = "Error"
          inc = inc+1
         c3 = c2.stdout
         cl[c3.rstrip()] = (r[0]) 
         #cl[(r[0])] = c3.rstrip() 
     #print(cl)

     t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
     l = {}
     inc = 0
     print("**********************")
     print("Images in the box") 
     for line in t1.stdout.splitlines():
       r = re.findall(r'\S+',line)
       if (r[2] != "IMAGE"):
        t2 = subprocess.run("docker inspect --format='{{{{.RepoTags}}}}' {}".format(r[2]), capture_output=True, shell=True, text=True, check=True) 
        #print(t2)
        if ((t2.stdout) == "\n"):
         t2.stdout = "NO-CONTAINER use this Image"
         inc = inc+1
        t3 = t2.stdout
        l[t3.rstrip()] = (r[2])
        #l[(r[2])] = t3.rstrip()
         #print("li " , l)
        temp = t3.rstrip()
        temp1 = str(temp)[1:-1]
        #print ("temp is " + temp1)
        if temp1 in cl:
          print(f'Image: \"{temp1}\" with ID \"{r[2]}\" is used by the container \"{cl[temp1]}\" ')
        else:
          print(f'Image: \"{temp1}\" with ID \"{r[2]}\" is NOT used by any container at the moment')

     values=l,inc
    # print(l)
     setattr(namespace, self.dest, values)

class Containerlist(argparse.Action):
   def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Containerlist, self).__init__(option_strings, dest, **kwargs)

   def __call__(self, parser, namespace, values, option_string=None):
     t1 = subprocess.run("docker container ps", capture_output=True, shell=True, text=True, check=True)
     l = {}
     t = ()
     print("***********************")
     for line in t1.stdout.splitlines():
       r = re.findall(r'\S+',line)
       if (r[0] != "CONTAINER"):
         t2 = subprocess.run("docker inspect --format='{{{{.Config.Image}}}}' {}".format(r[0]), capture_output=True, shell=True, text=True, check=True)
         #print(t2)
         if ((t2.stdout) == "\n"):
          t2.stdout = "Error"
          inc = inc+1
         t3 = t2.stdout      
         l[(r[0])] = t3.rstrip()

     values=l
     print("The list of Containers running in the box and its repo-tag..")
     print(values)
     setattr(namespace, self.dest, values)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='A python code to display argparse capability', fromfile_prefix_chars='@', epilog='Hope you like this program')
  
  #parser.add_argument('-s', type=findsh4, help='to display the image sha4')
  parser.add_argument('-img', type=count1, help='to display the total images in the box')
  parser.add_argument('-ctan', type=count2, help='to display the total containers in the box')
  parser.add_argument('-dstat', action=docklist, help='to display the list Docker deamon running')
  parser.add_argument('-il', action=Imagelist, help='to display the list of images and if they are DANGLING')
  #parser.add_argument('-ir', action=ImageRepo, help='to display the list of container iamges repo details')
  parser.add_argument('-cl', action=Containerlist, help='to display the list of containers in this box')
  args = parser.parse_args()
#  tr = parser.parse_args()._get_kwargs() 
#  print(args)
#  print("print tr") 
#  print(tr)

#  for _, value in parser.parse_args()._get_kwargs():
#    if value is not None:
#        print(value)
