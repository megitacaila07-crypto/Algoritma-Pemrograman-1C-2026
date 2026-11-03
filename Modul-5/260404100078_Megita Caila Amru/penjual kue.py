def pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pelanggan(n - 1) + pelanggan(n - 2)

m = int(input("Masukkan hari ke-N: "))
print("Jumlah pelanggan pada hari ke-" + str(m) + " adalah", pelanggan(m))