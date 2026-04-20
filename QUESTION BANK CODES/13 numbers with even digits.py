lst=list(map(int,input("Enter numbers:").split()))
def evendigit(lst):
    n=[]
    for x in lst:
        if len(str(abs(x)))%2==0:
            n.append(x)
    print("Numbers with even digits:",n)
evendigit(lst)    
            
