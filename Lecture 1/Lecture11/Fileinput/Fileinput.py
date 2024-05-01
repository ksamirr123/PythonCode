##!
with open("format.txt","w") as f:
    f.write("this is new idea about java\n")
    f.write("this is new idea about Buisness\n")


###2
with open("format.txt","r") as f:  
    data = f.read()

new_data = data.replace("java","python")  
print(new_data)

with open("format.txt","w") as f:
    f.write(new_data)



