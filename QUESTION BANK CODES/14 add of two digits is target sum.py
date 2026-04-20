lst=list(map(int,input("Enter a list:").split()))
n=int(input("Enter sum:"))
def addoftwo(lst,n):
    print("Pairs are:",end="")
    
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==n:
                print(f"({lst[i]},{lst[j]})",end=" ")
addoftwo(lst,n)                    
