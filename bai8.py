# Bài 8 - Tính chỉ số BMI
# Học sinh: Ngô Minh Hiếu
# Lớp: THCS 19A3
# STT: 21
# Ngôn ngữ: Python 3

can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
