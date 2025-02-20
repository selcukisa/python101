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

3 - ) PARA TRANSFER     



""")



def paracek(hesap):

    
    secim = int(input("İŞLEM SEÇİNİZ:  "))
                    
    for aktifhesap in onlinehesap:
            
            

        if secim == 1:
            miktar = int(input("GİRMEK İSTEDİĞİNİZ MİKTAR:  "))
            aktifhesap += miktar

        if secim == 2:
            miktar = int(input("GİRMEK İSTEDİĞİNİZ MİKTAR:  "))
            aktifhesap >= miktar
            aktifhesap -= miktar
        else:
            print("YETERSİZ BAKİYE")
            break
        
            
        if secim == 3:
            transfersecimi = input("PARA GÖDERMEK İSTEDİĞİNİZ HESABIN HESAP NUMARASINI GİRİNİZ:  ")
            

            
            
            if transfersecimi == False:
                
                break
                 
            if  transfersecimi == SelcukHesap['hesapNO']:
                    miktar = int(input("GÖNDERMEK İSTEDİĞİNİZ MİKTAR:  "))
                    aktifhesap -= miktar
                    SelcukHesap['bakiye'] += miktar
                    print(F"SELÇUK' UN HESABINDAKİ PARA: {SelcukHesap['bakiye']}")

            elif transfersecimi == AkifHesap['hesapNO']:
                    miktar = int(input("GÖNDERMEK İSTEDİĞİNİZ MİKTAR:  "))
                    aktifhesap -= miktar
                    AkifHesap['bakiye'] += miktar
                    print(f"AKİF' İN HESABINDAKİ PARA: {AkifHesap['bakiye']}")
                
                    
                
                
        print(F"HESABINIZDAKİ SON PARA DURUMU: {aktifhesap}")
            
    return
          
paracek(onlinehesap)













