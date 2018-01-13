#!/usr/bin/python3

# Orchard Project written By Dan Goodman, Signed 1/12/2018

# The Imports
import argparse
from subprocess import *
import os
# potentially use this: https://pypi.python.org/pypi/paramiko/1.8.0

# Arguments Section:

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--username", help="username of DRAC/iDRAC", type=str)
parser.add_argument("-p", "--passwordfile", help="""
the file containing the password of DRAC/iDRAC
this must be a file containing only:

        password:PASSWORD
        
where PASSWORD is the password ;)
""", type=str)
parser.add_argument("-ip", "--ip", help="host ip of DRAC/iDRAC", type=str)
parser.add_argument("-i", "--image", help=".iso/.img file location", type=str)
parser.add_argument("-e", "--enablepxe", help="enable pxe boot on server", type=bool)
args = parser.parse_args()

# printinput = args.input
# print(printinput)
# if printinput is None:
#     printinput = "no input provided"

# First check to see if sshpass is installed:
try:
    check_sshpass = check_output("dpkg -l sshpass", shell=True)
except CalledProcessError as e:
    check_sshpass = e.output
    print(check_sshpass.decode().strip())
    exit("sshpass not installed, please install sshpass using 'apt-get install sshpass' in order to avoiding storing sensitive passwords in the bash history")
    
# Check if a password file was given
if args.passwordfile is None:
    exit("please provide a file with a password in it!")

# SSH command to enable PXE boot on machine
print(args.ip)

user = check_output("whoami")
print(user.decode().strip())