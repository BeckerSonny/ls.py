import os, sys
from stat import *
import datetime

def ls():
    # Options get all optionnal parameters like "-l"
    options = []
    for argv in sys.argv:
        if argv == __file__:
            continue
        # Check if an Argv is an optionnal paramater (take only "-l", else it's unknow)
        if argv[:1] == "-":
            if argv == "-l":
                options.append(argv)
            else:
                print("Unknow parameter {}.".format(argv))
                break
        else:
            # If the agrv is not the file name or an optionnal parameter, it is considered like a path
            # Launch function for get file
            return find_files_in_path(argv, options)
    return "No path found in argv"



def find_files_in_path(path, options):
    # Check if not a folder, find file
    if not os.path.isdir(path):
        return find_a_file(path, options)
    # If is folder print file with optionnal parameters
    for file in os.listdir(path):
        if "-l" not in options:
            print(file)
        else:
            print(file, "an more details")

ls()