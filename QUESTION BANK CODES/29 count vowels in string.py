str=input("enter string:")
def countvowels(str):
    vowels="aeiouAEIOU"
    v=0
    for ch in str:
        if ch in vowels:
            v=v+1

    print("number of vowels:",v)
countvowels(str)    
    
            
