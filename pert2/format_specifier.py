# Format specifiers = {value:flags} → format a value based on the flags inserted
#
# .(number)f  = round to that many decimal places (fixed point)
# Example:  f"{3.14159:.2f}" → 3.14
#
# (number)    = allocate that many spaces
# Example:  f"{42:6}" → '    42'
#
# 0(number)   = allocate and zero-pad that many spaces
# Example:  f"{42:06}" → '000042'
#
# :<          = left justify
# Example:  f"{'Hi':<5}" → 'Hi   '
#
# :>          = right justify
# Example:  f"{'Hi':>5}" → '   Hi'
#
# :^          = center align
# Example:  f"{'Hi':^5}" → ' Hi  '
#
# :+          = use a plus sign to indicate positive value
# Example:  f"{42:+}" → '+42'
#
# :=          = place sign to leftmost position
# Example:  f"{-42:=6}" → '-   42'
#
# : (space)   = insert a space before positive numbers
# Example:  f"{42: }" → ' 42'
#
# :,          = use a comma as a thousands separator
# Example:  f"{1000000:,}" → '1,000,000'

# Format specifiers = {value:flags} → format a value based on the flags inserted
#
# .(number)f  = round to that many decimal places (fixed point)
# (number)    = allocate that many spaces
# 0(number)   = allocate and zero-pad that many spaces
# :<          = left justify
# :>          = right justify
# :^          = center align
# :+          = use a plus sign to indicate positive value
# :=          = place sign to leftmost position
# : (space)   = insert a space before positive numbers
# :,          = use a comma as a thousands separator

angka = 12.7149743187072
angka2 = 1
print("00000")
print(f"{angka2:05}")
print(f"{angka:.0f}")




# print(f"{10000000:,}")
#
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
#
# print(f"Price 1 is ${price1:10.2f}")
# print(f"Price 2 is ${price2:10.2f}")
# print(f"Price 3 is ${price3:10.2f}")
