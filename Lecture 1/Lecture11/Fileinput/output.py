# FILE INPUT/OUTPUT = pyhton used method to read and write in a file.
 # open a File ---> 
f=open("demo.txt" ,"r")
data = f.read(5) #--> they will only read first five character of lines
print(data)
f.close()

# f.readline() --> used to read a complete single line

#write in a file
