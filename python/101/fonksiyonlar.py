
###*** METHOD ***###

# list = [1,2,3]   # class ın içinde yer alır

# list.append(4)  # calss ın altında kullanılabilecek methodlar
# list.pop()



# print(type(list))
# print(list)

# myString = "HELLO"   # class ın içinde yer alır 

# print(myString.lower())  # class ın aldında yer alan methodlar
# print(type(myString))


###*** FONKSİYONLAR ***###

# def sayHello(name = "user"):
#     return "Hello " + name

# msg = sayHello("Selçuk")

# print(msg)

# def total(num1,num2):
#     return num1 + num2

# result= total(10,20)
# print(result)



# def yashesapla(doğumyılı):
#     return 2023 - doğumyılı          # değişken tanımladıktan sonra yapılacak işlem 

# ageSelçuk = yashesapla(2005)          # değişkenleri tanımlama 
# ageMert = yashesapla(2010)

# print(ageSelçuk , ageMert)


# def emekliligekaçyılkaldı(dogumyili, isim):
#     """
#     DOCSTRING: Dogum yiliniza gore emekliliginize kac yıl kaldı
#     INPUT: Dogum yili                                           ## FONKSİYON TANIMLA ARDINA YAPILACAK İŞLEMLERİ GİR EN SON FONKSİYONU ÇAĞIR.
#     OUTPUT: Hesaplanan yil bilgisi
#     """
#     yas = yashesapla(dogumyili)
#     emeklilik= 65 - yas

#     if emeklilik > 0:
#         print(f"emekliliğinize {emeklilik} yıl kaldı.")
#     else:
#         print("zaten emeklisiniz")
# emekliligekaçyılkaldı(1983, "Ali")

# print(help(emekliligekaçyılkaldı))


###*** FONKSİYON PARAMETRELERİ ***###

# def changeName(n):
#     n ='ada'
# name = 'yiğit'

# changeName(name)
# print(name)

# def change(n):
#     n[0]= "istanbul"

# sehirler = ["ankara", "izmir"]

# change(sehirler)
# print(sehirler)

# def add(a ,b, c = 0):     # eğer bazen iki bazen üç parametre kullanmak istersen c yi sıfara eşitle ve devam et
#     return sum((a,b,c))

# print(add(10,20))
# print(add(10,20,30))

# def add(*params):          # eğer birden fazla parameetre tanımlamak istersen fonksiyona *... değişkeni verirsen sum içinde hepsini toplar **** tuple liste için tek yıldız yazman gerekiyor
#     print(params)
#     return sum((params))

# print(add(10,20,40,40,52,4,805,0,4))

# def displayUser(**args):          # dictionary liste için iki yıldız ile tanımla
#     print(type(args))
#     for key, value in args.items():
#         print("{} is {}".format(key,value))

# displayUser(name ='Selçuk', age= 18, city= 'çorum') 
# displayUser(name ='Mert', age= 13, city= 'trabzon', email= 'mert.com') 

# def myfunc(a, b, *args, **kwargs):   # *args valueleri üstlenir **kwargs ditionary i üslenir
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# myfunc(10,20,30,40,50, key1 = 'value 1', key2 = 'value 2')


###*** FONKSİYONLAR UYGULAMA ***###

# göderilen bir kelimeyi belirtilen kez ekranda gösteren fonk. yazın

# def yazdir(kelime, adet):
#     print(kelime*adet)

# yazdir("merhaba\n", 10)

# kendine göderilen sınırsız sayıdaki bir parametreyi bir listeye çeviren fonk. yazın

# def liste(*params):
#     list = []
    
#     for param in params:
#             list.append(param)
       
#     return list

# result = liste(10,20,30,"merhaba")
# print(result)
    



# gönderilen iki sayı arasında ki tüm asal sayıları bulunuz



# def asalsayilaribul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                     if (sayi % i == 0):
#                         break
#                     else:
#                         print(sayi)

# sayi1 = int(input("sayı 1 :  "))
# sayi2 = int(input("sayı 2:  "))

# asalsayilaribul(sayi1, sayi2)

# kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde dödür

# def tambölenleribul(sayi):
#     tambölenler=[]

#     for i in range(2, sayi):
#         if (sayi % i == 0):
#             tambölenler.append(i)
#     return tambölenler

# print(tambölenleribul(60))


#####*** LAMBDA EXPRESSİONS , MAP VE FİLTER ***####

#def square(num): return num ** 2
#quare = lambda num:num ** 2
#numbers = [1,3,5,9]

#result = list(map(lambda num:num ** 2  ,numbers))   #eğer değişkende tanımlarsan list ile almalısın 
#result = list(map(square,numbers))
#for item in map(square, numbers):     
#    print(item)

#print(result)

###3# lambda bir işlemi yaparken sürekli değişicekse belirsiz bir işlem varsa lambda ile yapıp sadece değişkenlerini tanımlarsın
##### map verilen bir fonksiyonun sıralı nesnenin her elemanına tek tek uygulayarak bir liste yaratır
##### Map fonksiyonunda liste içerisindeki her bir sayı fonksiyona gönderilip bir işlem görüyor ve geriye gönderiliyor ancak filter metodu ile geriye dönecek sayılara bir filtre uygulayabiliriz


#def check_even(num):return num%2 == 0

#check_even = lambda num: num%2==0
#numbers = [1,3,5,9,8,4]
#result= list(filter(check_even,numbers))  # veya (bu kısım def fonk varken kullanılır)
#result= list(filter(lambda num: num%2==0,numbers))  # veya ( def olmasada olur)
#result= list(filter(check_even,numbers))     # def olamasada olur ama chech_even i tanımla lambda ile
#result = check_even(numbers[4]) # check_even tanımlı olması gerekiyor
#print(result)

##### GLOBAL , LOCAL #####

# global scope
x= "global x"

def function():
    #local scope
    x = "local x"
    print(x)            # fonksiyonun altında ki print fonksiyonda tanımlı olan x i yazdırır 


function()
print(x)                # fonksiyonun dışında ki print fonksiyonla alakası olmayan x değişkenini yazdırır


######################################3333
#global
name = 'Selçuk'

def changeName(new_name):
    #local
    name = new_name
    print(name)

changeName('Mert')
print(name)

#######################3############

name = "global string"

def greeting():
    #name ="selçuk"

    def hello():
        #name = "mert"
        print("hello "+ name)

    hello()

greeting()

#######################3############

x = 50 
def test():
    global x             # fonksiyonun dışanda tanımlanan değeri artık fonksiyon altında ne girilmişse ona değiştiriyor
    print(f"x : {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)
































