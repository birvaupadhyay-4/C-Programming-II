lst=list(map(int,input("list:").split()))
def freq(lst):
    freq={}
    for x in lst:
        if x not in freq:
            freq[x]=1
        else:
            freq[x]=freq[x]+1
    print("Frequency : ",freq)
freq(lst)    
