#Membandingkan 2 angka dan menampilkan yang lebih besar
#Input nilai
nilai1 = int(input("Masukkan nilai pertama: "))
nilai2 = int(input("Masukkan nilai kedua: "))
#Membandingkan dan menampilkan hasil
if nilai1 > nilai2:
    print("Nilai pertama lebih besar:", nilai1)
elif nilai2 > nilai1:
    print("Nilai kedua lebih besar:", nilai2)
else:
    print("Kedua nilai sama:", nilai1)


#Menentukan kategori umur
#input umur
umur = int(input("Masukkan umur Anda: "))
#enentukan kategori umur
if umur < 0:
    print("Umur tidak valid")
elif umur <= 12:
    print("Anda adalah anak-anak")
elif umur <= 19:
    print("Anda adalah Remaja")
elif umur <= 59:
    print("Anda adalah Dewasa")
else:
    print("Anda adalah Lansia")

#Menmpilkan tabel perkalian 1-10 menggunakan loop
print("Tabel Perkalian 1-10:")
#Melakukan perulangan
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=' ')
    print()
