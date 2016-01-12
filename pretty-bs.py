#! /usr/bin/env python
"""
    Pretty prints horrible HTML code.
    
    Usage:
        ./pretty-bs.py filename.html
            or output to another file
        ./pretty-bs.py filename.html > output.html
"""
import os
import sys
import re
from BeautifulSoup import BeautifulSoup
from argparse import ArgumentParser

def prettify_2space(soup, indent=4):
    # blatant copypasta from stackoverflow.com/questions/15509397/..
    # custom-indent-width-for-beautifulsoup-prettify
    r = re.compile(r"^(\s*)", re.MULTILINE)
    return r.sub(r"\1" * indent, soup.prettify())

def get_args():
    ap = ArgumentParser()
    ap.add_argument("html", help="HTML file to parse and pretty print.")
    args = ap.parse_args()
    return args

def main():
    args = get_args()
    if not os.path.isfile(args.html):
        sys.exit("HTML file does not exist.")
    with open(args.html) as f:
        soup = BeautifulSoup(f.read().decode("utf-8"))
    sys.stdout.write(prettify_2space(soup))


if __name__ == "__main__":
    main()

