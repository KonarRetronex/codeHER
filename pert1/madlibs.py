# Mad Libs Lucu - Versi Bahasa Indonesia

print("=== Selamat datang di Mad Libs Lucu! ===")
print("Isi kata-kata berikut untuk membuat cerita kocak!\n")

# Meminta input dari pengguna
nama = input("Masukkan nama orang: ")
tempat = input("Masukkan nama tempat: ")
hewan = input("Masukkan nama hewan: ")
benda = input("Masukkan nama benda: ")
makanan = input("Masukkan makanan favorit: ")
kata_kerja = input("Masukkan kata kerja (misalnya: berlari, makan): ")
sifat = input("Masukkan kata sifat (misalnya: lucu, aneh): ")

# Membuat cerita
cerita = input(f"""
Suatu hari, {nama} pergi ke {tempat} sambil membawa seekor {hewan}.
Tiba-tiba, {hewan} itu mencuri {benda} milik {nama} dan mulai {kata_kerja} keliling {tempat}!
Orang-orang yang melihat langsung tertawa karena kelakuannya sangat {sifat}.
Akhirnya, {nama} hanya bisa duduk sambil makan {makanan} dan berkata,
"Aduh... hidupku penuh kejutan!"
""")

# Menampilkan hasil cerita
print("\n=== Cerita Mad Libs Lucu Kamu ===")
print(cerita)
