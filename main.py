__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# imports

import os
import glob
import shutil
from zipfile import ZipFile
from os.path import isfile, join

# paths

base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")
data_path = os.path.join(base_path, "data.zip")

# 1

def clean_cache(): 
    if os.path.exists(cache_path):
        files = glob.glob(cache_path + "/*")
        for f in files:
            if os.path.isfile(f) or os.path.islink(f):
                os.remove(f)
            if os.path.isdir(f):
                shutil.rmtree(f)
        print("Cleaned cache")
    else:
        os.mkdir(cache_path)
        print("Directory 'cache' created")

# 2

def cache_zip(data_path, cache_path):
    with ZipFile(data_path, 'r') as zip_file:
        zip_file.extractall(path=cache_path)
        print("Unzipped zip file in cache directory")

# 3 

def cached_files():
    return [os.path.abspath(os.path.join(cache_path, p)) for p in os.listdir(cache_path) if isfile(join(cache_path, p))]

# 4

def find_password(cached_files): 
    for f in cached_files:
        file_content = open(f, "r").readlines()
        for line in file_content:
            if "password" in line:
                slice = line.find(' ')
                return line[slice + 1:-1]

# run functions

if __name__ ==  "__main__":
    clean_cache()
    cache_zip(data_path, cache_path)
    cached_files()
    print(find_password(cached_files()))