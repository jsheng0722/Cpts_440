a = 0
b = 0
c = 0
d = 1000

for i in range (11):
    a = a + 0.9 * (-1 + 0.9 * b - a)
    print(str(a))
    b = b + 0.9 * (-1 + 0.9 * c - b)
    print(str(b))
    c = c + 0.9 * (-1 + 0.9 * d - c)
    print(str(c) + "\n")
