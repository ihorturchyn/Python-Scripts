#!/usr/bin/env python
import subprocess

ips = ["10.0.1.1", "10.0.1.3", "10.0.1.11", "10.0.1.51"]

for i in ips:
    print("Pinging" + i)
    ret = subprocess.call("ping -c 1 %i", shell=True, stdout=open('null.txt', 'w'), stderr=subprocess.STDOUT)
    if ret == 0:
        print(i + "is alive")
    else:
        print(i + "did not respond")
