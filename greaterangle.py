a1=int(input("enter angle1 value:"))
a2=int(input("enter angle2 value:"))
a3=int(input("enter angle3 value:"))

if a1>a2 and a1>a3:
    print(a1,"angle1 is greater")
elif a2>a1 and a2>a3:
    print(a2,"angle2 is greater")
else:
    print(a3,"angle3 is greater")
