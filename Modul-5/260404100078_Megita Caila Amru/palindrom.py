def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("Masukkan kata: ")
hasil = palindrom(kata)

print("Hasil fungsi:", hasil)
if hasil == True:
    print("Kata", kata, "adalah palindrom")
else:
    print("Kata", kata, "bukan palindrom")