x = int(input('Enter the number: '))
y = int(input('Enter the number: '))

original = abs(y)

res = 0

for i in range(original):
    res += x

if  y <0:
    res = -res    


print(res)
