def is_triangle(a, b, c):
    return (
        a > 0 and b > 0 and c > 0 and
        a + b > c and
        a + c > b and
        b + c > a
    )

print("Kiểm tra tam giác")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if is_triangle(a, b, c):
    print("✔ Đây là 3 cạnh của một tam giác.")
else:
    print("✘ Không phải là tam giác.")