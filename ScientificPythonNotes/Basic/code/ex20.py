#exercise 20

from sys import argv

script,input_file = argv

def print_all(f):

	print(f.read())
def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print( "hihi", line_count,f.readline())

current_file=open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("now rewind")
rewind(current_file)

print("print 3 lines")

current_line=1

print_a_line(current_line,current_file)

current_line=current_line+1

print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)
