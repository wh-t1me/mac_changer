#!/usr/bin/env python
import subprocess
a = input("""Enter mac address 
E.g. 00:11:22:33:44:55: """)
subprocess.call("ifconfig eth0 down" , shell = True)
subprocess.call("ifconfig eth0 hw ether " + a, shell = True)
subprocess.call("ifconfig eth0 up" , shell = True)
