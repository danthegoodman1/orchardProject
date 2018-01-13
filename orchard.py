#!/usr/bin/python3

# Orchard Project written By Dan Goodman, Signed 1/12/2018

# The Imports
import argparse
from subprocess import *
import os
# Well that was convinient: https://thornelabs.net/2014/04/16/dell-idrac-racadm-commands-and-scripts.html
# potentially use this: https://pypi.python.org/pypi/paramiko/1.8.0
# this for making a PXE server: https://www.ostechnix.com/how-to-install-pxe-server-on-ubuntu-16-04/

# Arguments Section:

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--username", help="username of DRAC/iDRAC, leave out to use default: 'root'", type=str)
parser.add_argument("-p", "--passwordfile", help="""
the file containing the password of DRAC/iDRAC.
This must be a file containing only the password.
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
else:
    if os.path.isfile(args.passwordfile) == True:
        f = open(args.passwordfile, 'r')
        f= f.read().strip()
        if f is not "":
            f = ""
        else:
            exit("Error, please put a password inside of the password file!")
if args.username is None:
    args.username = "root"



# SSH command to enable PXE boot on machine
print("Setting server at {0} to boot once".format(args.ip))
command1 = check_output("sshpass -f {passfile} ssh {usrname}@{ip} racadm config -g cfgServerInfo -o cfgServerBootOnce 1".format(passfile=args.passwordfile, usrname=args.username, ip=args.ip), shell=True)
print("Setting server at {0} to PXE boot".format(args.ip))
command1 = check_output("sshpass -f {passfile} ssh {usrname}@{ip} racadm config -g cfgServerInfo -o cfgServerFirstBootDevice PXE".format(passfile=args.passwordfile, usrname=args.username, ip=args.ip), shell=True)
print("Restarting server at {0}".format(args.ip))
command1 = check_output("sshpass -f {passfile} ssh {usrname}@{ip} racadm serveraction powercycle".format(passfile=args.passwordfile, usrname=args.username, ip=args.ip), shell=True)

user = check_output("whoami")
print(user.decode().strip())