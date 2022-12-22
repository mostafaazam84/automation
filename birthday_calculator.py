from datetime import datetime
 



now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

byear = int(input("Enter The Brith Year : "))
bmonth = int(input("Enter The Brith Month In Number"))
bday = int(input("Enter The Brith Day In Number"))


year =int(year)
month = int(month)
day = int(day)

x = year - byear
y = month - bmonth
z = day - bday



print (f"Your age Is ===> {x} Years and {y} month and {z} Day")



