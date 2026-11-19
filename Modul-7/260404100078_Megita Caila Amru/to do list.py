tugas = {}

while True:
    print("\n--- MENU ---")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai dan belum")
    print("6. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = "Belum"

    elif menu == "2":
        for nama in tugas:
            print(nama, ":", tugas[nama])

    elif menu == "3":
        nama = input("Nama tugas: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
        else:
            print("Tugas tidak ditemukan")

    elif menu == "4":
        nama = input("Nama tugas: ")
        if nama in tugas:
            del tugas[nama]
        else:
            print("Tugas tidak ditemukan")

    elif menu == "5":
        selesai = 0
        belum = 0
        for nama in tugas:
            if tugas[nama] == "Selesai":
                selesai += 1
            else:
                belum += 1
        print("Selesai:", selesai)
        print("Belum:", belum)

    elif menu == "6":
        break