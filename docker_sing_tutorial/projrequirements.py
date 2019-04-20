#!/usr/bin/python3
import scipy
import numpy
import sys
import os

# Helper functions

def getversionnumbers(v):
    versionlist = v.split('.')
    version = {"major": versionlist[0],"minor": versionlist[1] }
    return version

# OS versions check

def checkOS():
    print("Checking OS distribution...")

    releasefile = open("/etc/lsb-release","r")

    distrofound = 0
    for line in releasefile:
       if "DISTRIB_ID=Ubuntu" in line:
           distrofound = 1

    if distrofound:
       print("\tUbuntu found. Distribution OK")
    else:
       print("\tWARNING: The distribution is not Ubuntu. This software is optimized for Ubuntu, but may work on others")

# Python version checks
def pythonchecks():

    print("Checking python version...")
    pythonversion = sys.version_info
    print("\tFound python version: ")
    print("\t"+str(pythonversion))

    # only python > 3.5.x acceptable
    if ( pythonversion[0] < 3 ):
        print("\tPython major version must be at least 3, exiting...")
        exit(1)

    if ( pythonversion[1] < 5 ):
        print("\tPython minor version must be at least 5, exiting...")
        exit(1)

    print("\tPython version OK.")

# sw versions checks
def checksw():
    
    print("Checking software versions...")

    targetversions={"scipy":"0.17.0","numpy":"1.11.0"}
    actualversions={"scipy":scipy.__version__,"numpy":numpy.__version__}
    #actualversions={"scipy":"1.0.5","numpy":"1.12.4"}

    for software in targetversions:
        versiont = getversionnumbers(targetversions[software]) 
        versiona = getversionnumbers(actualversions[software])
        if ((versiona["major"] >= versiont["major"]) and (versiona["minor"] >= versiont["minor"])):
           print("\t"+software+" version OK")
        else:
           print("\t"+software+" version not ok, found "+actualversions[software]+" required >= "+targetversions[software])


# main
checkOS()
pythonchecks()
checksw()

#numpy.show_config("atlas_info")


#numpy.test("fast")
