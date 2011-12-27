#!/usr/bin/python
import os,sys

paths = []
if( len( sys.argv ) > 1 ):
	lst = sys.argv[ -(len( sys.argv ) - 1 ) : ]
	paths.extend( lst )
else:
	paths.append( os.getcwd() )

for path in paths:
	if( len( paths ) > 1 ):
		print "%s:" % path
	dirList=os.listdir(path)
	for fname in dirList:
		if fname[0] != '.':
			print fname
	if( len( paths ) > 1 ):
		print 
