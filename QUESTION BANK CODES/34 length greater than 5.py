names=input("Enter list").split()
def length(names):
    n=list(filter(lambda x:len(x)>5,names))
    print("Names with length greater than 5:",n)
length(names)    
    
