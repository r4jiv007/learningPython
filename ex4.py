from sys import argv

filename = argv[1]
file = open(filename)

print file.read()

