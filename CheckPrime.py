# Get the number you want to check wheter it is prime or not
num = int(input("Enter the number you want to check for prime "))
#Set a check for prime number
prime_check = False
#Get the half of the number because the minimum factor for a number is 2
half = int(num/2)
if num == 1:
    print("The number is not prime")
elif num > 1:
    #Loop to check if the number is divisible by any number other than 1 amd itself 
    for i in range (2,half):
        if (num % i) == 0:
            prime_check = True
            break
    if prime_check:
        print("The number is not prime")
    else:
        print("The number is prime")
else:
    print("Please enter a positive number")