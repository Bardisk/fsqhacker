from sys import argv
if len(argv) == 1:
    print("No Files Specified!")

import cv2

from os import system

print("processing " + str(len(argv) - 1) + " files")

for name in argv[1:]:
    
    if len(name.split('.')) < 2:
        print("error found with: " + name)
        continue
    suffix = name.split('.')[-1]
    if suffix != "png":
        continue
    # do not change the picture color channels
    raw_pic = cv2.imread(name, -1)
    # print("processing " + name)
    # modify the last pixel slightly
    # note that the picture can be grey scaled
    if len(raw_pic.shape) == 3:
        if raw_pic[raw_pic.shape[0]-1][raw_pic.shape[1]-1][0] <= 127:
            raw_pic[raw_pic.shape[0]-1][raw_pic.shape[1]-1][0] += 1
        else:
            raw_pic[raw_pic.shape[0]-1][raw_pic.shape[1]-1][0] -= 1
    else:
        if raw_pic[raw_pic.shape[0]-1][raw_pic.shape[1]-1] <= 127:
            raw_pic[raw_pic.shape[0]-1][raw_pic.shape[1]-1] += 1
        else:
            raw_pic[raw_pic.shape[0]-1][raw_pic.shape[1]-1] -= 1
    # overwrite
    cv2.imwrite(name, raw_pic)
