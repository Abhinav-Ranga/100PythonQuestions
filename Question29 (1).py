def armschecker():

    for i in range(100,1001):
        n = len(str(i))
        a = i
        res = 0

        while a!= 0:
            b = a%10
            res = res +b**n
            a = a//10

        if res == i:
            print(i)    
        else:
            continue

armschecker()