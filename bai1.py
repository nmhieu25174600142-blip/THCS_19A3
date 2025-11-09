# Bài 1 - Tính tổng chi phí và thuế VAT
# Học sinh: Ngô Minh Hiếu
# Lớp: THCS 19A3
# STT: 21
# Ngôn ngữ: Python 3

gia = float(input("Nhập giá sản phẩm (VND): "))
so_luong = int(input("Nhập số lượng: "))
tong_tien = gia * so_luong
vat = tong_tien * 0.1
tong_phai_tra = tong_tien + vat
print(f"Tổng tiền phải trả (đã gồm VAT): {tong_phai_tra:.2f} VND")
