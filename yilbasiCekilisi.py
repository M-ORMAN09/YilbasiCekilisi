import random
import time
isim_listesi1 = []
isim_listesi2 = []

print("""\033[033m
----- YILBAŞI ÇEKİLİŞİ -----
      \033[0m""")

while(True):
    kisiSayisi = int(input("\033[032mÇEKİLİŞE KAÇ KİŞİ KATILACAK: \033[0m"))
    if(kisiSayisi < 2):
            print("\033[031mKİŞİ SAYISI 2'DEN BÜYÜK OLMALI..!\033[0m")
    else:
        break
    
sayac = 1
while(sayac <= kisiSayisi):
    isim = input(f"\033[034m{sayac}.KİŞİNİN İSMİ: \033[0m").upper()
    if(isim in isim_listesi1):
        print("\033[031mAYNI İSİMDE 2 KİŞİ OLAMAZ..!\033[0m")
    else:
        isim_listesi1.append(isim)
        isim_listesi2.append(isim)
        sayac +=1
print("\033[032mTORBA KARIŞTIRILIYOR", end='')
for i in range(3):
    print(".", end='', flush= True)
    time.sleep(3)
print("\033[0m")

while(True):
    random.shuffle(isim_listesi1)
    random.shuffle(isim_listesi2)
    eslesme_sorunu = False
    for i in range(len(isim_listesi1)):
        if isim_listesi1[i] == isim_listesi2[i]:
            eslesme_sorunu = True
            break
    if not eslesme_sorunu:
        break        
print("\033[033m\n----- SONUÇLAR -----\033[0m")
for i in range(len(isim_listesi1)):
    print(f"\033[034m\n{isim_listesi1[i]} => {isim_listesi2[i]}\033[0m")
