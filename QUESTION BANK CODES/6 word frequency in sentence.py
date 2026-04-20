s=input("sentence:")
def freq(s):
    words=s.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]=freq[word]+1
        else:
            freq[word]=1

    print("freq:",freq)
freq(s)     
