#!/usr/bin/python
import sys

if("--help" in sys.argv ):
    print "Usage: %s [NUMBER]..."%sys.argv[0]
    print "--help     display this help and exit"
    print "--version  output version information and exit"
elif( "--version" in sys.argv ):
    import version
    print "%s %s" % (sys.argv[0],version.package)
    print version.copyright
else:
	if( len( sys.argv ) == 1 ):
		fd = sys.stdin
	else:
		fd = open( sys.argv[1] )
	line_number = 0
	for line in iter(fd.readline, ''):
		line_number += 1
		print str( line_number ).rjust(10, ' '), line
