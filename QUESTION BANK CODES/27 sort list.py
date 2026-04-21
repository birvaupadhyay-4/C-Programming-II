lst=list(map(int,input("list:").split()))
def sort(lst):
    lst.sort()
    print("ascending:",lst)
    d=lst[::-1]
    print("descending:",d)
sort(lst)    
