# Your Life in 90 Years 
age = input("What is your current age?")

#Calculate your Years, Months, Weeks, Days

new_age = 90 - int(age)

days = new_age * 365
weeks = new_age * 52
months = new_age * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
