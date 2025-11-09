# Bài 5 - Tính lãi đơn
# Học sinh: Ngô Minh Hiếu
# Lớp: THCS 19A3
# STT: 21
# Ngôn ngữ: Python 3

tien_gui = float(input("Nhập số tiền gửi ban đầu (VND): "))
lai_suat = float(input("Nhập lãi suất năm (%): ")) / 100

lai_1_thang = tien_gui * lai_suat * (1/12)
lai_2_quy = tien_gui * lai_suat * (2/4)
lai_3_nam = tien_gui * lai_suat * 3

print(f"Lãi sau 1 tháng: {lai_1_thang:.2f} VND")
print(f"Lãi sau 2 quý: {lai_2_quy:.2f} VND")
print(f"Lãi sau 3 năm: {lai_3_nam:.2f} VND")
