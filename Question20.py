n = int(input('enter the number: '))

n = n-n*10/100
n = n-n*5/100
n = n-n*3/100

if n >=500000 and n<=1000000 :
    n  = n - n*10/100
elif n>= 1100000 and n<= 2000000:
    n = n- n*20/100

elif n>2000000:
    n = n-n*30/100
else :
    n

print('this is ur inhand salary: ',n)

    