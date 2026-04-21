lst=list(map(int,input("enter list:").split()))
def squares(lst):
    n=list(x**2 for x in lst)
    print("Squares:",n)
squares(lst)    
