#! /usr/bin/env python
"""
    Typically used for copying "season episodes" from the download folder to
    another directory. Requires:
    
    1. file extension filter, a condition for os.listdir(os.getcwd())
    2. target directory, must already exist
    3. separator, a character with which to split the filenames
    4. index of the item in the filename that will be used as the new name of
       the copied file
    
    For example, say we downloaded episodes for "The Show of Hands" and the
    filenames are in the following format:
    
    the.show.of.hands.S01E[01, 02, 03, ...].HDTV.x264.avi
    
    And we wanted to copy those episodes to /home/username/the-show-of-hands,
    the command we will be using is:
    
    ./batch-renamer -e avi -d "/home/username/the-show-of-hands" -s "." -i 4
    
"""
import sys
import os
import shutil
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-e", "--extension", help="file extension", required=True)
ap.add_argument("-d", "--destination", help="target directory", required=True)
ap.add_argument("-s", "--separator", help="filename splitter", required=True)
ap.add_argument("-i", "--index", help="target directory",
    required=True, type=int)
ap.add_argument("--testing", help="test only", action="store_true")
args = ap.parse_args()


if __name__ == "__main__":
    if not os.path.isdir(args.destination):
        raise Exception("Target directory %s does not exist." % \
            args.destination)
    files = [x for x in os.listdir(os.getcwd()) if x.endswith(args.extension)]
    if not files:
        raise Exception("No %s files were found." % args.extension)
    for f in sorted(files):
        split_name = f.split(args.separator)
        if len(split_name) < args.index:
            raise Exception("Filename split out of range.")
        # We "upper" the filename and "lower" the extension for uniformity.
        new_name = "%s.%s" % (split_name[args.index].upper(),
            args.extension.lower())
        new_path = os.path.join(args.destination, new_name)
        sys.stdout.write("Copying %s to %s\n" % (f, new_path))
        if not args.testing:
            shutil.copyfile(f, new_path)
    sys.exit("Files have been copied to target directory. Goodbye.")

