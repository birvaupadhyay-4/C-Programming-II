s=input("enter string:")
def freq(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]=freq[ch]+1
        else:
            freq[ch]=1
    print("charancter freq:",freq)
freq(s)    
