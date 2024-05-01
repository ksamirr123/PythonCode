#default parameter = when we used value which is given in parameter
def fun(a=1,b=2):
    return a*b
mul  = fun()
print(mul)

##
def fun(a,b=2):
    return a*b
mul  = fun(5)#here it will take a =5
print(mul)