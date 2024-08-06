a1 = 0.1256E2
b1 = 1256E-2
print(a1,b1)

print(float(11))
print(float(-11))
print(float(0b1011))
print(float(-0xe))
print(float(0x14))
print(float(-0x14))

"""Boolean..............."""

print(int(True))
print(int(False))


""" Complex Number..................."""


print(complex(11))
print(complex(11.0))
print(complex(-11))


"""" Type Conversion................"""

# Implicet type conversion........

a = 5
print(type(a))
b = 7.6
print(type(b))
c = a + b
print(type(c))

# Explicit type conversion.........

# Input finction..

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = x + y
print(z)

print(int(11.36))
print(int(.1136))
print(int(.1136E2))
print(int(1136E-2))

p = "Ansh "
q = " Thakur"
r = p + q
print(r)

print(int(3+5j))   #Show Error = "int() argument must be a string, a bytes-like object or a real number, not 'complex' "

e = "John"
i = "Amit"
j = int(e+i)
print(j)   #Show Error = " invalid literal for int() with base 10: 'JohnAmit' "

f = "4"
g = "7"
h = int(f+g)
print(h)

