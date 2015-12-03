#!/usr/bin/env python

import os
import re
import shutil
from sys import argv
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

outputpath = os.getcwd() + "/output/"
start = 0
if os.path.exists(outputpath):
        print FAIL + "Debag Mode On --- \"output\" directory already exist!!! --- " + ENDC
	print ">>delete \"output\" directory ? " + BLUE + "(yes/no)" + ENDC
	de = 0
	while de < 1:
		yn = raw_input(">>")
		if yn == "yes":
			shutil.rmtree("output")
			print ">>" + FAIL + "\"output\" deleted!!!" + ENDC
			print ">>continue ? " + BLUE + "(yes/no)" + ENDC
			while start < 1:
				swit = raw_input(">>")
				if swit == "yes":start = 1
				elif swit == "no":break
				else:print ">>" + FAIL + "input \"yes\" or \"no\"" + ENDC
			break
		elif yn == "no":break
		else:print ">>" + FAIL + "input \"yes\" or \"no\"" + ENDC
else:start = 1
if start == 0:pass
else:
    os.mkdir("output")
    iselect = []
    path = os.getcwd()
    file_list = os.listdir(path)
    aa = 0
    bb = 0
    for file in file_list:
        file = os.path.join(path,file)
        if os.path.isdir(file):
            os.chdir(file)
	    bb = bb + 1
            for filename in os.listdir(file):
                name = file.split("/")[-1]
                if filename.endswith("ecd"):
			f1 = open(filename)
			outputname = filename.replace('.ecd',"."+name+'.csv')
			iselect.append(outputname)
			f2 = open(outputname,"w")
			for line1 in f1.readlines():
				if re.match('^[0-9]',line1):
					line2 = ",".join(line1.split("\t"))
					f2.write(line2)
			f2.close()
			shutil.move(outputname,path)
			os.chdir(path)
			print "running... in",name,filename,"->",outputname
			shutil.move(outputname, "output")
			f1.close()
			os.chdir(file)
			aa = aa + 1
            os.chdir(file)
    os.chdir(path)
    print WARNING + "--- integrate parameter select ---" + ENDC
    ab = aa/(bb-1)
    tsk = 0
    while tsk < 1:
	    lig = []
	    dd = 0
	    print ">>parameter select " + BLUE + "(auto/manual)" + ENDC
	    tsn = 0
	    while tsn < 1:
		    ts = raw_input(">>")
		    if ts == "auto":
			    break
		    elif ts == "manual":
			    break
		    else:
			    print ">>" +FAIL+ "input \"auto\" or \"manual\"" + ENDC
	    if ts == "auto":
		    while dd < ab:
			    print WARNING+"|"+ENDC+iselect[dd].split(".")[0]+WARNING+"| "+BLUE+"(on/off)"+ENDC+" on"
			    lig.append(iselect[dd].split(".")[0])
			    dd = dd + 1
	    elif ts == "manual":
		    while dd < ab:
			    jk = 0
			    while jk < 1:
				    str = raw_input(WARNING+"|"+ENDC+iselect[dd].split(".")[0]+WARNING+"| "+BLUE+"(on/off) "+ENDC)
				    if str == "on":
					    break
				    elif str == "off":
					    break
				    else:
					    print ">>" + FAIL + "input \"on\" or \"off\"" + ENDC
			    if str == "on":
				    lig.append(iselect[dd].split(".")[0])
			    else:
				    pass
			    dd = dd + 1
	    print ">>parameter select, ok? " + BLUE + "(ok/retry)" + ENDC
	    endc = 0
	    while endc < 1:
		    target = raw_input(">>")
		    if target == "ok":
			    tsk = 1
			    endc = 1
		    elif target == "retry":endc = 1
		    else:print ">>" + FAIL + "input \"ok\" or \"retry\"" + ENDC
    print "--------------------------------------------"
    print ">>file.csv -> " +GREEN+ "output" + ENDC
    print ">>Your Project Finished!!!"
    print "--------------------------------------------"
