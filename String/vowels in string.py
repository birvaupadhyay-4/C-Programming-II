str=input("Enter the string:")
vowels="aieouAEIOU"

count=0
for ch in str:
    if ch in vowels:
        count+=1
print(f"The number of vowels in {str} are {count}")
    
