from datetime import datetime
name = (input("Enter name: "))
now = datetime.now()
month_now = now.strftime("%B")
day_now = now.strftime("%A")
print(month_now)
print(day_now)
print(name)
