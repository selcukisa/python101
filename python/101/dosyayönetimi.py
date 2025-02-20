# dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# Kullanım: open(dosya_adi, dosya_erişme_modu)
# doysa_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir

# "w": (Write) yazma modu. dosyayı konumda oluşturur
#    ** dosyayı konumda oluşturur
#    ** dosya içeriğini siler ve yenıden ekleme yapar

#file = open("newfile.txt","w")
# file.close()
#file = open("c:/Users/Selçuk Şahin/desktop/newfile.txt","w")

# file = open("newfile.txt","w",encoding="uft-8")
# file.write("selcuk sahin")
# file.close()


# "a": (Append) ekleme. dosya konumda yoksa oluşturur

# file = open("newfile.txt","a",encoding="uft-8")
# file.write("SELÇUK Şahin")
# file.close

# "x": (create) oluşturma. dosya zaten varsa hata verir

#file = open("newfile2.txt","x",encoding="uft-8")


# "r": (read) okuma. varsayılan dosya konumda yolsa hata verir

file = open("newfile.txt","r")

print(file)








