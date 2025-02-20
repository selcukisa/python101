# error => hata
# Error
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0)=> ZeroDivisionError

# error handling => hata yönetimi
# try:
#     x= int(input('x:  '))
#     y= int(input('y:  '))
#     print(x/y)
# except (ZeroDivisionError,ValueError):
#     print('yanlış biiligi giridiniz')

# while True:
#     try:
#         x= int(input('x:  '))
#         y= int(input('y:  '))
#         print(x/y)
#     except Exception as ex:
#         print('yanlış bilgi girdiniz', ex)
#     else:
#         break
#     finally:
#         print('try except sonlandı')

# x= 10

# if x > 5:
#     raise Exception('x 5 den büyük değer alamaz')

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception('parola en az 8 karakterli olmalıdır')
#     elif not re.search('[a-z]',psw):
#         raise Exception('parola küçük harf içermelidir')
#     elif not re.search('[A-Z]', psw):
#         raise Exception('parola büyük harf içermelidir')
#     elif not re.search('[0-9]',psw):
#         raise Exception('parola rakam içermelidir')
#     else:
#         print('GEÇERLİ PAROLA ')
    
# password= "12345678aA"
# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else: 
#     print('geçerli parola: else')
# finally:
#     print('validation tamamlandı')

# class Person:
#     def __init__(self,name,year):
#         if len(name) > 10:
#             raise Exception('name alanı fazla karakter içeriyor')
#         else: 
#             self.name = name
# p = Person('aliiii', 1989)

# UYGULAMA 
# liste= ["1","2","5a","10b","abc","10","20","50"]   
    
#1: liste elemanları içinde sayısal değerleri bulunuz

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue 


#2: kullanıcı "q" değerini girmedikçe aldığınız her input sayı
#olduğundan emin olunuz aksi takdirde hata mesaji yazınız 

# while True:
#     sayi = input('sayı:  ')
#     if sayi == 'q':
#         break

#     try:
#         result = float(sayi)
#         print('girdiğiniz sayı geçerli: ' ,result)
#     except:
#         print('geçersiz sayı')
#         continue



#3: girilen parola içinde türkçe karakter hatası veriniz 

# def checkPassword(parola):
#     turkce_karakter = "ğşıİöçü"
    
#     for i in parola:
#         if i in turkce_karakter:
#             raise TypeError('parola türkçe karakter içeremez')
#         else:
#             pass
#     print('geçerli parola')
# parola = input('paraola:  ')
# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)

#4: faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajı veriniz


def faktoriyel(x):
    x= int(x)
    if x<0:
        raise ValueError('Negatif değer alamaz')
    result = 1
    for i in range(1, x+1):
        result *=i
        return result
for x in [5,10,20,-3,'10a']:   
    try:
        y= faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
print(y)




