from tempfile import mkstemp
from shutil import move
import glob, os

def find(name, directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(name):
                return (root, file)

def findFiles(name, directory):
    foundFiles = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(name):
                foundFiles.append((root, file))  
    return foundFiles              

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)