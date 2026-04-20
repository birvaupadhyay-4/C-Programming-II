import math
lst=list(map(int,input("Enter a number:").split()))
def fact(lst):
    fact=list(map(lambda x:math.factorial(x),lst))
    print("Factorials:",fact)
fact(lst)    
