from sys import argv
if len(argv) == 1:
    print("No Files Specified!")

from os import system

print("processing " + str(len(argv) - 1) + " files")

for name in argv[1:]:
    
    if len(name.split('.')) < 2:
        print("error found with: " + name)
        continue
    suffix = name.split('.')[-1]
    if suffix != "xml":
        continue