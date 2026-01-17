a=int(input("Enter a:"))
b=int(input("Enter b:"))
r=int(input("Enter radius r:"))
x=int(input("Enter x:"))
y=int(input("Enter y:"))

d=((y-b)*(y-b))+((x-a)*(x-a))

if(d==r*r):
    print("Given point is on the circle")

elif(d<r*r):
    print("Given point is inside the circle")

else:
    print("Given point is outside the circle")
