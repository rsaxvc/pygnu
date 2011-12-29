#!/usr/bin/python
import sys

if("--help" in sys.argv ):
	print "Usage: %s [OPTION]..."%sys.argv[0]
	print "Print certain system information.  With no OPTION, same as -s."

	print " -a, --all                print all information, in the following order"
	print " -s, --kernel-name        print the kernel name"
	print " -n, --nodename           print the network node hostname"
	print " -r, --kernel-release     print the kernel release"
	print " -v, --kernel-version     print the kernel version"
	print " -m, --machine            print the machine hardware name"
	print "     --help     display this help and exit"
	print "     --version  output version information and exit"
elif( "--version" in sys.argv ):
	import version
	print "%s %s" % (sys.argv[0],version.package)
	print version.copyright
else:
	import os
	(sysname, nodename, release, version, machine) = os.uname()
	if len(sys.argv)==1:
		sys.argv.append("-s")

	if "-a" in sys.argv or "--all" in sys.argv:
		print sysname,nodename,release,version,machine
	else:
		if "-s" in sys.argv or "--kernel-name" in sys.argv:
			print sysname,
		if "-n" in sys.argv or "--nodename" in sys.argv:
			print nodename,
		if "-r" in sys.argv or "--kernel-releae" in sys.argv:
			print release,
		if "-v" in sys.argv or "--kernel-version" in sys.argv:
			print version,
		if "-m" in sys.argv or "--machine" in sys.argv:
			print machine,
		print
