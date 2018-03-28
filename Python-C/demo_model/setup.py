#!/usr/bin/env python  
  
from distutils.core import setup, Extension  
  
MOD = 'demo_model'  
setup(name=MOD, ext_modules=[Extension(MOD, sources=['demo_model.c'])])  