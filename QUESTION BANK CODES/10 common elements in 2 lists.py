l1=list(map(int,input("Enter list 1:").split()))
l2=list(map(int,input("Enter list 2:").split()))
def common(l1,l2):
    c=[]
    for x in l1:
        if x in l2 and x not in c:
            c.append(x)
    print("Common elements:",c)
common(l1,l2)    
