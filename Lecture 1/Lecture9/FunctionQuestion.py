#1
list = ["sameer",6,"sufiyan","mango","games"]
def length(list):
    return len(list)
length = length(list)
print(length)

#2
def fun(list):
    for item in list:
        print(item,end=" ")

fun(list)   

#3
def factt(n):
    fact =1
    for i in range(1,n+1):
      fact = fact*i
      print(fact)
factt(5)     

#4
def converter(usd):
    inr = usd*83
    print(inr)

converter(100)    