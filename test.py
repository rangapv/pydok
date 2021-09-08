#!/usr/bin/env python
class temp1(object):
    def __init__(self,func):
        print("Inside init")
        self.func = func 
    def __call__(self,a):
        print("hi")
        print("f is ")
        self.func(a) 
      # return self(a,b)
    def add(self,x,y):
        result = x + y
        return result

@temp1
def trg(a):
    print("Inside trg")
    print("Inside trg parm is ", a)
    return 3 

if __name__ == '__main__':
    #c = temp1()
   # print("cis ", c)
    #g = temp1().add(3,4)
    #print("add" , g)
    print("In main")
    trg(4)
