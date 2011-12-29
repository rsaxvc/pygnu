#!/usr/bin/python
import sys,os

if("--help" in sys.argv or len( sys.argv ) == 1 ):
	print "Usage: %s [OPTION]... DIRECTORY..."%sys.argv[0]
	print "-p         makes directory and parents of directory"
	print "--help     display this help and exit"
	print "--version  output version information and exit"
elif( "--version" in sys.argv ):
	import version
	print "%s %s" % (sys.argv[0],version.package)
	print version.copyright
elif( "-p" in sys.argv ):
	for arg in sys.argv[ 2: ]:
		os.makedirs( arg )
else:
	for arg in sys.argv[ 1: ]:
		os.mkdir( arg )
