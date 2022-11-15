from sys import argv
if len(argv) == 1:
    print("No Files Specified!")

res = open("overall_res.csv", "w")
for name in argv[1:]:
    csv = open(name, "r")
    res.write(csv.read())
