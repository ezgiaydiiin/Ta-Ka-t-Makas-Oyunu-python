# taskagıtmakas

import random


sayac = 0
elemanlar = ['t', 'k', 'm']
oyuncuskor = 0
pcskor = 0


def karsilastir(oyuncu, pc, oyuncuskor, pcskor):
    if oyuncu == 'k' and pc == 't':
        oyuncuskor += 1
    elif oyuncu == 'k' and pc == 'm':
        pcskor += 1
    elif oyuncu == 't' and pc == 'm':
        oyuncuskor += 1
    elif oyuncu == 't' and pc == 'k':
        pcskor += 1
    elif oyuncu == 'm' and pc == 't':
        pcskor += 1
    elif oyuncu == 'm' and pc == 'k':
        oyuncuskor += 1

    return oyuncuskor,pcskor


while True:
    oyuncu = input("tas icin t ye kagit icin k ye makas icin m ye basın\n")
    pc = random.choice(elemanlar)
    print(pc)

    oyuncuskor, pcskor = karsilastir(oyuncu, pc, oyuncuskor, pcskor)
    print("sizin skorunuz: ", oyuncuskor)
    print("pc skoru: ", pcskor)
    sayac+=1

    if oyuncuskor == 3 or pcskor == 3:


        if oyuncuskor > pcskor:
            print("tebrikler siz kazanadınız")
            break
        elif oyuncuskor == pcskor:
            print("berabere kalındı")
            break
        else:
            print("bilgisayar kazandı")
            break