
from sys import argv

#a new script

script,filename,filename_new=argv

print("We are going to erase file %r" % filename)
input("?")

print("Opening the file ...")
target=open(filename,'w')

print("Truncating the file")
target.truncate()
outfile=target
target.close()

outfile=open(filename_new,'w')

print("Now will ask for three lines")

line1 = input("Give me Line 1 - ")
line2 = input("Line 2 - ")
line3 = input("Line 3 - ")
line4 = input("Line 4 - ")

print("write these to file")

outfile.write(line1)
outfile.write("\n")
outfile.write(line2)
outfile.write("\n")
outfile.write(line3)
oufile.write("\n")
outfile.write(line4)

outfile.close()
