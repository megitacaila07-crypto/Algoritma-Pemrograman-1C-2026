total_gaji = 0

for hari in range(1, 8):
    print(f"Hari ke - {hari}")
    gaji = 100000

    lembur = int(input("Jam Lembur : "))
    while lembur < 0 or lembur == 5 or lembur == 7:
        print("Jam Lembur tidak valid, Masukan Ulang!")
        lembur = int(input("Jam Lembur : "))

    if lembur == 0:
        upah_lembur = 0
    elif lembur <= 4:
        upah_lembur =  lembur * 25000
    elif lembur == 6:
        upah_lembur =  200000
    elif lembur == 8:
        upah_lembur  = 300000
    else:
        print("Jumlah lembur melebihi batas yang ditentukan")
        upah_lembur = 0

    shift = input("Apakah shift malam ? ")
    if shift == "ya":
        gaji = gaji + 50000

    gaji = gaji + upah_lembur
    total_gaji = total_gaji + gaji
    print(f"Gaji hari ke - {hari} : Rp {gaji}")

print(f"Total gaji mingguan : Rp {total_gaji}")
