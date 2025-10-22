#Menghitung nilai akhir mahasiswa

# Data mahasiswa
nim = 25552011290
nama = "Wafi Muhammad Zain"
kelas = "TIF RP 25E"

# Bobot nilai
bobot_presensi = 0.15
bobot_tugas = 0.25
bobot_kuis = 0.10
bobot_uts = 0.20
bobot_uas = 0.30

# Input nilai
nilai_presensi = int(input("Masukkan nilai presensi : "))
nilai_tugas = int(input("Masukkan nilai tugas : "))
nilai_kuis = int(input("Masukkan nilai Kuis : "))
nilai_uts = int(input("Masukkan nilai UTS : "))
nilai_uas = int(input("Masukkan nilai UAS : "))

# Menghitung nilai akhir
nilai_akhir = (nilai_presensi * bobot_presensi +
               nilai_tugas * bobot_tugas +
               nilai_uts * bobot_uts +
               nilai_uas * bobot_uas +
               nilai_kuis * bobot_kuis)

# Menampilkan hasil
print("\n=== Nilai Akhir Mahasiswa ===")
print("NIM          :", nim)
print("Nama         :", nama)
print("Kelas        :", kelas)
print("Nilai Presensi :", nilai_presensi)
print("Nilai Tugas    :", nilai_tugas)
print("Nilai Kuis     :", nilai_kuis)
print("Nilai UTS      :", nilai_uts)
print("Nilai UAS      :", nilai_uas)
print("Nilai Akhir  :", round(nilai_akhir,2))




