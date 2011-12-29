#!/usr/bin/python
import sys

if("--help" in sys.argv ):
	print "Usage: %s"%sys.argv[0]
	print "--help     display this help and exit"
	print "--version  output version information and exit"
elif( "--version" in sys.argv ):
	import version
	print "%s %s" % (sys.argv[0],version.package)
	print version.copyright
else:
	import os
	print os.uname()[4]
