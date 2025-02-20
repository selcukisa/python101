# x= 5
# y=10
# z=15

# x, y, z= 5, 10, 15

# # x, y=y, x

# x += 5        # x = x + 5
# x -= 5        # x = x - 5
# x *= 5        # x = x * 5
# x /= 5        # x = x / 5 
# x **= 5       # x = ** 5 

# x *= z        # x = x * z





# # print(x, y, z)

# values = 1, 2, 3
# print(values)
# print(type(values))

# x, y, z = values

# print(x, y, z)



                 # bütün elemanların eşleşmesi gerekiyor yoksa hata verir
                 # values = 1, 2, 3, 4, 5
                 # x, y, z = values
                 # => bu şekilde eşleştirmez ama x, y, *z = values yaparsak 
                 #   1,2,[3,4,5] yapar ve z ye liste verir.
                 # print(x, y, z[0]) da z nin listesinin 0.indexteki elemanını verir.


##########UYGULAMA#########
x, y, z = 2, 5, 10

numbers= 1, 5, 7, 10, 6

# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# sayı1= int(input("s1:  "))
# sayı2= int(input("s2:  "))

# result= (sayı1*sayı2) - (x+y+z)
# print(result)


# 2- y nin x e kalansız bölümü

# result= y//x
# print(result)




# 3- (x,y,z) toplamının mod 3 ü nedir

# result= (x+y+z) % 3
# print(result)



# 4- y nin x. kuvvetini hesaplayınız 

# result= y**x
# print(result)


# 5- x, *y, z = numbers işlemine göre z nin küpü kaçtır
# numbers= 1, 5, 7, 10, 6
# x, *y, z = numbers
# print(z**3)





# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı

# numbers= 1, 5, 7, 10, 6
# x, *y, z = numbers

# result = y[0]+y[1]+y[2]
# print(result)





print(90/(1.90**2))




















