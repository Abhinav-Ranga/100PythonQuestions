n = int(input('enter the number: '))
a = n
sum = 0

while a<1000 or a>9999:
    a = int(input('write correct output: '))


nl = len(str(n))

while a != 0:
    s = a%10
    sum += s**nl
    a = a// 10

if sum == n :
    print('this is a narcicist number: ')
else : 
    print('this is not a narcicist number: ')
    