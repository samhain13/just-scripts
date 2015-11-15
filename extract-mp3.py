#! /usr/bin/env python
"""
    A script that extracts audio from an MP4 video into an MP3 file.
    Requires the avconv command from the Libav package.
"""
import os
import subprocess
from argparse import ArgumentParser

def set_conditions(x, title_filter):
    is_mp4 = x.endswith(".mp4")
    has_string_in_title = title_filter in x if title_filter else True
    return has_string_in_title and is_mp4

description = "Extracts audio from MP4 files in the current directory."

ap = ArgumentParser(description=description)
ap.add_argument("-f", "--title-filter", help="title filter")
args = ap.parse_args()

songs = [x for x in os.listdir(os.getcwd()) \
    if set_conditions(x, args.title_filter)]

for song in songs:
    target_filename = "%s.mp3" % "".join(song.split(".")[:-1])
    command = ["avconv", "-i", song, "-vn", "-ab", "240k", "-ar", "44100",
        "-ac", "2", target_filename]
    p = subprocess.Popen(command)
    p.wait()

