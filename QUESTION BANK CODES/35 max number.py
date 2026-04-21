from functools import reduce
lst=list(map(int,input("enter list:").split()))
def max(lst):
    n=reduce(lambda a,b:a if a>b else b,lst)
    print("max value:",n)
max(lst)
