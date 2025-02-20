# x = 5
# hak= 5
# devam = "e"
# # result = 5 < x < 10


# # and
 
# # True, true  => true
# # True, false  => false



# result= (x > 5) and (x < 10)   
# result= (hak > 0) and (devam == "e")



# # or 

# #true, false  => true
# #true, true  => true
# #false, false  => false

# result= (x > 0) or (x % 2 == 0)



# not


# result= not(x > 0)


# x, 5-10 arasında olan bir çift sayımı ?

# result= ((5<x) or (x<10)) and (x%2==0) 


# print(result)


###########MANTIKSAL OPERATÖRLER UYGULAMA##########

# girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

# x = float(input("sayı:  "))
# if (0<x) and (x<100):
#     print("sayı 0-100 arasında.")
# else:
#     print("sayı 0-100 arasında değil")



# girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

# x= int(input("sayı:  "))
# if (x >0) :
#       if (x%2==0):
#             print("sayı pozitif ve çifttir")
#       else:
#             print("sayı sadece pozitiftir")
# else:
#       print("sayı sadece çifttir")


# email ve parola bilgileri ile giriş kontrolü yapınız 
# girilenEmail = input("email:  ")
# girilenPassword = input("parola:  ")
# email = "email@selcuk.com"
# password= "1453"
# if girilenEmail == email:
#       if girilenPassword== password:
#             if not ((girilenEmail == email) and (girilenPassword== password)):
#                   print("hoş geldiniz")
#             else:
#                   print("şifreyi yanlış girdiniz")
#       else:
#             print("email yanlış girdiniz")


      




# girilen 3 sayıyı büyüklük olarak karşılaştırınız
# x = int(input("s1:  "))
# y = int(input("s2:  "))
# z = int(input("s3:  "))

# if (x > y) and  (x > z):
#       print("x en büyük sayıdır")

# elif (y > x) and  (y > z):     
#       print("y en büyük sayıdır")

# elif (z > y) and  (z > x):
#       print("z en büyük sayıdır")


# kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız 

# vize1 = int(input("v1:  "))
# vize2 = int(input("v2:  "))
# final = int(input("f:  "))
# ortalama = (((vize1+vize2)/2) * 0.6 + (final * 0.4))

# a) ortalama 50 olsa bile final notu en az 50 olmalıdır

# if (ortalama >= 50):
#     if (final >= 50):
#             print("dersi geçtiniz")
#     elif (ortalama >= 50) and (final < 50):
#           print("ortalamanız geçiyor fakat final notunuz yetersiz")
# elif (ortalama < 50) and (final >= 50):
#       print("final notunuz yeterli fakat ortalamanız yetersiz")
# else:
#       print("dersi geçemediniz")

#       b) finalden 70 aldığında ortalamanın önemi olmasın

# if (final >= 70):
#     print("SINAVI GEÇTİNİZ")
# else:
#     print("SINAVI GEÇEMEDİNİZ")




# kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız 
#       formül: (kilo/boy uzunluğunun karesi)
#       aşağıdaki tabloya göre kişi hangi guruba girmeltedir
#       0-18.4 = zayıf
#       18.5-24.9 = normal
#       25.0-29.9 = fazla kilolu
#       30.0-34.9 = şişman(obez)


isim = input("kişinin adı:  ")
kilo = float(input("kilo:  "))
boy = float(input("boy:  "))
x = (kilo/(boy**2))


if (x>=0 and x<=18.4 ):
    print(f"{isim} zayıfsınzı")
elif (x>=18.5 and x<=24.94):
 print(f"{isim} kilonuz normal")
elif (x>=25.0 and x<=29.9):
    print(f"{isim} fazla kilolusunzu")
elif (x>=30.0 and x<=34.9):
    print(f"{isim} obezsiniz")
elif (x>=35 and x<=50):
    print("git kilo ver {isim}")
else:
    print("hatalı bilgi girdiniz")










