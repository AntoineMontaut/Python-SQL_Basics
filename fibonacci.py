'''
Calculates the first 100 Fibonacci numbers starting at 0 and 1
'''

fib_num = raw_input("Please enter an integer: ")

try:
    fib_num = int(fib_num)
except:
    print("Your input must be an integer!")

def fib(n):
    '''
    recursive funtion to get Fibonacci numbers starting at 0 and 1
    '''
    def fib_print(num):
        if num % 3 == 0 and num % 5 == 0:
            print("{0} FizzBuzz!".format(num))
        elif num % 3 == 0:
            print("{0} Fizz!".format(num))
        elif num % 5 == 0:
            print("{0} Buzz!".format(num))
        else:
            print str(num)
    
    if n < 2:
        #fib_print(n)
        return n
    else:
        num  = fib(n - 2) + fib(n - 1)
        #fib_print(num)
        return num
 
print("Fibonacci number at n = {0} starting at 0 and 1 is: {1}".format\
(fib_num, fib(fib_num)))