lst=list(map(int,input("Enter list:").split()))
def second(lst):
    lst.sort()
    print("Second largest number in list:",lst[-2])
second(lst)    
