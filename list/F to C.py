import random
nums=[random.randint(0,100) for i in range(5)]
print("Temp in Fahrenheit:",nums)
c=[(temp-32)*5/9 for temp in nums]
print("Temp in Celcius:",c)
