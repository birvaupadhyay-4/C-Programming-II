lst=list(map(int,input("Enter list of numbers:").split()))
def sumoflist(lst):
    t=0
    for x in lst:
        t=t+x
    print("Sum of all elements:",t)

sumoflist(lst)    
