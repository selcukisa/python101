while True:
    haftadakaçgün = int(input("gün sayısı:  "))
    günlükçalışmasaat = float(input("günlük saat:  "))
    saatlikmaaş = 55
    gelir = (haftadakaçgün * günlükçalışmasaat * saatlikmaaş * 4)

    if (0 <= gelir) and (gelir <= 11500 ):
        print("fakir katagorisindesiniz")
        if (0<= günlükçalışmasaat <= 3) or (0 <= haftadakaçgün <=3):
            print("ultra zenginsizniz")
    elif (11500 < gelir) and (gelir <= 20000):
        print("durumunuz normal")
    elif (20000 < gelir) and (gelir <= 50000):
        print("durumunuz güzel")
    elif (50000<gelir) and (gelir <= 1000000000000000000000000000000000000000000):
        print("zenginsiniz")
    else:
        print("girdiğiniz bilgileri kontrol ediniz")































