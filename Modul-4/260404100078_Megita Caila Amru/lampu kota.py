jumlah_baris = int(input("Jumlah Baris Lampu : "))
jumlah_lampu = int(input("Jumlah Lampu pada Setiap Baris : "))

for baris in range(1, jumlah_baris):
    print()
    print("Baris", baris)
    for lampu in range(1, jumlah_lampu):
        if lampu % 3 == 0:
            print(f"Lampu {lampu} Mengalami Gangguan")
        else:
            print(f"Lampu {lampu} Berfungsi Normal")

print()
print("Periksa Sumber Listrik Utama Taman.")
print()