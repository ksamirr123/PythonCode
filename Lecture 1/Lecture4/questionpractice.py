list = []
mov1 = input("first name:")
mov2 = input("second name:")
list.append(mov1)
list.append(mov2)
print(list)
#palindrome
list1 = [1,2,1,3]
copylist = list1.copy()
copylist.reverse()
if(copylist==list1):
    print("palindrome")
else:
    print("not palindrome")

    #count program
list2 = ["A","B","A","C","A","D"]
print(list2.count("A"))
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)
