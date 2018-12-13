import re

pattern = r"P[A-Z]{3}[A-Z]+\<\<[A-Z]+\<[A-Z]+"

passport = input("please enter passport number")

if len(passport) == 42 and re.search(pattern, passport):
    print("Passport is valid")
else:
    print("not vaild")