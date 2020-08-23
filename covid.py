#Task : Estimating the risk of death from coronavirus. Write a program that;
#Takes "Yes" or "No" from the user as an answer to the following questions :
#Are you a cigarette addict older than 75 years old? Variable → age
#Do you have a severe chronic disease? Variable → chronic
#Is your immune system too weak? Variable → immune
#Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).

age = input("Please Enter Yes or No: Are you a cigarette addict older than 75 years old?")
chronic = input("Please Enter Yes or No: Do you have a severe chronic disease?")
immune = input("Please Enter Yes or No: Is your immune system too weak?")
if age.capitalize() == "Yes":
    age = True
else:
    age = False
if chronic.capitalize() == "Yes":
    chronic = True
else:
    chronic = False
if immune.capitalize() == "Yes":
    immune = True
else:
    immune = False
risk = bool(age or chronic or immune)
if risk:
    print("You are in risky group")
else:
    print("You are not in risky group")