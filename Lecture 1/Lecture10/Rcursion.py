# RECURSION : when function call itself again and again.
##1
def rec(n):
    if(n==0):
        return
    print(n)
    rec(n-1)
   ## print("End")

rec(5)    

##2
def factt(n):
    if(n==0 or n==1):
        return 1
    return n*factt(n-1)
print(factt(5))

##3
def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)
print(sum(4))
