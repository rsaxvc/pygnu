#!/usr/bin/python
import os,sys

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
