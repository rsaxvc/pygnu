#!/usr/bin/python
import os,sys

if("--help" in sys.argv ):
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
		paths.append( os.getcwd() )
	for path in paths:
		if( len( paths ) > 1 ):
			print "%s:" % path
		for fname in os.listdir(path):
			if fname[0] != '.':
				print fname
		if( len( paths ) > 1 ):
			print 
