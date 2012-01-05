#!/usr/bin/python
import os,sys

if("--help" in sys.argv ):
	print "Usage: %s [OPTION]... [FILE]..."%sys.argv[0]
	print "--help     display this help and exit"
	print "--version  output version information and exit"
elif( "--version" in sys.argv ):
	import version
	print "%s %s" % (sys.argv[0],version.package)
	print version.copyright
else:
	paths = []
	if( len( sys.argv ) > 1 ):
		paths.extend( sys.argv[ 1: ] )
	else:
		paths.append( "." )
	for path in paths:
		for curpath, dirs, files in os.walk(path,False):
			print curpath
			for filename in files:
				print os.path.join(curpath, filename)
