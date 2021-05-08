def bütünler(açı):
    cevapb = int(açı) - int(+180)
    print(cevapb)

def tümler(açı):
    cevapt = int(açı) - int(+90)
    print(cevapt)




print("""

[1] Tümler

[2] Bütünler



""")

istek = input("İsteğiniz Nedir ? ; ")
istek = int(istek)

if istek == 1:
    acevap = input(("Açı kaç derece ; "))
    acevap = int(acevap)
    tümler(acevap)

if istek == 2:
    acevap = input(("Açı kaç derece ; "))
    acevap = int(acevap)
    bütünler(acevap)
