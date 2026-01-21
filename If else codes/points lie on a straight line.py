a=int(input("Enter x1:"))
b=int(input("Enter y1:"))
c=int(input("Enter x2:"))
d=int(input("Enter y2:"))
e=int(input("Enter x3:"))
f=int(input("Enter y3:"))

m=(d-b)/(c-a)

n=(f-d)/(e-c)

o=(f-b)/(e-a)

if(m==n and n==o):
    print("Given points lie on a straight line")

else:
    print("Given points do not lie on a straight line")
