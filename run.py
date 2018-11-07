# genfind.py
#
# A function that generates files that match a given filename pattern

import os
import shutil
import fnmatch
import json

# Set config
with open('config.json') as json_data_file:
    data = json.load(json_data_file)
    src = data["src"]
    dst = data["dst"]

# Uncomment if your directory has an escape character
# src = "source/path"
# dst = "destination/path"

def gen_find(filepat,top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)

# You can change *.* to *.xslx if you are looking for xlsx files. 
# THis allows you to drill down what you are looking for.

if __name__ == '__main__':
    filesToMove = gen_find("*.*",src)
    for name in filesToMove:
        shutil.copy(name, dst)