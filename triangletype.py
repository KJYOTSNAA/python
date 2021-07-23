s1=int(input("enter side1 value:"))
s2=int(input("enter side2 value:"))
s3=int(input("enter side3 value:"))
if s1==s2==s3:
    print("it is a equilaterl triangle ")
elif s1==s2 or s2==s3 or s3==s1:
    print("it is a isoscalent triangle")
else:
    print("it is a scalene triangle")
