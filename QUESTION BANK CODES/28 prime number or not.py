n=int(input("enter a number:"))
def prime(n):
    if n==2:
        print("prime")
    elif n<=0:
        print("invalid number")
    elif n==1:
        print("neither prime nor composite")
    else:    
        for i in range(2,n):
            if n%i!=0:
                print("prime")
                break
            else:
                print("not prime")
                break
prime(n)                
                
