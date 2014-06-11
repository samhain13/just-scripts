#! /usr/bin/python
"""
    A simple zip extractor.
"""
import os, sys, zipfile

if len(sys.argv) != 3:
    print """Usage:
    ./zipextract.py <path_to_zipfile> <filename_to_extract>
    """
    sys.exit()
if os.path.isfile(sys.argv[1]):
    with zipfile.ZipFile(sys.argv[1]) as czip:
        if sys.argv[2] in czip.namelist():
            czip.extract(sys.argv[2])
            sys.exit("%s has been extracted." % sys.argv[2])
        else:
            sys.exit("Error: %s is not in the archive." % sys.argv[2])
else:
    sys.exit("Error: Archive does not exist.")
