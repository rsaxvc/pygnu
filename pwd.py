#!/usr/bin/python
import sys,os

if("--help" in sys.argv ):
	print "Usage: %s [NUMBER]..."%sys.argv[0]
	print "--help     display this help and exit"
	print "--version  output version information and exit"
elif( "--version" in sys.argv ):
	import version
	print "%s %s" % (sys.argv[0],version.package)
	print version.copyright
else:
    print os.getcwd()
