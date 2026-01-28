s=input("Enter your string:")
print("First character:",s[0])
print("Last character:",s[-1])

if len(s)%2==1:
    print("Middle character:",s[len(s)//2])
elif len(s)==0:
    print("Given string is empty")
elif len(s)%2==0:
    print("Given string is even")
