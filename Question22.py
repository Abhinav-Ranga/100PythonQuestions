heads = int(input("total no of heads: "))
legs = int(input("total no of legs: "))


# assume if all are chicken 
assumelegs = heads*2

extraleg = legs-assumelegs

dogs = extraleg//2



chicken = heads-dogs 
print("no of dogs: ",dogs)
print("no of chicken : ", chicken)


