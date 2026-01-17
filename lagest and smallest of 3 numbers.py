a=int(input("Ënter a:"))
b=int(input("Ënter b:"))
c=int(input("Ënter c:"))

if (a>b and a>c):
    print("a is the largest")
    if (b>c):
        print("c is the smallest")
    else:
        print("b is the smallest")
        
if (b>a and b>c):
    print("b is the largest")
    if (a>c):
        print("c is the smallest")
    else:
        print("a is the smallest")

if (c>a and c>b):
    print("c is the largest")
    if (a>b):
        print("b is the smallest")
    else:
        print("a is the smallest")

              
