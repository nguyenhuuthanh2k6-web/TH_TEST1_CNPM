def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Ví dụ
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))

print("BCNN =", lcm(x, y))