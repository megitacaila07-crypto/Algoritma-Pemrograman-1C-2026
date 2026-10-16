regular = 40000
vip = 75000
vvip = 100000
minum = 10000
while True:
    jenis = str(input("Jenis Tiket Yang Dibeli :"))
    tiket = int(input("Jumlah Tiket Yang DIbeli :"))
    if jenis == vip:
        print("Mendapat Minuman Gratis")
    elif jenis == vvip:
        print("Mendapat Minuman Gratis")
    else:
        print("Tambahan minuman seharga Rp.10.000/tiket")
        tambah_minum = int(input("Jumlah Tambahan Minum :"))

total_tiket = tiket * jenis
total_minum = tambah_minum * minum
total = total_tiket + total_minum
print(total)
uang = int(input("uang yang dibayar:"))
kembalian =  uang - total
print(kembalian)


#Pertama tersedia data yang telah disediakan lalu disediakan untuk input jenis serta jumlah tiket yang dibeli.
# dihitung dan ditentukan apa yang diinput