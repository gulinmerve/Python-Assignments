a = int(input("bir sayı giriniz: "))
def faktoriyel(a):
    count = 1
    for i in range(a,0,-1):
        count *= i
    return count
print(faktoriyel(a))
#####
########
def faktoriyel(num):
    if num == 0: return 1
    elif num < 0: return "Please enter positive number"
    else: return num*faktoriyel(num-1)
print(faktoriyel(4))

###
def factorial(n):
	for i in range(1,n+1):
		n *= i
	return n
print(factorial(5))