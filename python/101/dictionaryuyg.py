ogrenciler = {}

number = input("öğrenci no:  ")
name = input("öğrenci adı:  ")
surname = input("öğrenci soyadı:  ")
phone = input("öğrenci telefon:  ")

# ogrenciler[number] = {
#         "ad" : name,
#         "soyad" : surname,
#         "telefon" : phone,
# }

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})



number = input("öğrenci no:  ")
name = input("öğrenci adı:  ")
surname = input("öğrenci soyadı:  ")
phone = input("öğrenci telefon:  ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})



number = input("öğrenci no:  ")
name = input("öğrenci adı:  ")
surname = input("öğrenci soyadı:  ")
phone = input("öğrenci telefon:  ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})



print("*"*50)

ogrno = input("öğrenci no:  ")
ogrenci = ogrenciler[ogrno]

print(f"Aradığınız {ogrno} nolu öğrencinin adı: {ogrenci['ad']} soyadı:{ogrenci['soyad']} ve telefonu ise: {ogrenci['telefon']}")




































