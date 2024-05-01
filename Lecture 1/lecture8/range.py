print(range(5))
#2
seq = range(10)
for i in seq:
    print(i)


#3
for j in range(6):#range(stop)
    print(j)

#4
for j in range(6,15):#range(start,stop)
    print(j)
#5
for j in range(6,15,2):#range(start,stop,end)
    print(j)
#sum of n natural number
n = int(input("value of n:"))
sum=0
for i in range(1,n+1):
    sum = sum+i

print(sum)