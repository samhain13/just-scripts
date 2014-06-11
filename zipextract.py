#! /usr/bin/python
"""
    A simple zip extractor.
"""
import os, sys, zipfile

if len(sys.argv) != 3:
    print """Usage:
    ./zipextract.py <path_to_zipfile> <filename_to_extract>
    ./zipextract.py <path_to_zipfile> --list
    """
    sys.exit()
if os.path.isfile(sys.argv[1]):
    with zipfile.ZipFile(sys.argv[1]) as czip:
        if sys.argv[2] == "--list":
            files = "\n".join(["    %s" % x for x in czip.namelist()])
            sys.exit("Files list:\n%s\n" % files)
        if sys.argv[2] in czip.namelist():
            czip.extract(sys.argv[2])
            sys.exit("%s has been extracted. Bye.\n" % sys.argv[2])
        else:
            sys.exit("Error: %s is not in the archive.\n" % sys.argv[2])
else:
    sys.exit("Error: Archive does not exist.\n")
