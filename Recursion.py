### Find summation from 1 to n  
#  Recursive formula:  $sum(n) = n + sum(n-1)$.  
# Base $sum(1) = 1$. 
def sum_recursion(n:int):
    #Base
    if n ==1:
        return 1
    #Recursive case
    else:
        return n+ sum_recursion(n-1)
        
print('sum(1) = ', sum_recursion(1))
print('sum(5) = ', sum_recursion(5))


### Find products from 1 to n (n factorial)  
# Recursive formula: $n!=n*(n-1)!$.    
# Base:$ 1! =1$.  
# (Remember $0!=1$.)


def factorial_recursion(n:int):
    #Base
    if n==0 or n==1:
        return 1
    #Recursive case
    else:
        return n*factorial_recursion(n-1)

print('0! = ', factorial_recursion(0))
print('1! = ', factorial_recursion(1))
print('5! = ', factorial_recursion(5))


### Find $n^{th}$ Fibonacci number
# Recursive formula: $F(n) = F(n-1) + F(n-2)$.  
# Base: $F(0) = 0, F(1) = 1.$  

def Fibonacci_recursion(nth: int):
    #Base
    if nth == 0:
        return 0
    elif nth ==1:
        return 1
    #Recursive case
    else:
        return Fibonacci_recursion(nth-1)+Fibonacci_recursion(nth-2)

print('F(0) = ', Fibonacci_recursion(0))
print('F(1) = ', Fibonacci_recursion(1))
print('F(2) = ', Fibonacci_recursion(2))
print('F(10)= ', Fibonacci_recursion(10))