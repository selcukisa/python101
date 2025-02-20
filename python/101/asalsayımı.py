while True:
    sayı = int(input("sayı girin:  "))
    if sayı > 1:
        
        for i in range(2,sayı):
            if (sayı%i) == 0:
                print(sayı, "asal sayı değildir.")
                break
        else:
            print(sayı, "asal sayıdır")
            
    else:
        print(sayı,"asal sayı değildir")
    

































