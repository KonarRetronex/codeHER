



# age = int(input("masukkan usiamu: "))
#
# if age > 100:
#     print(f"tua banget udah {age} tahun")
# elif age >= 17:
#     print("lo dah bisa buat sim")
# elif age == 0:
#     print("baru lahir dah mau buat sim")
# elif age < 0:
#     print("ngacok lo, masa usia negatif")
# else:
#     print("msaih kecil")

#
# day = input("masukkan hari: ")
#
# match day:
#     case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
#         print("Kuliah woy")
#     case "saturday" | "sunday":
#         print("Libur yey")
#     case _:
#         print("ngacok lo")


# match day:
#     case "monday":
#         print("Kuliah woy")
#     case "tuesday":
#         print("Kuliah woy")
#     case "wednesday":
#         print("Kuliah woy")
#     case "thursday":
#         print("Kuliah woy")
#     case "friday":
#         print("Kuliah woy")
#     case "saturday":
#         print("Libur yey")
#     case "sunday":
#         print("Kuliah woy")


# jumlah_waktu_tidur = 10
# deadline_tugas = input("masukkan (True/False): ").lower().strip() == "true"
# waktu_main_game = 2
#
# if deadline_tugas == "false":
#     deadline_tugas = False
# elif deadline_tugas == "true":
#     deadline_tugas = True
# else:
#     print("Ngaco lo, masukkinnya antara True atau False doang")
#
# if not deadline_tugas and jumlah_waktu_tidur >= 5:
#     print("YEYY")
# elif deadline_tugas and jumlah_waktu_tidur < 5:
#     print("mampos lo")
# elif waktu_main_game > 6 or jumlah_waktu_tidur > 10:
#     print("Jangan lupa belajar")
# else:
#     print("terserah lah isi apa, gua bingung")

# deadline_tugas = input("Masukkan (True/False)").lower() == "true"
# if deadline_tugas:
#     print("nah")
# elif not deadline_tugas:
#     print("yey")


number1 = float(input("Masukkan angka pertama: "))
number2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+ - / *): ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print("Operator tidak ditemukan")

if result.is_integer():
    result = int(result)
print(result)

















