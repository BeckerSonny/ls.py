import os, sys
from stat import *
import datetime

def ls():
    print("Args ==> ", sys.argv)
    options = []
    path = None
    for argv in sys.argv:
        if argv == __file__:
            continue
        if argv[:1] == "-":
            if argv == "-l":
                options.append(argv)
        else:
            return find_files_in_path(argv, options)
    return "No path found"



def find_files_in_path(path, options):
    print("find Files path", path)
    print("find Files options", options)


ls()