#! /usr/bin/env python
"""
    A script that extracts audio from an MP4 video into an MP3 file.
    Requires the avconv command from the Libav package.
"""
import os
import subprocess
from optparse import OptionParser

def set_conditions(x, title_filter):
    is_mp4 = x.endswith(".mp4")
    has_string_in_title = title_filter in x if title_filter else True
    return has_string_in_title and is_mp4

op = OptionParser()
op.add_option("-f", "--filter", dest="title_filter", help="Title filter.")
(options, args) = op.parse_args()

songs = [x for x in os.listdir(os.getcwd()) \
    if set_conditions(x, options.title_filter)]

for song in songs:
    target_filename = "%s.mp3" % "".join(song.split(".")[:-1])
    command = ["avconv", "-i", song, "-vn", "-ab", "240k", "-ar", "44100",
        "-ac", "2", target_filename]
    p = subprocess.Popen(command)
    p.wait()

