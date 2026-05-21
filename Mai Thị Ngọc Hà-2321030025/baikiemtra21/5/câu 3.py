n = int(input("Nhập số nguyên dương n: "))
tich = 1
for chu in str(n):
    tich = tich * int(chu)

if tich % 2 == 0 and tich > 20:
    print("Tich la so chan va lon hon 20")
else:
    print("Khong thoa man dieu kien")