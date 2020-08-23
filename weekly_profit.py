# Assignment-1 (Weekly Profit)
# 
# 💡Objective:
# To improve your arithmetic algorithm and problem solving skills.
# Write a Python code on your Playground and submit your code (answer) as a plain text.
# Problem : If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, 
# how much would your $ 1000 reach at the end of the 7th day?

x = 1000 * 1.07 ** 7
print("$", x) # This is the First Answer

currency_amount = 1000
total_day = 7
profit_rate = 1.07
total_amount =  currency_amount * profit_rate ** total_day
print("$", total_amount) # This is the Second Answer

x = 1000 * 1.07 ** 7
print("$", int(x)) # This is Third Answer

currency_amount = int(input("Insert the amount of currency: "))
profit = float(input("Insert the profit rate: "))
day = int(input("Insert the day: "))
total_amount =  currency_amount * (1 + profit) ** day
print("Your money will be reached : $", int(total_amount)) # This is the fourth answer