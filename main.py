from datetime import date
import datetime


def age(birthdate):
    # Get today's object
    today = date.today()
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
    year_difference = today.year - birthdate.year
    age = year_difference - one_or_zero
    return age


#thisHour = datetime.datetime.now()
#print(thisHour.hour,":",thisHour.minute,":",thisHour.second," ",thisHour.year,"-",thisHour.month,"-",thisHour.day)


firstName = str(input("What is your first name? "))
lastName = str(input("What is your last name? "))
birthYear = int(input("What is your year of birth? "))
birthMonth = int(input("What is the month of birth? "))
birthDay = int(input("What is the day of birth? "))

ageCalc = age(date(birthYear, birthMonth, birthDay))
txt = "Hello, my name is {fn} {ln}.  I am currently {a} years old.".format(fn = firstName, ln = lastName, a = ageCalc)

print(txt)

