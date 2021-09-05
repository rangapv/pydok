#!/usr/bin/env python

import os
import subprocess
import sys

import io
import re
import argparse

from subprocess import PIPE


class Prin(object):
  def __init__(self):
     #self = "Docker";
     print("Inside Prin") 
     print("Inside Prin"+ str(self)) 

  def New1(a):
    print ("Hello " + a.x);

class New2(argparse.Action):

   def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(New2, self).__init__(option_strings, dest, **kwargs)

   def __call__(self, parser, namespace, values, option_string=None):
      print("Inside new2")
      t1 = subprocess.run("docker ps", capture_output=True, shell=True, text=True, check=True)
      print("returncode is" + str(t1.returncode))
      if ( t1.returncode == 0 ):
       print("stdout is" + "\n" + t1.stdout)
       print ("the output is successful :" )
      else:
       print ("the command failed :" + str(t1))
      return t1.returncode

class Ancestor(argparse.Action):

     def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Ancestor, self).__init__(option_strings, dest, **kwargs)


     def __call__(self, parser, namespace, values, option_string=None):
     #def Ancestor(a,b):
        t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
        cl = []
        pl = []
        cc = 0
        pc = 0
        for line in t1.stdout.splitlines():
           r = re.findall(r'\S+',line) 
           pa = subprocess.run("docker inspect --format='{{{{.Parent}}}}' {}".format(r[2]), capture_output=True, shell=True, text=True, check=False)
           if (len(pa.stdout) > 1 ):
             print ("Image with ID:"+  r[2] + "is a CHILD")
             cl.append(r[2])
             cc = cc + 1
           else:
             print ("Image with ID:"+  r[2] + "is a PARENT")
             pl.append(r[2])
             pc = pc + 1 
        return(cl,pl,cc,pc)

