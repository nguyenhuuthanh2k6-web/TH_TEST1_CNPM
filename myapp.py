a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra có phải tam giác không
if a + b > c and a + c > b and b + c > a:
    print("Đây là 3 cạnh của một tam giác")

    # Tam giác đều
    if a == b == c:
        print("→ Tam giác đều")

    # Tam giác vuông
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        # Vuông cân
        if a == b or a == c or b == c:
            print("→ Tam giác vuông cân")
        else:
            print("→ Tam giác vuông")

    # Tam giác cân
    elif a == b or a == c or b == c:
        print("→ Tam giác cân")

    # Tam giác nhọn
    elif (a*a + b*b > c*c) and (a*a + c*c > b*b) and (b*b + c*c > a*a):
        print("→ Tam giác nhọn")

    # Tam giác tù
    else:
        print("→ Tam giác tù")

else:
    print("Không phải 3 cạnh của tam giác")