# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluştur
arabalar= ["Bmw", "Mercedes", "Opel", "Mazda"]


# 2- liste kaç elemanlıdır
result= len(arabalar)


# 3-listenin ilk ve son elemanı
result= arabalar[0]
result= arabalar[3]
result= arabalar[-1]
result= arabalar[-3]


# 4-mazda elemanını toyata ile değiştir
arabalar[3]= "Toyota"
result= arabalar

# 5-mercedes listenin bir elemanımıdır 
result = "Mercedes" in arabalar
# 6-listenin -2 indexsindeki değer nedir
result = arabalar[-2]
# 7-listenin ilk 3 elemanını alın
result= arabalar[0:4]
# 8-listenin son 2 elemanının yerine totoya ve renault değerlerini ekle
arabalar[-2:]= ["Toyota", "Renault"]
result= arabalar
# 9-listenin üzerine audi ve nissan değerlerini ekleyin
result = arabalar + ["Audi" ,"Nissan"] 
# 10-listenin son 2 elemanını silin 
del arabalar[-1]
result= arabalar
# 11-listenin elemnalarını tersten yazdırın
result = arabalar[::-1]
# 12-aşağıdaki verileri bir liste içinde saklayınız 
studentA = ["Yiğit","Bİlgi", 2010,[70,60,70]]
studentB= ["Sena","Yiğit",1999,[80,80,70]]
studentC= ["Ahmet","Turan",1998,[80,70,90]]
#      studentA: Yiğit Bilgi 2010, (70,60,70)
#      studentB: Sena Turan 1999, (80,80,70)
#      studentC: Ahmet Turan 1998, (80,70,90)
# 13-liste elemanlarını ekrana yazdırın
result= studentA[0]
result= studentB[1]
result= studentC[3][1]

result= f"Yiğiy Bilgi 9 yaşında ve not ortalaması 80"
result= f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+ studentA[3][1]+studentA[3][2])/3}"

print(result)

