#writing to files
from sys import argv

print "enter file to create :-"
prompt = '>'
filename = raw_input(prompt)
file = open(filename,'w')
print "enter any value ?"
val = raw_input(prompt)

file.write(val+"\n")
file.close()

