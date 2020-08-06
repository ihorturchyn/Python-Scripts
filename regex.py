#!/usr/bin/env python
import re

pattern = r'(\S{0,15})\s(\S{0,15}).*(\d{12})->(\d{12})\sevent type 2'
file = open('example.txt').read()
array = file.split(',')

for i in (array):
    mo = re.findall(pattern, i)
    print(mo)
    
file.close
