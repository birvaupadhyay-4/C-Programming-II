s=input("sentence:")
def unique(s):
    words=s.split()
    u=[]
    for word in words:
        if word not in u:
            u.append(word)

    print("unique:"," ".join(u))
unique(s)        
