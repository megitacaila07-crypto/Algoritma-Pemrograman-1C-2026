def evaluasi(pc):
    ram = int(pc[2])
    if pc[1] == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

inventaris = []
jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    nama = input("Nama PC: ")
    status = input("Status (normal/rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    inventaris.append([nama, status, ram])

for pc in inventaris:
    try:
        hasil = evaluasi(pc)
    except:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')