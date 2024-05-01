class student:
    def __init__(self,name):
        self.name = name

s1 = student("sameer")
print(s1.name)   
del s1 #to delete the object in the class.
print(s1.name)  

class bomb:
    __name = "sameer"
s2=bomb()
print(s2.__name)
