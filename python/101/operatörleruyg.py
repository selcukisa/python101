# "=="   => eşitmi sorusunu sorar
# "!="   => eşit değilmi sorusunu sorar
# "<,>,>=,<=" => büyük mü küçük mü büyük eşit mi büyük küçük mü sorusunu sorar

# 1-girilen iki sayıdan hangisi büyüktür
# a= int(input("a:  "))
# b= int(input("b:  "))
# result= (a>b)
# print(f"a:  {a} b:  {b} den büyüktür: {result}")


# 2-kullanıcıdan 2 vise (%60) ve 2 final (%40) notunu alıp ortalama hesaplayınız 
# eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazıdırınız

# vize1= int(input("v1:  "))
# vize2= int(input("v2:  "))
# final= int(input("f:  "))
# ortalama = ((vize1+vize2) / 2 * 0.6) + (final * 0.4)

# print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama >= 50}")



# 3-girilen bir sayının tekmi çift mi olduğunu yazdırınız 

# sayı = int(input("sayı:  "))
# tekçift=(sayı % 2 == 0)
# print(f"girilen sayı çift olma durumu: {tekçift}")



# 4-girilen bir sayının negatif mi pozitifmi olduğunu yazdırınız

# sayı = int(input("sayı:  "))
# negpoz = (sayı > 0 )
# print(f"girilen sayı pozitif mi: {negpoz}")



# 5-parola ve gmail bilgisini isteyip doğruluğunu kontrol ediniz 
gmail = "selcuk@gmail.com"
password= 1453
girilenGmail = input("gmail:  ")
girilenPassword= input("parola:  ")
isGmail = gmail == girilenGmail
isPassword= password== girilenPassword
print(f"gmail bilgisi doğrumu: {isGmail} ve parola doğrumu: {isPassword}")
























