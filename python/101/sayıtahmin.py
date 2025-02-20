import random

sayı = random.randint(1,100)
can = int(input("KAÇ HAK KULLANMAK İSTERSİNİZ: "))
hak = can
sayaç = 0
kalanhak = 10
while hak> 0:
    hak -= 1
    sayaç += 1
    kalanhak -= 1
    tahmin = int(input("tahmin:  "))
    if sayı== tahmin:
        print(f"TEBRİKLER BİLDİNİZ {sayaç}. defada bildiniz. TOPLAM PUANINIZ: {100 - (100/can) * (sayaç-1)} ")
        break
    elif sayı > tahmin:
        print(f"BİRAZ DAHA YUKARI. KALAN HAKKINIZ: {kalanhak}")
    else:
        print(f"BİRAZ DAHA AŞAĞI. KALAN HAKKINIZ: {kalanhak} ")
    if hak == 0:
        print(f"HAKKINIZ BİTTİ. TUTULAN SAYI: {sayı}")






















