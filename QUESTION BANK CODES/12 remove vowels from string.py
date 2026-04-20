str=input("enter a string:")
def vowels(str):
    v="aeiouAEIOU"
    n=""
    for ch in str:
        if ch not in v:
            n=n+ch
    print("String w/o vowels:",n)        
vowels(str)
