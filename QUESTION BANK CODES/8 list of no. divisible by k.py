lst=list(map(int,input("Enter list of numbers:").split()))
k=int(input("Enter a number:"))
def divisible(lst,k):
    n=[]
    for x in lst:
        if x%k==0:
            n.append(x)
    if n==[]:
        print(f"none of the numbers are divisible by {k}")
    else:
        print(f"Numbers divisble by {k}:",n)

divisible(lst,k)    
