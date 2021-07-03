print("    Seleksi Awal Studycle - Maleakhi Ekklesia")
print("==================================================")
print()
jumbil = []

def menuinput():
    #Input Bilangan
    print()
    print("                 INPUT BILANGAN")
    print("---------------------------------------------------")
    bilangan = int(input("Masukan Jumlah Bilangan = "))
    for x in range (bilangan):
        inputbil = int(input("Bilangan Ke - " + str(x+1) +" = "))
        jumbil.append(inputbil)
    print("==================================================")
    print()
    print(menu())

def menu():
    print()
    print("                  MENU PROGRAM")
    print("---------------------------------------------------")
    print("1. Menampilkan Bilangan Yang diInput")
    print("2. Melakukan Sort Ascending (Terkecil - Terbesar)")
    print("3. Melakukan Sort Descending (Terbesar - Terkecil)")
    print("4. Menampilkan Hasil Average (Rata - Rata)")
    print("5. Menampilkan Hasil Median (Nilai Tengah)")
    print("6. Menampilkan Hasil Perkalian Seluruh Bilangan Yang diInput")
    print("7. Memberikan Input Bilangan")
    print("8. Reset Input Bilangan")
    print("9. Exit Program")
    print("==================================================")
    print()
    pilihan = int(input("Masukan Pilihan Menu = "))
    print()
    if pilihan == 1 :
        if len(jumbil) <= 0 :
            print("Bilangan Belum di Input")
            d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
            if d == 1:
                print (menu())
            else:
                print(quit())
        else :
            print("Bilangan yang diinput = ",jumbil)
            d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
            if d == 1:
                print (menu())
            else:
                print(quit())
    if pilihan == 2 :
        print(asc())
        d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
        if d == 1:
            print (menu())
        else :
            print(quit())
    if pilihan == 3 :
        print(desc())
        d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
        if d == 1:
            print (menu())
        else :
            print(quit())
    if pilihan == 4 :
        print(avg())
        d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
        if d == 1:
            print (menu())
        if d == "t" or "T":
            print("Terima Kasih")
            print(quit())
        else :
            print(quit())
    if pilihan == 5 :
        print(median())
        d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
        if d == 1:
            print (menu())
        else :
            print(quit())
    if pilihan == 6 :
        print(kali())
        d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
        if d == 1:
            print (menu())
        else :
            print(quit())
    if pilihan == 7 :
        print("Bilangan Yang DiInput : ",jumbil)
        print(menuinput())
        d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
        if d == 1:
            print (menu())
        else :
            print(quit())
    if pilihan == 8 :
        print(reset())
        d = int(input("Ingin Lanjutkan [1 (ya)] / [0 (tidak)] : "))
        if d == 1:
            print (menu())
        else :
            print(quit())
    if pilihan == 9 :
            print(quit())
    else :
        print("Masukan Pilihan Menu Dengan Benar !")
        print()
        print (menu())

#Melakukan pengurutan bilangan dari terkecil ke terbesar
def asc():
    if len(jumbil) >= 1:
        jumbil.sort()
        print("Hasil Pengurutan Bilangan (Ascending) = ",jumbil)
    else :
        print("Bilangan Belum Ada")
        print(menu())

#Melakukan pengurutan bilangan dari terbesar ke terkecil
def desc():
    if len(jumbil) >= 1:
        jumbil.sort(reverse = True)
        print("Hasil Pengurutan Bilangan (Descending) = ",jumbil)
    else :
        print("Bilangan Belum Ada")
        print(menu())

#Melakukan perkalian dari semua bilangan yang di-input
def kali():
    if len(jumbil) > 0:
        hasil = 1
        for i in jumbil:
            hasil *=i
        print("Hasil Perkalian = ",hasil)
    else :
        print("Bilangan Belum Ada")
        print(menu())

#Mencari nilai rata - rata dari seluruh bilangan yang di-input
def avg():
    if len(jumbil) > 0:
        bilangan = len(jumbil)
        hasil = 0
        for i in jumbil:
            hasil +=i
            rata2 = hasil / bilangan
        print("Hasil Rata - Rata = ",rata2)
    else :
        print("Bilangan Belum Ada")
        print(menu())

#Mencari nilai tengah (median) dari bilangan yang di-input
def median():
    if len(jumbil) > 0 :
        jumbil.sort()
        print("Bilangan Setelah di-Sort = ",jumbil)
        if len(jumbil) % 2 == 0 :
            a = int(len(jumbil)/2)
            b = (jumbil[a - 1] + jumbil[a]) / 2
            median = str(b)
        else :
            a = int ((len(jumbil) + 1) / 2)
            median = str(jumbil[a - 1])
        print("Median Bilangan = ",median)
        return
    else :
        print("Bilangan Belum Ada")
        print(menu())

def reset():
    jumbil.clear()
    print("Bilangan sudah dihapus")

def quit():
    print("Terima Kasih")
    exit(0)

if __name__ == "__main__":
    while(True):
        menu()
