n = int(input("Nhập số lượng phần tử n: "))
day_so = []
for i in range(n):
    x = float(input("Nhập số thứ {i+1}: "))
    day_so.append(x)
tong = 0
dem = 0
for so in day_so:
    if 0 < so < 1000:
        tong += so
        dem += 1
if dem > 0:
    trung_binh = tong / dem
    print("Trung bình cộng = {trung_binh:.2f}")
else:
    print("Không có số nào trong khoảng (0, 1000)")