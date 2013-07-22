#!/usr/bin/python
import fileinput,sys

if( len( sys.argv ) != 2 ):
	print "Usage: "+sys.argv[0]+" <string to prepend> "
	sys.exit(1)

prepend = str(sys.argv[1])

for line in sys.stdin.readlines():
	sys.stdout.write( prepend + line )
