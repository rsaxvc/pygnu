#!/usr/bin/python
import sys

if( len( sys.argv ) == 1 ):
	print ""
elif("--help" in sys.argv ):
	print "Usage: %s [OPTION]... [STRING]..."%sys.argv[0]
	print "--help     display this help and exit"
	print "--version  output version information and exit"
elif( "--version" in sys.argv ):
	import version
	print "%s %s" % (sys.argv[0],version.package)
	print version.copyright
else:
	for arg in sys.argv[ 1: ]:
		print arg,
