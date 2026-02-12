import random
lst=[random.randint(1,30) for i in range(50)]
print("The list is:",lst)

new_list=[]
for i in lst:
    if i not in new_list:
        new_list.append(i)

print("Unique List is:",new_list)        
      
