s1={'Math','Physics','Chemistry'}
s2={'Physics','Biology','Math'}

s3=s1&s2
print("Common subjects:",s3)

s4=s1-s2
print("Subjects taken by only first student:",s4)

s5=s2-s1
print("Subjects taken by only second student:",s5)

s6=s4|s5
print("Toal unique subjects:",s6)
