lst=list(map(int,input("enter list:").split()))
def duplicate(lst):
    n=[]
    for x in lst:
        if x not in n:
            n.append(x)
    print("Updated list:",n)
duplicate(lst)    
