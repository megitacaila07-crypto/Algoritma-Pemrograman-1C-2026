total_awal = int(input("Total belanja: "))

if total_awal % 100000 == 0:
    bayar = 0
elif total_awal % 50000 == 0:
    bayar = total_awal - (total_awal * 50 / 100)
elif total_awal % 10000 == 0:
    bayar = total_awal - (total_awal * 20 / 100)
elif total_awal >= 200000:
    bayar = total_awal - (total_awal * 10 / 100)
else:
    bayar = total_awal

poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"

print("Total belanja awal:", total_awal)
print("Total bayar:", bayar)
print("Status poin:", poin)