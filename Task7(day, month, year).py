weeks = int(input("Enter amount weeks: "))
months = int(input("Enter amount months: "))
years = int(input("Enter amount years: "))
print(f"all days: {(weeks * 7) + (months * 30) + (years * 12 * 30)}")