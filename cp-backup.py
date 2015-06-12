#!/usr/bin/env python
import os, fnmatch
import sys

def all_files(root, patterns=['*'], single_level=False, yield_folders=False):
	for path, subdir, files in os.walk(root):
		if yield_folders :
			files.extend(subdir)
		files.sort()
		for name in files:
			for pattern in patterns:
				if fnmatch.fnmatch(name, pattern):
					yield os.path.join(path, name)
					break
		if single_level:
			break

for path in all_files('./', patterns=['*.py~HEAD']):
    if sys.argv[1]:
        #print "copying %s to %s" % (path, sys.argv[1])
        dir_of_file = os.path.join(sys.argv[1], os.path.split(path[1:])[0][1:])
        #print os.path.join(dir_of_file, os.path.split(path[1:])[1])
        if not os.path.exists(dir_of_file):
            os.makedirs(dir_of_file)
        print os.popen("mv %s %s" % (os.path.abspath(path), dir_of_file)).read()


