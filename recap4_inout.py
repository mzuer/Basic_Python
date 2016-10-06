##########################
# input and output with files
##########################

# files are used to store permanently data or information on the disk

# Opening a file

outfile = open("myseq.fasta", "w")  
infile = open("myseq.fasta", "r")
# -> filename can be relative or absolute path
# -> access-mode: 'w' (write), 'r' (read; default) or 'a' (append), 'r+' (read and write)
# -> possible 3d argument: to control the output buffering 
#    (0: output transferred immediately to the file, which may be slow)
# built-in function open()
# returns an object of type file (link to a file in the filesystem)

# Closing a file

infile.close() 	
# -> terminates the connection
# -> flushes the output buffer (if any) to the actual file
# -> releases the lock on the open file (can be used by other applications)
# -> files automatically closed at the end of a Python program

# Reading from file

myfile = open("myseq.txt", "r")
a = myfile.readline()
print(a)
b = myfile.readline()
print(b)
myfile.close
# -> keeps track of the current position in the file
# (incremented after each read operation)

myfile.readline.rstrip() # to remove the \n at the right end of the line

# Parsing and other reading methods
# 2 10
# sp1 ACATACATTT
# sp2 AGCTCATCGG
myfile = open("myseq.fasta", "r")
line = myfile.readline()  	 # '2 15\n'
nseq, nchar = line.split(' ')  	 # nseq=2, nchar=10
line=myfile.readline()    	 # 'sp1 ACATACATTT\n'
k, v = line.split(' ')
seq={}
seq[k] = v

# Reading more than 1 line:
line = myfile.read(n)	# read the text n bytes (char) into a string next call
			# to readline will read the end of line+next one
lines = myfile.read()	# read entire file into a single string
lines = myfile.readlines()	# read entire file in a list of lines
myfile.seek(n)	# change the current file position to offset n for next read

# End of line
"\n" 	# end of line for UNIX/LINUX and MacOS X
"\r\n"	# end of line for Windows
"\r"	# end of line for MacOS up to version 9

f = open("test.txt", 'rU') # add U for universal end of line -> sure that files correctly read

# Reading an entire file
# best to read line by line
f = open("input.dat", "r")
while True:
	line = f.readline()
	if line:             # an empty line means the end of file
		line = line.rstrip()
	else:
		break

# iterable file objects:
# best and fastet way to read a file:
f = open("input.dat", "r")
for line in f:
	line = line.rstrip()
	#...
f.close()

# Writing to a file
f = open("input.txt", "w")   
# when access mode "w" -> the file is created if not already exists
# else overwritten; with "a" -> added at the end (or beginning of new one)
# access mode "r+": open for both reading and writing

f.write("some strings")
f.writeLines(aList)
f.flush()   # -> flushes the output buffer to actual file without closing

# Only strings are written/read to/from files
# Some methods to deal with complex objects:
x,y,z = 10, 50, 100
s = "ACCATGC"
D = {"CCC": "Pro", "ACC": "Thr"}
L = ["A", "T", "C", "G"]

f = open("datafile.txt", "w")
f.write(s+"\n")   # to have newline

f.write("%s, %s, %s\n" %(x,y,z))

f.write(str(L)+"$"+str(D)+"\n") # explicit conversion to string needed

f.write(' '.join(L))  #"A T C G"
#or
f.write('_'.join(L))  #"A_T_C_G"

for k, v in D.items():
	f.write("%s: %s\n"%(k,v))

# The % operator -> ued to format a printout [print(string % tuple)]
a = "AACTA"
b = 5
print("Length of sequence %s is %d nucleotides"%(a,b))

# Serialize/deserialize an object
# = transform it to a string that can be written to a file and read it back
import pickle
f = open("filename", "wb")
D = {"CCC":"Pro", "ACC":"Thr"}
pickle.dump(D, f)                 # write D to file object f
f.close()

f = open("filename", "rb")
E = pickle.load(f)

# !!! with pickle.load() and pickle.dump() -> need reading and writing in binary mode ("rb" and "wb")

# Risk of failing to open a file -> try-except construct to recover from a file error
filename = raw_input("Enter a file name: ")
try:
	f = open(filename, "r")
except:
	print("File cannot open")

# Variable file names
# File name usually given by a user and will change.
# Not ideally coded in the script, use sys module and call (command line):
# ...$..: ./myscript.py data/inputFile.txt
import sys
pyScriptName = sys.argv[0]   # name of the script
filename = sys.argv[1]	     # name of the file (data/inputFile.txt)

# File operations from the module os
chdir(path)	#=> changes current dir
getcwd()	#=> returns current dir
listdir(path)	#=> lists dir content
rmdir(path)	#=> removes directory
remove(path)	#=> removes file
rename(src,dst)	#=> moves from src to st

# File operations from os.path sub-modules
exists(path)	#=> does path exists?
isfile(path)	#=> is path a file?
isdir(path)	#=> is path a dir?
islink(path)	#=> is path a symbolic link?
join(*paths)	#=> joins path together
dirname(path)	#=> dir containing path
basename(path)	#=> path minus dirname
split(path)	#=> returns dirname and basename
