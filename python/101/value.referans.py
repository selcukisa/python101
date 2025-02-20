# value types => string, number (birbirini etkilemez[farklı adreslerdedirler])
x= 5
y = 25
x=y
y=10
print(x,y)

#referance types => list  (birbirini etkiler[aynı adrese gider])

a =["apple","banana"]
b =["apple","banana"]
a=b

b[0] = "grape"

print(a,b)








