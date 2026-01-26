str=input("Enter your string:")
lower = ""
upper = ""
toggle = ""
for ch in str:
    if ch>='A' and ch<='Z':
        lower = lower + chr(ord(ch) + 32)
        upper = upper + ch
        toggle = toggle + chr(ord(ch) + 32)

    elif ch>='a' and ch<='z':
        lower=lower+ch
        upper=upper+chr(ord(ch)-32)
        toggle=toggle+chr(ord(ch)-32)

    else:
        lower=lower+ch
        upper=upper+ch
        toggle=toggle+ch

print("Lower:",lower)
print("Upper:",upper)
print("Toggle:",toggle)
