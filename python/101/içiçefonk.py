# def greeting(name):
#     print("hello", name)

# print(greeting("ali"))
# print(greeting)

# sayHello= greeting

# print(sayHello)
# print(greeting)

# del sayHello
# print(greeting)


# def outer(num1):
#     def inner_increment(num1):
#         return num1 + 1
#     num2= inner_increment(num1)
#     print(num1,num2)
# outer(10)

# def factorial(number):
#     if not isinstance(number, int):
#         raise TypeError("number must be an intager")
    
#     if not number >= 0:
#         raise ValueError("number must be zero or positive")

#     def inner_factorial(number):
#         if number <=1:
#             return 1
#         return number * inner_factorial(number-1)
#     return inner_factorial(number)
# try:
#     print(factorial(5))
# except Exception as ex:
#     print(ex)


# def usalma(number):
#     def inner(power):
#         return number**power
    
#     return inner

# two = usalma(2) #2-3
# three = usalma(3) #3-4
# print(two(3)) 
# print(three(4))


# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolünün {1} sayfasına ulaşabilir".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
#     return inner
# user1 = yetki_sorgula("Product Edit")
# print(user1("user"))


# def islem(islem_adı):
#     def toplam(*args):
#         toplam=0
#         for i in args:
#             toplam += i
#         return toplam
    
#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim*= i
#         return carpim

#     if islem_adı == "toplama":
#         return toplam
#     else:
#         return carpma

# toplama = islem("toplama")
# print(toplama(1,3,5,7,8))

# carpma = islem("carpma")
# print(carpma(1,2,3,4,5))


# def toplama(a,b):
#     return a+b 
# def cikarma(a,b):
#     return a-b
# def carpam(a,b):
#     return a*b
# def bolme(a,b):
#     return a/b

# def islem(f1,f2,f3,f4, islem_adı):
#     if islem_adı == "toplama":
#         print(f1(2,3))
#     elif islem_adı== "cikarma":
#         print(f2(5,3))
#     elif islem_adı== "carpma":
#         print(f3(3,4))
#     elif islem_adı == "bolme":
#         print(f4(10,2))
#     else:
#         print("geçersiz işlem")

# islem(toplama,cikarma,carpam,bolme, "toplama")


## DECORATOR FONKSİYON ##











