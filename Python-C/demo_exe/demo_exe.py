#!/usr/bin/python2.7
# coding=UTF-8 

import commands  
import os  
main = "demo_exe"  

#获取每一行的数据
f = os.popen(main)    
data = f.readlines()    
f.close()    
print data  

#获取全部的返回数据
os.system(main)