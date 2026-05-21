n = int(input("Nhập số nguyên dương n: "))

tong_chu_so = 0
for chu in str(n):
    tong_chu_so += int(chu)

if tong_chu_so % 3 == 0:
    print("Tong chia het cho 3")
else:
    print("Tong khong chia het cho 3")