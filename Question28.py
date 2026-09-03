def primechecker(n):

    if n<2:
        print('this is not a prime number')
        return False

    if n == 2:
        print('this is a prime number')    
        return True


    for i in range(2,n):
        if n%i == 0:
                print('this is not a prime number')
                return False
    print('this is a prime number')       

n = int(input('enter the number: '))

primechecker(n)