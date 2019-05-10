def is_leap(year):

    if year%4==0 or year%100!=0 or year%400==0:
        print(year,"is leap year")
    elif year%4!=0:
        print(year,"is not a leap year")


year = int(input("enter the year"))
is_leap(year)