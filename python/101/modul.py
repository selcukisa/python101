#YONTEM 1
#import math
#import math as islem

# value = dir(math)
# value = help(math)
# value = help(math.factorial)
# value = math.sqrt(49)
# value = math.factorial(5)


#value = islem.factorial(5)

#YÖNTEM 2

#from math import *

#def sqrt(x):              # fonksiyon veya kütüphane hangisi sonsa onu algılar
 #   print('x: '+ str(x))


#from math import factorial , sqrt    #math kütüphanesinden faktöriyel ve sqrt işlemlerini al

#value = factorial(5)
#value = sqrt(9)

#print(value)


import random

#result = dir(random)
#result = help(random)
result = random.random() #0.0 - 1.0 arasında
result = random.random() * 100
result = random.uniform(1,10)
result = random.randint(1,100)

names= ["ali", "yağmur", "emir", "ahmet"]
result = names[random.randint(0,len(names)-1)]
result= random.choice(names)

liste = list(range(10))
random.shuffle(liste)
result= liste

liste= range(100)
result = random.sample(liste,3)
result = random.sample(names, 2)


print(result)






















