str=input("string:")
def vowcon(str):
    v,c=0,0
    vowels="aeiouAEIOU"
    for ch in str:
        if ch.isalpha():
            if ch in vowels:
                v=v+1

            else:
                c=c+1
    print("vowels",v)
    print("con:",c)

vowcon(str)
