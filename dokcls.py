#!/usr/bin/env python

import os
import subprocess
import sys

import io
import re
import argparse
import shutil

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

class Ancestor:

     def __call__(self, b):
     #def Ancestor(a,b):
        t1 = subprocess.run(b, capture_output=True, shell=True, text=True, check=True)
        cl = []
        pl = []
        cc = 0
        pc = 0
        for line in t1.stdout.splitlines()[1:]:
           r = re.findall(r'\S+',line) 
           pa = subprocess.run("docker inspect --format='{{{{.Parent}}}}' {}".format(r[2]), capture_output=True, shell=True, text=True, check=False)
           if (len(pa.stdout) > 1 ):
             print ("Image with ID:"+  r[2] + " is a CHILD")
             cl.append(r[2])
             cc = cc + 1
           else:
             print ("Image with ID:"+  r[2] + " is a PARENT")
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
    icl,ipl,icc,ipc = Ancestor.__call__(self, b)
    print("Parent list of images is ", ipl)
    print("Child list of images is ", icl)
    print("Parent count is ", ipc)
    print("Child count is ", icc)
    count = 0
    chcount = 0 
    icl = list(dict.fromkeys(icl))
    for x in icl:
      c = "docker inspect --format='{{{{.RootFS.Layers}}}}' {}".format(x)
      t1 = subprocess.run(c, capture_output=True, shell=True, text=True, check=True)
      print("inside for x loop", c)
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
                else:
                  chcount += 1
    print("Total found parent with child is {}".format(count))      
    print("Total found Children with parent is {}".format(chcount))      


class Imageid:

  def __call__(self):
    #print("inside Imageid") 
    t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
    l = []
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      l.append(r[2])
    #print("li " , l)  
    return(l)


class ImageRepo:

  def __call__(self):
    t1 = subprocess.run("docker image ls", capture_output=True, shell=True, text=True, check=True)
    l = [] 
    t = ()
    for line in t1.stdout.splitlines():
      r = re.findall(r'\S+',line)
      t = (r[2],r[0]) 
      l.append(t)
    #print("Imagerepo is ", l)
    return(l)


class Findsha(argparse.Action):

  def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Findsha, self).__init__(option_strings, dest, **kwargs)


  def __call__(self, parser, namespace, values, option_string=None):
  #def Findsha(a,sh):
    print('%r %r %r %r' % (namespace, values, option_string, parser))
    print("inside Findsha") 
    scount = 0
    id = Imageid.__call__(self)
    print("id ", id)
    for ip in id:
      pc = "docker inspect --format='{{{{.RootFS.Layers}}}}' {}".format(ip)
      pl = subprocess.run(pc, capture_output=True, shell=True, text=True, check=False)
      l21 = pl.stdout
      l24 = l21.replace("[","")
      l25 = l24.replace("]","")
      s = re.findall(r'\S+', l25)
      for g in s:
        g1 = values.find(g)
        if (g1 != -1):
          print("The sha id: {} is having Guardian: {}".format(values,ip))
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

class ContainerCheck:

  def __call__(self,x):
  #def ContainerCheck(self,x):
    #print("Inside container call") 
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
    li = Imageid.__call__(self)
   
    l = ImageRepo.__call__(self)
    di = 0
    si = 0
    for x in l[1:]:
      cd = ContainerCheck()
      cc = cd(x)
      if (cc == 0):
        di = di + 1
      else:
        si = si + 1
    print("The totat Dangling Image count is {} ".format(di))
    print("The total Image in use by container is {} ".format(si))

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

class Filecopy(argparse.Action):
      def __init__(self, option_strings, dest, nargs=None, **kwargs):
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Filecopy, self).__init__(option_strings, dest, **kwargs) 
    
    
      def __call__(self, parser, namespace, values, option_string=None):
          print('%r %r %r %r' % (namespace, values, option_string, parser))
          print("values" , values.name)
          print("name", namespace.ff.name)
          shutil.copyfile(namespace.ff.name,values.name)



class Action2:

     def __init__(self,f):
         self.f = f

     def __call__(self,a):
      #   print("as is ")
         return self.f 
    #     self.function(self, option_strings, dest, nargs=None, **kwargs)

class Action1(argparse.Action):

     def __init__(self, option_strings, dest, nargs=None, **kwargs):
         #print("inside action1")
         if nargs is not None:
             raise ValueError("nargs not allowed")
         super(Action1, self).__init__(option_strings, dest, **kwargs)

     def __call__(self, parser, namespace, values, option_string=None):
         print('%r %r %r %r' % (namespace, values, option_string, parser))
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
#     @staticmethod
     def Method1():
         print("Inside Method1")
     #def Method1(self, option_strings, dest, nargs=None, **kwargs):
   #  def Method1(self, dest, option_strings):
         g = "docker container ls"
         t1 = subprocess.run(g, capture_output=True, shell=True, text=True, check=True)
         l = []
         for line in t1.stdout.splitlines():
           r = re.findall(r'\S+',line)
           l.append(r[0])
#         return(l)
         values = l
         print(values) 
    #     setattr(namespace, self.dest, values)


#class Action2():
@Action2(argparse.Action)
def findsh4(self):
     print("hello")

if __name__ == '__main__':
#  y = Prin()
  q = Action1
  parser = argparse.ArgumentParser(description='A python code to display Docker stats', fromfile_prefix_chars='@', epilog='Hope you like this program')
  parser.add_argument('-id', action=Dangle1) 
  parser.add_argument('-cid', action=Containerdid1)
  parser.add_argument('-z',  action=Dangle)
  parser.add_argument('-p', action=ImageArray)
#  parser.add_argument('-a', action=Ancestor)
  parser.add_argument('-f', action=Findsha)
  parser.add_argument('-t', action=Action1)
  parser.add_argument('-i', action=findsh4)
#  parser.add_argument('-r', action=q.Method1())
  parser.add_argument('-s', action=Action1)
#  parser.add_argument('-c', action=Action1.Containercheck())
#  parser.add_argument('-v', action=findsh1)
  parser.add_argument('-ff', type=argparse.FileType('r'))
  parser.add_argument('-df', type=argparse.FileType('w'), action=Filecopy)
#  parser.add_argument('-s', action=Action1.Method1)
  args = parser.parse_args()
#  print(args)

#for 3.5  tg = subprocess.run(['docker', 'image', 'ls'], stdout=PIPE, stderr=PIPE)
