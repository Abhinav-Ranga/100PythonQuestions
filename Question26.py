

def factorial(n):
    fact = 1

    for i in range(1,n):
        fact  = fact*i

        
    return print(fact)

n = int(input('enter the number: '))
factorial(n)