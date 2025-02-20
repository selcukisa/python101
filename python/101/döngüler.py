######   FOR DÖNGÜSÜ   ######

# numbers = [1,2,3,4,5]

# for a in numbers:
#     print(a)        # print(a) yaerine print("hello") yazarsanda listedeki eleman kadar hello yazar

# names = ["çınar", "ali", "selçuk"]

# for name in names:
#     print(f"my name is {name}")

# name = "selçuk"

# for n in name:
#     print(n)       # string ifade ise elamanlarını tek tek yazar

# tuple = [(1,2),(1,3),(3,5),(5,7)]

# for a,b in tuple:
#     print(a,b)

# d = {"k1": 1,"k2": 2, "k3": 3}

# for key,value in d.items():
#     print(value)     # print in içine ne yazarsan orayı alırsın  

#****** FOR DÖNDÜSÜ UYGULAMA ******#

sayılar = [1,3,5,7,9,12,19,21]

#listedeki hangi sayılar 3 ün katıdır

# for sayı in sayılar:
#    if (sayı%3 ==0):
#       print(sayı)


#listedeki sayıların toplamı kaçtır

# toplam = 0
# for sayı in sayılar:
#     toplam +=  sayı
# print("toplam:" ,toplam)


#listedeki tek sayıların karesinin toplamını alınız
# toplam = 0
# for sayı in sayılar:
#     if (sayı%2 == 1):
#         toplam+= sayı ** 2
#         print(toplam)



# sehirler = ["kocaeli","istanbul", "ankara", "izmir","rize"]

#şehirlerden hangileri en fazla 5 karakterlidir

# for şehir in sehirler:
#     if (len(şehir) <= 5):
#         print(şehir)




# urunler = [
#     {"name": "samsung S6", "price": "3000"},
#     {"name": "samsung S7", "price": "4000"},
#     {"name": "samsung S8", "price": "5000"},
#     {"name": "samsung S9", "price": "6000"},
#     {"name": "samsung S10", "price": "7000"}
# ]

# ürünlerin fiyatları toplamı nedir
# toplam = 0
# for ürün in urunler:
#     fiyat = int(ürün["price"])
#     toplam += fiyat
# print("toplam:", toplam)


# fiyatı en fazla 5000 olan ürünleri gösteriniz

# for urun in urunler:
#     a = int(urun["price"])
#     if (a <= 5000):
#         print(urun["name"])



######*** WHİLE DÖGÜSÜ ***######

# x = 1

# while x <= 100:
#     if x%2==1:
#         print(f"sayı tek: {x}")
#     else:
#         print(f"sayı çift: {x}")
#     x += 1

# print("bitti...")


# name= '' #false değer not da true ye çevirir
# while not name.strip():    # boşluk ifadelerini silmek için .strip kullan
#     name = input("isminizi girin: ")

# print(f"merhaba, {name}")

###########******* WHİLE DÖNGÜSÜ UYGULAMA ###########********

# sayılar = [1,3,5,7,9,12,19,21]

# sayılar listesini while ile yazdır

# i = 0
# while (i < len(sayılar)):
#      print(sayılar[i])
#      i += 1


# başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdır

# baslangıc = int(input("başlangıç:  "))
# bitis = int(input("bitis:  "))


# i = baslangıc
# while i < bitis:
#     i += 1
#     if i % 2 ==1:
#         print(i)


# 1-100 arasındaki sayıları azalan şekilde yazdır

# i = 100

# while i > 0:
#     i -=1
#     print(i)



# kullanıcıdan alacağınız 5 değeri ekrana sıralı şekilde yazdırınız

# numbers = []

# i=0 

# while i<5:
#     sayı = int(input("sayı:  "))
#     numbers.append(sayı)
#     i += 1
# numbers.sort()

# print(numbers)

# kullanıcıdan alacağınız sınırsız ürün bilgisini ürünlr listesi içinde saklayınız
# **ürün sayısını kullanıcıya sorun
# **dictionary listesi yapınız(name ,price) şeklinde olsun
# **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyniz

# urunler= []

# adet = int(input("kaç ürün eklemek istiyorsunuz:  "))
# i=0

# while(i<adet):
#     name = input("ürün ismi:  ")
#     price = input("ürün fiyatı:  ")
#     urunler.append({
#         "name": name,
#         "price": price
#     })
#     i += 1

# for urun in urunler:
#     print(f"ürün adı {urun['name']}, ürün fiyatı: {urun['price']}")


#######*** BREAK ve CONTİNUE komutları ***#######

#name = "sadık turan"

# # for letter in name:
# #     if letter == "ı":
# #         break      # belirtilene geldiğnde çalışmayı durdurur
# #     print(letter)


# for letter in name:
#     if letter == "ı":
#         continue     # belirtileni gördüğünde sadece onu yazdırmaz
#     print(letter)

#x = 0

# while x < 5:
#     if x == 2:
#         break    # 2 ile karşılaştığında döngüyü durdur der.
#     print(x)
#     x += 1

# while x < 5:
#     x += 1
#     if x == 2:
#         continue  
#     print(x)
    
 #x+=1 in önde olmasının sebebi 2 yi gördüğü anda 
          # durur ama eğer arttırma işlemini önceye alırsak
                    # arttırır ve sadece 2 yi yazmaz

# 1-100 e kadar tek sayıların toplamı
# x = 0
# result = 0

# while x <= 100:
#     x +=1
#     if x % 2 == 0:
#         continue
#     result += x
    
# print(f"toplam: {result}")



##***  DÖNGÜ METODLARI  range() , zip() , enumerate()  ***##

#**** RANGE ****

# for item in range(50,100,10):  # 50 den başla 100 e kadar 10 10 git
#     print(item)

# print(list(range(5,100,10)))  # for la alakalı değil



#**** ENUMERATE  

# greeting = "HELLO"

# for item in enumerate(greeting):
#     print(item)
#     #print(f"index: {index} letter: {letter}")



#**** ZİP  => listeleri eşleştiriyor

# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]

# zip(list1,list2)
# print(list(zip(list1,list2)))

# for item in zip(list1,list2):
#     print(item)



###*** LİST COMPRESENSİONS => LİSTE OLARAK ALGILAMA

# numbers = []
# for x in range(10):
#     numbers.append(x)

# print(numbers)
# ###############################
# numbers = [x for x in range(10)]
# print(numbers)
# ###########################
# for x in range(10):
#     print(x**2)
# #######################
# numbers = [x**2 for x in range(10)]
# print(numbers)
# #######################33
# numbers = [x*x for x in range(10) if x%3==0]
# print(numbers)
# ##############################################
# myString = "Hello"
# myList = []

# for letter in myString:
#     myList.append(letter)

# print(myList)
# #######################################

# myList = [letter for letter in myString]
# print(myList)
# ########################################

# years = [1983, 1999, 2008, 1956, 1986]
# ages = [2019-year for year in years]

# print(ages)
# #####################################

#results = [x if x%2==0  else "tek" for x in range(1,10)]
#print(results)


# result = []

# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)
# ###################################

# numbers = [(x,y) for x in range(3) for y in range(3)]
# print(numbers)
#############################################
numbers = [(x,y) for x in range(1,10) for y in range(1,10) if y%2==1 if x%2==0]
print(numbers)                               #x ler çift y ler tek şekilde ikili oluştur





