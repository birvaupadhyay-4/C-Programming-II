lst=list(map(int,input("Enter integers:").split()))
def sumeven(lst):
    t=0
    for x in lst:
        if x%2==0:
            t=t+x
    print("Sum of even numbers:",t)
sumeven(lst)    
