#collection
#list [], ordered, dupliket oke, bisa diubah ubah
#set {} unroder, duplikat not oke, bisa diubah ubah
#tuple () order, duplikat ok, gak bisa diubah ubah

# buah_buahan = ["apple", "pineapple", "grape", "avocado", "banana", "cherry"]
#                 0          1          2         3          4          5
# print(buah_buahan[:3])

# print(buah_buahan)

# for buah in buah_buahan:
#     print(buah, end=" ")
#
# print("\nHALLOOOOO")

# buah_buahan = ["apple", "pineapple", "grape", "avocado", "banana", "cherry", "apple"]
# # print(dir(buah_buahan))
# # print(help(buah_buahan))
#
# # print(buah_buahan.count("apple"))
#
# buah_buahan[1] = "sherlock"
# buah_buahan.insert(2, "rock")
# buah_buahan.remove("rock")
#
# # buah_buahan.append("jambu")
# #
# print(buah_buahan)

# buah_buahan = {"apple", "pineapple", "grape", "avocado", "banana", "cherry", "apple"}
#
# buah_buahan.remove("apple")
# print(buah_buahan)

# buah_buahan = ("apple", "pineapple", "grape", "avocado", "banana", "cherry", "apple")
#
# print(buah_buahan.index("grape"))
#
# print(dir(buah_buahan))



#--------------------------------dictionary---------------------------------------
#             key    value
mahasiswa = {"085":"fani",
             "002":"nayla",
             "029":"audy"}

# print(mahasiswa.get("085")) #buat dapaten value dengan cara kasih key
# print(mahasiswa["fani"])

key = mahasiswa.keys()
print(key)

for key in mahasiswa.keys():
    print(key)

print(" ")
print("-------value---------")

value = mahasiswa.values()
print(value)

for value in mahasiswa.values():
    print(value)

print(" ")
print("-------key & value---------")
item = mahasiswa.items()
print(item)

for key, value in item:
    print(f"{key} : {value}")

#-----------------------random------------------------------
import random

# high = 30
# low =12
# print(random.randint(low, high)) #random integer

buah = ["apple", "anggur", "jeruk"]

option = random.choice(buah)
print(option)

























