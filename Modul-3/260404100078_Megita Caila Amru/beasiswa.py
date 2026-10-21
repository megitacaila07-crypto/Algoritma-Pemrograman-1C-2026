jumlah_penuh = 0

for i in range(1, 11):
    print("Mahasiswa ke-", i)
    nama = input("Nama                  : ")
    ipk = float(input("IPK                   : "))
    penghasilan = int(input("Penghasilan orang tua : "))

    if ipk < 3.00:
        print(nama, ": Tidak memenuhi syarat")
        continue

    if penghasilan <= 3000000:
        print(nama, ": Beasiswa penuh")
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        print(nama, ": Beasiswa sebagian")
    else:
        print(nama, ": Tidak mendapatkan beasiswa")
    print()

    if jumlah_penuh == 3:
        print("Kuota beasiswa penuh terpenuhi, seleksi dihentikan.")
        break