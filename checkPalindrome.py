#Function to check palindrome
def palindrome(n):
    #Getting a string because it can be reversed easily
    l = str(n)
    #Reversing the string to get opposite word
    z = l[: : -1]
    if(n == z):
        print('It is a palindrome')
    else:
        print('It is not a palindrome')

palindrome("123404321")