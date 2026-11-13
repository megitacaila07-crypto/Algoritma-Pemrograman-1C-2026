daftar = []

# Meminta input nama sampai diketik "selesai"
nama = input("Masukkan nama calon anggota: ")
while nama != "selesai":
    daftar.append(nama)
    nama = input("Masukkan nama calon anggota: ")

# Memeriksa daftar satu per satu dari awal sampai akhir
for n in daftar:
    if n == "admin" or len(n) < 4:
        print("Nama", n, "tidak valid")

# Menghapus nama penyusup
penyusup = input("Masukkan nama penyusup yang akan dihapus: ")
if penyusup in daftar:
    daftar.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus")
else:
    print("Nama", penyusup, "tidak ada di daftar")

print("Daftar sekarang:", daftar)