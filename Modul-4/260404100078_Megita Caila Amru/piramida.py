n = int(input("Masukkan bilangan bulat positif n: "))

for baris in range(1, n + 1):
    for angka in range(1, baris + 1):
        print(angka, end="")

    for spasi in range(n - baris):
        print(" ", end="")

    for jarak in range(4):
        print(" ", end="")

    for spasi in range(n - baris):
        print(" ", end="")

    for angka in range(baris, 0, -1):
        print(angka, end="")

    print()