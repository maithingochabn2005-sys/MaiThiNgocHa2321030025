a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
tong = a + b
print("Tổng a + b = {tong}")
chu_so_lon_nhat = 0
for chu in str(tong):
    if int(chu) > chu_so_lon_nhat:
        chu_so_lon_nhat = int(chu)
        print("Chu so lon nhat =",chu_so_lon_nhat)