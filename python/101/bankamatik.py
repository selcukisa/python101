
SelcukHesap = {
    'ad': "Selçuk",
    'hesapNO': '1',
    'bakiye': 3000,
    'ekHesap': 2000,
    'şifre': '5252'
}

AkifHesap = {
     'ad': "Akif",
     'hesapNO': '2',
     'bakiye' : 3000,
     'ek hesap': 2000,
     'şifre': '3131'
}

print("""


KTÜ BANKA HOŞ GELDİNİZ


""")

girilenHesapNO = input("HESAP NO GİRİNİZ:")
girilenŞifre = input("HESAP ŞİFRENİZİ GİRİNİZ: ")

onlinehesap= []

if girilenHesapNO==AkifHesap['hesapNO'] and girilenŞifre==AkifHesap['şifre']:
    print("AKİF HOŞ GELDİN")
    onlinehesap.append(AkifHesap['bakiye'])
elif girilenHesapNO== SelcukHesap['hesapNO'] and girilenŞifre== SelcukHesap['şifre']:
    print("SELÇUK HOŞ GELDİN")
    onlinehesap.append(SelcukHesap['bakiye'])
else:
    print("TEKRAR DENEYİNİZ")
print("""

SEÇMEK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ :
      
1 - ) PARA YATİRMA

2 - ) PARA ÇEKME 

3 -) PARA TRANSFER     



""")
secim = int(input("İŞLEM SEÇİNİZ:  "))




for aktifhesap in onlinehesap:
    miktar = int(input("GİRMEK İSTEDİĞİNİZ MİKTAR:  "))
    if secim == 1:
        aktifhesap += miktar
    elif secim == 2:
        aktifhesap -= miktar

print(aktifhesap)



###############################################################################################
# while döngüsüne sok para miktarı bidahakinde 3000 den başlamasın
# transfer hesabı tanımla


    # elif secim == 3:
    #     for gönderilenhesap in onlinehesap:
    #         aktifhesap -= miktar
    #         gönderilenhesap += miktar





        

# print(gönderilenhesap)


































