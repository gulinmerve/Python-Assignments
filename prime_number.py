num = int(input("Please enter a number: "))
# If given number is greater than 1 
if num > 1: 
      
   for i in range(2, num): 
        
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 