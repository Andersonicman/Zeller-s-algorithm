# Zeller Algoritması

# 1582'den sonraki tarihler için kullanılabilir.

gunkodu = 0
def zeller(gun , ay , yil):

    yeniyil = yil % 100
    # ay kodu belirleme

    if ay == "ocak":
        aykodu = 0
    elif ay == "şubat":
        aykodu = 2
    elif ay == "mart":
        aykodu = 3
    elif ay == "nisan":
        aykodu = 6
    elif ay == "mayıs":
        aykodu = 1
    elif ay == "haziran":
        aykodu = 4
    elif ay == "temmuz":
        aykodu = 6
    elif ay == "ağustos":
        aykodu = 2
    elif ay == "eylül":
        aykodu = 5
    elif ay == "ekim":
        aykodu = 0
    elif ay == "kasım":
        aykodu = 3
    else:
        aykodu = 5

    # yil kodu belirleme

    ilkiki = yil // 100
    if ilkiki == 15:
        yilkodu = 0
    elif ilkiki == 16:
        yilkodu = 6
    elif ilkiki == 17:
        yilkodu = 4
    elif ilkiki == 18:
        yilkodu = 2
    elif ilkiki == 19:
        yilkodu = 0
    elif ilkiki == 20:
        yilkodu = 6

    # formul
    kalan = (gun + aykodu + yeniyil + yeniyil//4 + yilkodu) % 7

    if kalan == 0:
        print("Pazar")
    elif kalan == 1:
        print("Pazartesi")
    elif kalan == 2:
        print("Salı")
    elif kalan == 3:
        print("Çarşamba")
    elif kalan == 4:
        print("Perşembe")
    elif kalan == 5:
        print("Cuma")
    elif kalan == 6:
        print("Cumartesi")


gun = int(input("Lütfen Gün Giriniz : "))
ay = input("Lütfen Ay Giriniz : ").lower()
yil = int(input("Lütfen yıl Giriniz : "))


zeller(gun,ay,yil)