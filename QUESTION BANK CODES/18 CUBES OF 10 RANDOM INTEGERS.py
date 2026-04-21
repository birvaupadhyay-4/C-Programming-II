import random
lst=[random.randint(1,25) for i in range(10)]
cube=[x**3 for x in lst]

print("Original:",lst)
print("Cubes:",cube)
