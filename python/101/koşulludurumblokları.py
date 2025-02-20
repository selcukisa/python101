###    İF  / /   ELSE  BLOKLARI

# username= "selcukisa"
# password = "1453"

# isLoggedin = (username == "selcukisa") and (password == "1453") 

# if isLoggedin:
#     print("hoş geldin")

# VEYA DEĞİŞKEN TANIMLAMAK YERİNE DİREK İF İN YANINA YAZABİLİRSİN
input("aa: ")
username= "selcukisa"
password = "1453"

if (username == "selcukisa"):
     if(password == "1453"):
         print("hoş geldin")
     else:
         print("parola yanlış")

else:
     print("username yanlış")



###     İF-ELİF  /  ELSE  BLOKLARI
# x = int(input("x:  "))
# y = int(input("y:  "))

# if x > y:
#     print("x y den büyük")
# elif x==y:
#     print("x y ye eşit")
# else:
#     print("y x den büyük")


# num = int(input("sayı:  "))

# if num > 0:
#     print("pozitif sayı")
# elif num < 0:
#     print("negatif sayı")
# else:
#     print("sayı sıfır")


# 1)kullanıcıdan isim, yaş ve eğitim bilgilerini alıp
# ehliyet alabilme durumunu kontrol ediniz.ehliyet alabilme 
# koşulu en az 18 yaş ve eğitim durumu lise ya da üniversite 
# olmalıdır.

# name = input("isim:  ")
# age = int(input("yaş:  "))
# education = input("sınıf:  ")
# if (age >= 18): 
#     if (education=="lise" or education=="üniversite"):
#         print(f"{name} ehliyet alabilir")
#     else:
#         print(f"{name} ehilet alamaz eğitim durumu yetersiz")
# else:
#     print(f"{name} ehliyet alamaz yaşı tutmuyor")


# 2)bir öğrencinin iki yazılı bir sözlü notunu alıp hesaplanan
# ortalamaya göre not aralığına denk gelen not bilgisinş yazdır
# 0-24 = 0
# 25-44 =1
# 45-54 =2
# 55-69 = 3
# 70-84 = 4
# 85-100 = 5

# yazılı1 = float(input("y1:  "))
# yazılı2 = float(input("y2:  "))
# sözlü = float(input("s:  "))
# ortalama = int(yazılı1 + yazılı2 + sözlü)/3
# if ortalama >= 0 and ortalama <=24:
#     print(f"ortalamanız: {ortalama} notunuz: 0")
# elif ortalama >=25 and ortalama <=44:
#     print(f"ortalamanız: {ortalama} notunuz: 1")
# elif ortalama >=45 and ortalama <=54:
#     print(f"ortalamanız: {ortalama} notunuz: 2")
# elif ortalama >=55 and ortalama <=69:
#     print(f"ortalamanız: {ortalama} notunuz: 3")
# elif ortalama >=70 and ortalama <=84:
#     print(f"ortalamanız: {ortalama} notunuz: 4")
# elif ortalama >=85 and ortalama <=100:
#     print(f"ortalamanız: {ortalama} notunuz: 5")
# else:
#     print("YANLIŞ BİLGİ GİRDİNİZ")

# 3) trafiğe çıkış tarihi alınan bir aracın servis zamanını
# aşşağıdaki bilgilere göre hesaplayınız 
# 1. bakım = 1. yıl
# 2. bakım = 2. uıl
# 3. bakım = 3. yıl
# **süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız 
# ***datatime modülünü kullanmanız gerekiyor
# (şimdi) - (2018/8/1) => gün
# import datetime
# tarih = input("aracınız hangi gün trafiğe çıktı (2019/8/9):  ")
# tarih = tarih.split("/")
# # print(tarih[0])
# # print(tarih[1])
# # print(tarih[2])
# trafiğeçıkış= datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafiğeçıkış
# days = fark.days
# print(days)

# if days <=365:
#     print("1. servis aralığı")
# elif days > 365 and days<= 365*2:
#     print("2. servis aralığı")
# elif days > 365*2 and days <= 365*3:
#     print("3. servis aralığı")
# else:
#     print("hatalı bilgi girdiniz")




























