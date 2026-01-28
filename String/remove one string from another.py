s1=input("Enter string:")
s2=input("Enter string to be removed:")
s3=s1.replace(s2,"")

if s3!=s1:
    print("Final string:",s3)
else:
    print("Invlaid string to be removed")
    

