from tempfile import mkstemp
from shutil import move
import glob, os , os.path

def find(name, directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(name):
                return (root, file)

def findFiles(name, directory, parent):
  
    foundFiles = []
    for root, dirs, files in os.walk(directory):
        for adir in dirs:
            if adir.endswith(parent):
               path = root +("/"+adir)
               for r, d, f in os.walk(path):
                    for afile in f:
                     if afile.endswith(name):
                        foundFiles.append((r, afile))  
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