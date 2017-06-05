#!/usr/bin/python

import sys, os
try:
    ClipDirectory = sys.argv[1]
    NewRoll = sys.argv[2]
except StandError as msg:
    print "Please provide Enough Parameters. "
    print "EXAMPLE: python arriRenamerCLI.py /Users/DIT/Desktop/A001/A001_C002 A034"

if ClipDirectory == "":
    print "No Directory Specified, please add a Directory"
    print "EXAMPLE: python arriRenamerCLI.py /Users/DIT/Desktop/A001/A001_C002 A034"
    exit(0)
if NewRoll == "":
    print "Please Specifiy a Roll #"
    print "EXAMPLE: python arriRenamerCLI.py /Users/DIT/Desktop/A001/A001_C002 A034"
    exit(0)
for file in os.listdir(ClipDirectory):
    ari = 0
    with open(str(file), "r+b") as f:
        if str(f.read(4)) == "ARRI":
            f.seek(1272)
            if os.path.basename(file)[0:4] == f.read(4):
                f.write(NewRoll)
                f.seek(1688)
                f.write(NewRoll)
            f.close
            ari = 1
    if ari == 1:
        os.system("mv "+str(file)+" "+str(NewRoll)+str(file)[4:])
