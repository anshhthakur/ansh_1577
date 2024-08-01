b = -5
print(type(b))

a = 4
print(a+b)

print(23322**100)

print(2322**1000)

print(23322**1000)   # Show error becouse of limit reached.

#******************************************************

# Converison......

# bin()
# oct()
# hex()

num = 24
b_num = 10110110

print(bin(num))
print(oct(b_num))
print(hex(num))

n = "101011"
print(int(n , 2))


print(chr(20))  # Not satisfied of the output.

#*********************************************
#Integer methods......

print((24).as_integer_ratio)
print((20.34).as_integer_ratio)
print((20.60).as_integer_ratio)


s = 111111
print(s.bit_count())

s2 = 10101111
print(s2.bit_count())


#Show error
s3 = 0011100101   
print(s3.bit_count())


#**************************************************************
# For nigative values......


print(-23322**100)

print(-2322**1000)

print(-23322**1000)   # Show error becouse of limit reached.

#******************************************************

# Converison......


num = -26
b_num = 10110110

print(bin(num))
print(oct(b_num))
print(hex(num))

n = "101011"
print(int(n , 2))


#*********************************************
#Integer methods......

print((-28).as_integer_ratio)
print((-21.34).as_integer_ratio)
print((-20.60).as_integer_ratio)