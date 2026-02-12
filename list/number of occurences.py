import random
nums=[random.randint(1,10) for i in range(20)]
print("The list is:"lst)
num=int(input("Enter a number:"))

if (num in lst):
    num_occ=[]
    for i,ele in enumerate(lst):
        if(ele==num):
            num_occ.append(i)
    print(f"occurences of{num} in list are at position:{num_occ}")
else:
    print("Number does not exist in list")
    
