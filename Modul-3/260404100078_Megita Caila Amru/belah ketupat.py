n = int(input("Tinggi setengah menara (2-15) : "))

while n < 2 or n > 15:
    print("Tidak valid, ulangi!")
    n = int(input("Tinggi setengah menara (2-15) : "))

# Bagian atas (baris 1 sampai n)
for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for a in range(1, i + 1):
        print(a % 10, end="")
    for a in range(i - 1, 0, -1):
        print(a % 10, end="")
    print()

# Bagian bawah (baris n-1 sampai 1)
for i in range(n - 1, 0, -1):
    for s in range(n - i):
        print(" ", end="")
    for a in range(1, i + 1):
        print(a % 10, end="")
    for a in range(i - 1, 0, -1):
        print(a % 10, end="")
    print()