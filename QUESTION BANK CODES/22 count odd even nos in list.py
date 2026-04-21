lst=list(map(int,input("Enter list:").split()))
def count(lst):
    odd=0
    even=0
    for x in lst:
        if x%2==0:
            even=even+1

        else:
            odd=odd+1
    print("Odd nos.:",odd)
    print("even nos.:",even)
count(lst)     
