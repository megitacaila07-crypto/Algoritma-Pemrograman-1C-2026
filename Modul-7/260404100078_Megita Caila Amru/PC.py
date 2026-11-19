undangan = set()
webinar_a = set()
webinar_b = set()

n = int(input("Jumlah undangan: "))
for i in range(n):
    undangan.add(input("Nama undangan: "))

n = int(input("Jumlah peserta Webinar A: "))
for i in range(n):
    webinar_a.add(input("Nama peserta Webinar A: "))

n = int(input("Jumlah peserta Webinar B: "))
for i in range(n):
    webinar_b.add(input("Nama peserta Webinar B: "))

print("Semua peserta kedua webinar:", webinar_a | webinar_b)
print("Peserta hadir di keduanya:", webinar_a & webinar_b)
print("Peserta hanya di salah satu webinar:", webinar_a ^ webinar_b)
print("Undangan tidak hadir di webinar mana pun:", undangan - (webinar_a | webinar_b))