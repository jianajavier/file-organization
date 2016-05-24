# Used for raw files from Photos application

import argparse

parser = argparse.ArgumentParser(description='Move photos into higher folder')

parser.add_argument('folder_location', type=str)

args = parser.parse_args()

#os.chdir(args.folder_location)

path_list = os.listdir(args.folder_location)

if not path_list:
    print "empty list"
else:
    for sub in path_list:
        # if sub is a directory, then go into the directory
        # take all the contents of the directory and dump it into a level above sub?
