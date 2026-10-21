print("Tarif Terminal Sidoarjo")

jumlah = 0
pendapatan = 0
total_jarak = 0
terjauh = 0
jarak =  int(input("Jarak Tempuh (km) : "))

while jarak != 0:
    if jarak < 0:
        print("Jarak Tidak Valid, Ulangi!")
    else:
        jumlah += 1
        if jarak <= 5:
            tarif = 3000
        elif jarak <= 15:
            tarif = 3000 + 1000 * (jarak - 5)
        else:
            tarif = 13000 + 500 * (jarak - 15)

        if jumlah % 5 == 0:
            tarif = tarif / 2

        pendapatan += tarif
        total_jarak += jarak
        if jarak > terjauh:
            terjauh = jarak
    jarak = int(input("Jarak Tempuh (km) : "))

print("Jumlah Penumpang : ", jumlah)
print("Total Pendapatan : ", pendapatan)
print("Jarak Terjauh : ", terjauh, "km")
if jumlah > 0:
    print("Rata-rata jarak:", total_jarak / jumlah, "km")
else:
    print("Rata-rata Jarak : 0 km")