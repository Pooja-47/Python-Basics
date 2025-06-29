"""To perfom various tasks on files (like open, read, write or close) a file.
Before reading or writing we have to open a file.
There are various modes (r,w,a, b(combined[rb,wb,ab..]), t(it is by default)...) 
r is a default mode"""

#READING:::
f=open("docx.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

"""To read a particular set of characters."""

f=open("docx.txt","r")
data=f.read(8)         #reads starting 8 chars including space
print(data)
print(type(data))
f.close()

"""To read one line at a time. Gives an empty line in op as it reads \n char.
If we already read the whole data it will return empty lines."""

"""f=open("docx.txt","r")
data=f.read()
print(data)"""

f=open("docx.txt","r")
line1=f.readline() #reads one line at a time(we can also specify the no. of chars to read.)
print(line1)
line2=f.readline()
print(line2)
f.close()

#WRITING::

A=open("docx.txt","w")  #"w"it truncates the old file and owr the new text.
write=A.write("This is a sample file.")
print(write)
print(type(write))
A.close()


A=open("docx.txt","a")
write=A.write("\nI want to be a programmer.") #adds new text at the end.\n to print in next line.
print(write)
print(type(write))
A.close()

"""f=open("sample.txt","w")  #if file does not exist creates a file named sample.txt.
data=f.write("I m a learner.")
print(data)
print(type(data))
f.close()"""



with open("docx.txt","r")as f:  #simple way to r,w,a.. file it autm. closes the file.
    changes=f.read()
    print(changes)

#DELETING FIlE::
"""we use  built-in osmodule to perform this task."""
import os
os.remove("sample.txt")
