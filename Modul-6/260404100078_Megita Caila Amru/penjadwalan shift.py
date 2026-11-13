# Tahap 1: input nama asisten awal sampai "cukup", disimpan dalam tuple
asisten_awal = ()
nama = input("Masukkan nama asisten awal: ")
while nama != "cukup":
    asisten_awal = asisten_awal + (nama,)
    nama = input("Masukkan nama asisten awal: ")

# Tahap 2: input satu asisten tambahan, digabung ke tuple baru
tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

# Tahap 3: input nama hari tugas sampai "cukup", disimpan dalam tuple
hari_tugas = ()
hari = input("Masukkan nama hari tugas: ")
while hari != "cukup":
    hari_tugas = hari_tugas + (hari,)
    hari = input("Masukkan nama hari tugas: ")

# Input pengecualian
asisten_kecuali = input("Masukkan nama asisten pengecualian: ")
hari_kecuali = input("Masukkan hari pengecualian: ")

# Memasangkan setiap asisten dengan setiap hari, kecuali kombinasi pengecualian
for a in asisten_akhir:
    for h in hari_tugas:
        if not (a == asisten_kecuali and h == hari_kecuali):
            print(a, "-", h)