import os, sys, stat
from datetime import datetime

"""
Main function, check argv
"""
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
    print("No path found in argv")

"""
Find files in the path and define if it's a folder or a prefixe
"""
def find_files_in_path(path, options):
    # Display files in this list
    list_of_files = []
    # Check if its a folder or not, if not a folder find files with prefixe
    if os.path.isdir(path):
        list_of_files = os.listdir(path)
    else:
        list_of_files, path = find_files_with_prefixe(path)
        
    # Loop on files and display data with options
    for file in list_of_files:
        if "-l" not in options:
            # Ignore hide file like ls
            if file[:1] != ".":
                print(file)
        else:
            # Ignore hide file like ls
            if file[:1] != ".":
                path_join = os.path.join(path, file)
                # Find data of last modification
                file_time_last_modification = round(os.stat(path_join).st_mtime)
                file_time_last_modification = datetime.fromtimestamp(file_time_last_modification)
                print("{} {} {}".format(stat.filemode(os.stat(path_join).st_mode), file_time_last_modification, file))

"""
Return a list of files with the prefixe
"""
def find_files_with_prefixe(path):
    prefixe = path.split('/')[-1:][0]
    folder = "/".join(path.split('/')[:-1])
    if not prefixe:
        return False
    list_of_files = []
    for file in os.listdir(folder):
        #if prefixe is good add to list
        if file[:len(prefixe)] == prefixe:
            list_of_files.append(file)

    if not list_of_files:
        print("No file or directory found for this path '{}'.".format(path))
    return list_of_files, folder


ls()