class ImageArray(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(ImageArray, self).__init__(option_strings, dest, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
  #def ImageArray(a,string):
    b = "docker image ls"
    icl,ipl,icc,ipc = y.Ancestor(b)
    count = 0
    print(icl)
    icl = list(dict.fromkeys(icl))
    print(icl)
    print(ipl)
    for x in icl:
      c = "docker inspect --format='{{{{.RootFS.Layers}}}}' {}".format(x)
      t1 = subprocess.run(c, capture_output=True, shell=True, text=True, check=True)
    #  for line in t1.stdout.splitlines():
      r = re.findall(r'\S+', t1.stdout)
      cv = 0
      for iy in r:
          if (cv > 0):
            break
          l1 = subprocess.Popen(["echo {} | sed -e 's/\[//g; s/\]//g'".format(iy)], shell=True, text=True, stdout=PIPE, stderr=PIPE)
          l2,l3 = l1.communicate()
          for ip in ipl:
             # print("The child id is: {} and the Parent id is {}".format(x,ip))
              pc = "docker inspect --format='{{{{.RootFS.Layers}}}}' {}".format(ip)  
              pl = subprocess.run(pc, capture_output=True, shell=True, text=True, check=False)
              l11 = subprocess.Popen(["echo {} | sed -e 's/\[//g; s/\]//g'".format(pl.stdout)], shell=True, text=True, stdout=PIPE, stderr=PIPE)
              l21,l31 = l11.communicate()
              l24 = l21.replace("[","")
              l25 = l24.replace("]","")
              s = re.findall(r'\S+', l25)
              for g in s:
                g1 = l2.find(g) 
                if (g1 != -1): 
                  print("The image child id: {} is having Guardian: {}".format(x,ip))
                  count = count + 1
                  cv = 1  
    print("Total found parent is {}".format(count))      


class Imageid(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Imageid, self).__init__(option_strings, dest, **kwargs)


  def __call__(self, parser, namespace, values, option_string=None):
  #def Imageid(self):
    t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
    l = []
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      l.append(r[2])
    return(l)

class ImageRepo(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(ImageRepo, self).__init__(option_strings, dest, **kwargs)


  def __call__(self, parser, namespace, values, option_string=None):
  #def ImageRepo(self):
    t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
    l = [] 
    t = ()
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      t = (r[2],r[0]) 
      l.append(t)
    return(l)


class Findsha(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Findsha, self).__init__(option_strings, dest, **kwargs)


  def __call__(self, parser, namespace, values, option_string=None):
  #def Findsha(a,sh):
    scount = 0
    id = y.Imageid()
    for ip in id:
      pc = "docker inspect --format='{{{{.RootFS.Layers}}}}' {}".format(ip)
      pl = subprocess.run(pc, capture_output=True, shell=True, text=True, check=False)
      l21 = pl.stdout
      l24 = l21.replace("[","")
      l25 = l24.replace("]","")
      s = re.findall(r'\S+', l25)
      for g in s:
        g1 = sh.find(g)
        if (g1 != -1):
          print("The sha id: {} is having Guardian: {}".format(sh,ip))
          scount = scount + 1
    print("Total Count:" + str(scount))  


class Containerid(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Containerid, self).__init__(option_strings, dest, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
  #def Containerid(a):
    t1 = subprocess.run("docker container ls", capture_output=True, shell=True, text=True, check=True)
    l = []
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      l.append(t)
    return(l)


class Containerdid1(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Containerdid1, self).__init__(option_strings, dest, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
  #def Containerid1(a,string):
    t1 = subprocess.run("docker container ls", capture_output=True, shell=True, text=True, check=True)
    l = []
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      l.append(r[0])
    return(l)

class ContainerCheck(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(ContainerCheck, self).__init__(option_strings, dest, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
  #def ContainerCheck(self,x):
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
    return(count)


class Dangle1(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Dangle1, self).__init__(option_strings, dest, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
  #def Dangle1(a,string):
    value = int(string)

    t1 = subprocess.run("docker container ls", capture_output=True, shell=True, text=True, check=True)
    l = []
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      l.append(r[0])
    return(l)

class Dangle(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Dangle, self).__init__(option_strings, dest, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
  #def Dangle(self):
    li = self.Imageid()
   
    l = self.ImageRepo()
    di = 0
    si = 0
    for x in l:
      cc = self.ContainerCheck(x)
      if (cc == 0):
        di = di + 1
      else:
        si = si + 1
    print("The totat Dangling Image count is {} ".format(di))
    print("The total Iamge in use by container is {} ".format(si))

class New3(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(New3, self).__init__(option_strings, dest, **kwargs)

  def __call__(self, parser, namespace, values, option_string=None):
  #def New3(a,b):
    t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
    t2 = io.TextIOWrapper(t1)
    while True:
      line = t2.readline()
      if line != '':
        os.write(1, line)
      else:
        break

class Action1(argparse.Action):

     def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Action1, self).__init__(option_strings, dest, **kwargs)

     def __call__(self, parser, namespace, values, option_string=None):
         print('%r %r %r %r' % (namespace, values, option_string, parser))
         print("inside call1")
         t1 = subprocess.run("docker container ls", capture_output=True, shell=True, text=True, check=True)
         l = []
         print("ContainerID::::Up-Time::::Name")
         for line in t1.stdout.splitlines()[1:]:
          r = re.findall(r'\S\S\S',line)
          s = re.split(r"\s{3,}",line)
          print(s[0],"::", s[4],"::", s[5])
          l.append(r[0])
          values = l
         #setattr(namespace, self.dest, values)
         return values

     def __len__(self, parser, namespace, values, option_string=None):
         print("inside len")
         #print('%r %r %r' % (namespace, values, option_string))
         setattr(namespace, self.dest, values)
         #return values 

     def __call1__(**kwargs):
         #print('%r %r %r %r' % (namespace, values, self.dest, option_string))
         print("inside call1")
         t1 = subprocess.run("docker container ls", capture_output=True, shell=True, text=True, check=True)
         l = []
         for line in t1.stdout.splitlines():
           r = re.findall(r'\S+',line)
           l.append(r[0])
#         return(l)
         values = l
         print (values)
         #setattr(namespace, self.dest, values)
         return values 
#     @Action1 
     def Method1(option_strings, dest, nargs=None, **kwargs):
         g = "docker container ls"
         t1 = subprocess.run(g, capture_output=True, shell=True, text=True, check=True)
         l = []
         for line in t1.stdout.splitlines():
           r = re.findall(r'\S+',line)
           l.append(r[0])
#         return(l)
         values = l
         print(values) 
         setattr(namespace, self.dest, values)

     def Findsha(a,sh):
      scount = 0
      id = y.Imageid()
      for ip in id:
        pc = "docker inspect --format='{{{{.RootFS.Layers}}}}' {}".format(ip)
        pl = subprocess.run(pc, capture_output=True, shell=True, text=True, check=False)
        l21 = pl.stdout
        l24 = l21.replace("[","")
        l25 = l24.replace("]","")
        s = re.findall(r'\S+', l25)
        for g in s:
          g1 = sh.find(g)
          if (g1 != -1):
            print("The sha id: {} is having Guardian: {}".format(sh,ip))
            scount = scount + 1
        print("Total Count:" + str(scount))
     def findsh():
        print("Hello from findsh")

#@Action1
#def findsh1(self, dest=v):
#    print("hello")

#class Action2():
#   @Action1(argparse.Action)
#   def findsh1():
#       print("hello")

if __name__ == '__main__':
  y = Prin()
  parser = argparse.ArgumentParser(description='A python code to display Docker stats', epilog='Hope you like this program')
  parser.add_argument('-id', action=Dangle1) 
  parser.add_argument('-cid', action=Containerdid1)
  parser.add_argument('-z',  action=Dangle)
  parser.add_argument('-p', action=ImageArray)
  parser.add_argument('-a', action=Ancestor)
  parser.add_argument('-f', action=Findsha)
  parser.add_argument('-t', action=Action1)
#  parser.add_argument('-r', action=c)
#  parser.add_argument('-v', action=findsh1)

#  parser.add_argument('-s', action=Action1.Method1)
  args = parser.parse_args()
#  print(args)

#for 3.5  tg = subprocess.run(['docker', 'image', 'ls'], stdout=PIPE, stderr=PIPE)
