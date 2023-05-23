#Make a variable to get the number you want to get factorial of
num = int(input("Enter the number you want factorial of : "))
fact = 1
#Loop to get the factorial of the number
for i in range (1,num+1):
    fact = fact*i
print("The factorial of",num,"is",fact)