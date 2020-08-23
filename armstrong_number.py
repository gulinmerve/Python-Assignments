number= input("Please write an integer:")
if ("." in list(number) or "," in list(number) or "-" in list(number) or number.isnumeric()==False):
    print ("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    i=0
    sum_num=0
    while i<len(number):
        sum_num +=(int(number[i]))**(len (number))
        i+=1
    if sum_num==int(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")