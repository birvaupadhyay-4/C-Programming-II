d1={'100','101','102','105'}
d2={'101','103','104','105'}

a=d1&d2
print("Visitors who visited both the days:",a)

b=d1^d2
print("Visitors who visied only one of the days:",b)

c=d1|d2
print("Total unique visitors:",c)

