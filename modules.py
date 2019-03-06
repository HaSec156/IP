#!/bin/python2
import os
def ip_get():
    command = "curl ifconfig.co"
    process = os.popen(command)
    results = process.read()
    return results
print("Your Ip Is : "+print(ip_get())+" (-Tool By HaSec156-)")
