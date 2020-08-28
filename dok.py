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

  def ImageArray(a):
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
    return(count)

  def Dangle(a):
    li = y.Imageid()
#    for i in l:
#      print("The imageID is : {}".format(i)) 

    l = y.ImageRepo()
    di = 0
    si = 0
    for x in l:
      cc = y.ContainerCheck(x)
      if (cc == 0):
        di = di + 1
      else:
        si = si + 1
    print("The totat Dangling Image count is {} ".format(di))
    print("The total Iamge in use by container is {} ".format(si))
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
      mcl,mpl,chc,phc = y.Ancestor("docker image ls")
      print("The total Child Image count is {}".format(chc))
      print("The total Parent Image count is {}".format(phc))
    elif (sys.argv[1] == "-d" ):
      y.Dangle()
    elif (sys.argv[1] == "-p" ):
      y.ImageArray()
    elif (sys.argv[1] == "-f" ):
      sh = sys.argv[2]
      y.Findsha(sh)
    else:
      print("Allowed options are -a/-d/-p")
  else:
    print("No comamnd line")
#for 3.5  tg = subprocess.run(['docker', 'image', 'ls'], stdout=PIPE, stderr=PIPE)
