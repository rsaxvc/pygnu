#!/usr/bin/python
import fileinput,sys

if("--help" in sys.argv or len( sys.argv ) < 2 ):
    print "Usage: %s [String] [optional file]"%sys.argv[0]
    print "--help     display this help and exit"
    print "--version  output version information and exit"
elif( "--version" in sys.argv ):
    import version
    print "%s %s" % (sys.argv[0],version.package)
    print version.copyright
else:
	prepend = str(sys.argv[1])

	if( len( sys.argv ) == 2 ):
		fd = sys.stdin
	else:
		fd = open( sys.argv[2] )

	line_number = 0
	for line in iter(fd.readline, ''):
		line_number += 1
		sys.stdout.write( prepend + line )
