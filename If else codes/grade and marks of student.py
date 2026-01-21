m=int(input("Enter marks of maths:")
p=int(input("Enter marks of physics:")
c=int(input("Enter marks of chemistry:")

t=m+p+c
print("total marks are:",t)      

a=t/3
print("average marks are:",a)

if(a<35 or m<=39 or p<=39 or c<=39):
    print("Candidate has failed")

else:
    print("Candidate has passed")

print("Grade in Maths:")

if(m>=0 and m<=39):
    print("F")

elif(m>=40 and m<=44):
    print("P")

elif(m>=45 and m<=49):
    print("C")

elif(m>=50 and m<=54):
    print("B")

elif(m>=55 and m<=59):
    print("B+")

elif(m>=60 and m<=69):
    print("A")

elif(m>=70 and m<=79):
    print("A+")

elif(m>=80 and m<=100):
    print("O")

print("Grade in Physics:")    

if(p>=0 and p<=39):
    print("F")

elif(p>=40 and p<=44):
    print("P")

elif(p>=45 and p<=49):
    print("C")

elif(p>=50 and p<=54):
    print("B")

elif(p<=55 and p<=59):
    print("B+")

elif(p>=60 and p<=69):
    print("A")

elif(p>=70 and p<=79):
    print("A+")

elif(p>=80 and p<=100):
    print("O")

print("Grade in Chemistry:")    

if(c>=0 and c<=39):
    print("F")

elif(c>=40 and c<=44):
    print("P")

elif(c>=45 and c<=49):
    print("C")

elif(c<=50 and c<=54):
    print("B")

elif(c>=55 and c<=59):
    print("B+")

elif(c>=60 and c<=69):
    print("A")

elif(c>=70 and c<=79):
    print("A+")

elif(c>=80 and c<=100):
    print("O")

    

    
