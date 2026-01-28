fact=1
i=int(input("Enter a number:"))
for j in range(1,i+1):
    fact=j*fact
    
print(f"factorial of {i}={fact}")
