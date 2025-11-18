import math
n = int(input("Nhap so: "))
t = int(math.isqrt(n))
print("La so chinh phuong" if t*t == n else "Khong phai so chinh phuong")
