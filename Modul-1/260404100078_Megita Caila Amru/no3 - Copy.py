# Kebutuhan bahan bakar

jarak_pergi =  100 #km
konsumsi = 40 #km per liter
sisa_bensin = 1.5 #liter
harga_bensin = 10000 #Rp per liter

# Total jarak Pulang-Pergi
total_jarak = jarak_pergi * 2

# Total kebutuhan bahan bakar
total_bensin = total_jarak / konsumsi

# Bahan bakar yang harus dibeli
beli_bensin = total_bensin - sisa_bensin

# Total biaya
total_biaya = beli_bensin * harga_bensin

# Hasil
print("-----HASIL-----")
print("Total jarak perjalanan =",  total_jarak, "km")
print("Total kebutuhan bahan bakar =", total_bensin, "liter")
print("Bahan bakar yang harus dibeli =", beli_bensin, "liter")
print("Total Biaya = Rp", total_biaya)