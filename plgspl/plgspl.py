# -*- coding: utf-8 -*-

__version__ = "0.0.0"


import sys
import os
import json
from plgspl.to_pdf import to_pdf
from plgspl.classlist import classlist


def append_cwd(s):
    return os.path.join(os.getcwd(), s)


def main():
    print("Running plgspl version %s..." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    cmd = sys.argv[1]
    if cmd == 'pdf':
        args = list(map(append_cwd, sys.argv[2:]))
        if len(args) < 2:
            print("Please provide all required files.")
            sys.exit(1)
        for f in args[0:1]:
            if not os.path.isfile(f):
                print("Unable to find the given file: %s" % f)
                sys.exit(1)
        file_dir = args[2] if len(args) == 3 else None
        if file_dir and not os.path.isdir(file_dir):
            print("Unable to find the given file directory: %s" % f)
            sys.exit(1)
        to_pdf(args[0], args[1], file_dir)
    elif cmd == "classlist":
        f = sys.argv[2]
        if not os.path.isfile(f):
            print("Unable to find the given file: %s" % f)
            sys.exit(1)
        classlist(f)
