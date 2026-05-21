tong = 0
n = int(input("nhap so trong day :"))

while n != 0:
    if n % 2 == 0:                      
        tong = tong + n                  
        print("tong cac so chan la:", tong)
    
    
    n = int(input("nhap so tiep theo (nhap 0 de dung):"))