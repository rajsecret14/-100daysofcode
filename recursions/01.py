# what is recursions ?
# factorial = n * factorial (n-1)
def factorial (n):
    if (n==0 or n==1):
        return 1
    else :
        return n * factorial (n-1) #function ke ander function
print (factorial(3))