s=input("Enter  a string:")
l=len(s)
print(f"Length of {s} is {l}")
vowls="aeiouAEIOU"

count=0
for ch in s:
    if ch in vowels:
        count+=1

print(f"Number of vowels in {s} are {count}")
c=l-count
print(f"Number of comsomamts in {s} are {c}")
