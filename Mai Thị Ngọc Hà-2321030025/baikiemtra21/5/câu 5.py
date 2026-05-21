m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
tong_chu_so_n = 0
for chu in str(n):
    tong_chu_so_n += int(chu)
if tong_chu_so_n == 0:
    print("Tổng chữ số của n bằng 0, không chia được")
else:
    if m % tong_chu_so_n == 0:
        print("m chia hết cho",tong)
    else:
        print("m KHÔNG chia hết cho",tong)