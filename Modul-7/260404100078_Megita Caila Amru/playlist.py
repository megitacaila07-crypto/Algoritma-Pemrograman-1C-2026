playlist = {}

while True:
    print("--- MENU ---")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        nama = input("Nama playlist: ")
        if nama in playlist:
            print("Playlist sudah ada")
        else:
            playlist[nama] = {}

    elif menu == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            playlist[nama][judul] = penyanyi
        else:
            print("Playlist tidak ditemukan")

    elif menu == "3":
        for nama in playlist:
            print("Playlist", nama)
            for judul in playlist[nama]:
                print("-", judul, ":", playlist[nama][judul])

    elif menu == "4":
        judul = input("Judul lagu yang dicari: ")
        ketemu = False
        for nama in playlist:
            if judul in playlist[nama]:
                print("Ada di playlist", nama, "- penyanyi:", playlist[nama][judul])
                ketemu = True
        if not ketemu:
            print("Lagu tidak ditemukan")

    elif menu == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
            else:
                print("Lagu tidak ditemukan")
        else:
            print("Playlist tidak ditemukan")

    elif menu == "6":
        nama = input("Nama playlist: ")
        if nama in playlist:
            del playlist[nama]
        else:
            print("Playlist tidak ditemukan")

    elif menu == "7":
        break