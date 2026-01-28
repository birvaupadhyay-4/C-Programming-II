alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit="01234567809"
a=0
d=0
s=input("Enter your string:")
for ch in s:
    if ch in alphabet:
        a=a+1

    if ch in digit:
        d=d+1

print("No. of alphabets=",a)
print("No. of digits=",d)
