#!/usr/bin/python3

# Orchard Project written By Dan Goodman, Signed 1/12/2018

# The Imports
import argparse
from subprocess import *
import os
# potentially use this: https://pypi.python.org/pypi/paramiko/1.8.0

# Arguments Section:

parser = argparse.ArgumentParser()


parser.add_argument("-u", "--username", help="username of DRAC/iDRAC")
parser.add_argument("-p", "--password", help="password of DRAC/iDRAC")
parser.add_argument("-h", "--host", help="host ip of DRAC/iDRAC")
parser.add_argument("-i", "--image", help=".iso/.img file location")
args = parser.parse_args()

# printinput = args.input
# print(printinput)

#call(['whoami'])
user = check_output("whoami")
print(user)