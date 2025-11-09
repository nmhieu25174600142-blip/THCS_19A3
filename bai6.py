# Bài 6 - Kiểm tra năm nhuận
# Học sinh: Ngô Minh Hiếu
# Lớp: THCS 19A3
# STT: 21
# Ngôn ngữ: Python 3

nam = int(input("Nhập một năm: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")
