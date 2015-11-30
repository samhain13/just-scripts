#! /usr/bin/env python
"""
    A script that extracts audio from an MP4 video into an MP3 file.
    Requires the avconv command from the Libav package.
"""
import os
import subprocess
from argparse import ArgumentParser

def conditions(item, title_filter, video_file_extension):
    """Extra conditions used in the songs list comprehension."""
    is_video = item.endswith(".%s" % video_file_extension)
    has_string_in_title = title_filter in item if title_filter else True
    return has_string_in_title and is_video

description = "Extracts MP3 audio from video files in the current directory."

ap = ArgumentParser(description=description)
ap.add_argument("-f", help="title filter")
ap.add_argument("-e", help="video file extension", default="mp4")
ap.add_argument("-ab", help="audio bitrate", default="240", type=int)
ap.add_argument("-ar", help="audio rate", default="44100", type=int)
ap.add_argument("-ac", help="audio channels", default="2", type=int)
ap.add_argument("--overwrite", help="overwrite existing files",
    action="store_true")
args = ap.parse_args()

songs = [x for x in os.listdir(os.getcwd()) if conditions(x, args.f, args.e)]

for song in songs:
    target_filename = "%s.mp3" % "".join(song.split(".")[:-1])
    if args.overwrite and os.path.isfile(target_filename):
        os.remove(target_filename)
    command = ["avconv", "-i", song, "-vn", "-ab", "%dk" % args.ab,
        "-ar", str(args.ar), "-ac", str(args.ac), target_filename]
    p = subprocess.Popen(command)
    p.wait()


