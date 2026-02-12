import random
nums=[random.randint(-20,20) for i in range(30)]
print("Original list:",nums)
pos=[i for i in nums if i>0]
neg=[i for i in nums if i<0]
print("Positive numbers:",pos)
print("Negative numbers:",neg)



       
