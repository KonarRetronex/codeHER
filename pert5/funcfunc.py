
def get_discount(price, the_discount):
    discount = price * (the_discount/100)
    # return discount
    print(discount)

a = get_discount(500, 10)
print(a + 2)
#
# harga = 500
# a = get_discount(harga, 10)
# harga_setelah_discount = harga - a
# print(harga_setelah_discount)


# get_discount(500, 10)