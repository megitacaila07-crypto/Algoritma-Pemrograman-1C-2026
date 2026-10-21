jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total = 0
tertinggi = 0
terendah = 0
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 3):
    print("Mahasiswa ke-", i)
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", round(akhir, 2))
    print("Kategori    :", kategori)
    print()

    total += akhir

    if i == 1 or akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if i == 1 or akhir < terendah:
        terendah = akhir

        nama_terendah = nama

print("=== REKAP ===")
print("Jumlah mahasiswa A :", jumlah_A)
print("Jumlah mahasiswa B :", jumlah_B)
print("Jumlah mahasiswa C :", jumlah_C)
print("Jumlah mahasiswa D :", jumlah_D)
print("Jumlah mahasiswa E :", jumlah_E)
print("Nilai tertinggi    :", round(tertinggi, 2), "-", nama_tertinggi)
print("Nilai terendah     :", round(terendah, 2), "-", nama_terendah)
print("Rata-rata nilai    :", round(total / 10, 2))