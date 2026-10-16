pin = int(input("PIN: "))
jam = int(input("Jam: "))

a = pin // 100
b = (pin // 10) % 10
c = pin % 10

print(a, b, c)

if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Lampu Dinyalakan")
elif pin % 2 == 0:
    if a + c == b:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi!")
else:
    print("Akses Ditolak")

print("Mode Malam Merekam" if jam > 18 else "Mode Siang Standby")