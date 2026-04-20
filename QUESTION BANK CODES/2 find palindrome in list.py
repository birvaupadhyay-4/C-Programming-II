def pali(lst):
    result=[]
    for x in lst:
        if str(x)==str(x)[::-1]:
            result.append(x)
    print("Pali nos.:",result)

lst=list(map(int,input("Enter list").split()))
pali(lst)
