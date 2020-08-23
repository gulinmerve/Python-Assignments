num = int(input("Please enter a number: "))

count = 0
for i in range(2, num):
    if not ((i % i == 0) and (i % 1 == 0) and (i > 1)): count += 1
    else:
        print(num.append(i))