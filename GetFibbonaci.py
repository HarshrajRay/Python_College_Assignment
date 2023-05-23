#Function to get fibbonaci series
def fibo(n):
    if n <= 1:
       return n
    else:
       return(fibo(n-1) + fibo(n-2))

#Get the number of terms you want fibbonaci series upto
nterms = int(input("Enter the number of terms you want fibonacci upto :"))
#To check if the number of terms is greater than 0 
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   #A loop to get fibbonaci series startig fron zero
   for i in range(nterms):
       print(fibo(i))