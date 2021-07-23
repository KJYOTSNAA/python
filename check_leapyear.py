year=int(input("enter the year:"))
if year%400==0 and year%4==0:
    print(year,"is aleap year")
else:
    print(year,"is not  a leap year")
