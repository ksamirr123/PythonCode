count =1
while(count<=100):
    print(count)
    count+=1

i=100
while(i>1):
    print(i)
    i-=1
 #multiplication
 
n = int(input("value of n:"))
j=1
while(j<=10):
    print(n,"x",j,"=",n*j)
    j+=1
#4
nums = [1,4,9,16,25,36,49,64,81,100]
f = 0
while f<len(nums):
    print(nums[f])
    f+=1  

#5
num = [1,4,9,16,25,36,49,64,81,100]
k = 0
y = 64
while k<len(num):
    if(num[k]==y):
        print("index of",y,"is","=",k)
    k+=1     

# break : it is uesd to break the loop and come out from that loop
# continue : it only skip the specific terms based on conditions and remains flow in loop    

m =0
while(m<5):
    print(m)
    if(m==3):
        break
    m+=1

#6
l = 1
while l<10:
     if(l==3):
         l+=1
         continue
     print(l)
     l+=1