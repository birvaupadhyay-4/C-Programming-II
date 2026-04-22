lst=list(map(int,input("Enter list:").split()))
def prime(n):
    if n<2:
        return False
    elif n>2:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                return True
def remove(lst):
    nlst=list(filter(lambda x:not prime(x),lst))
    print("List after removing prime nos.:",nlst)
    


remove(lst)
