# Bài 9 - Tính tiền điện theo bậc thang
# Học sinh: Ngô Minh Hiếu
# Lớp: THCS 19A3
# STT: 21
# Ngôn ngữ: Python 3

kwh = int(input("Nhập số kWh điện đã tiêu thụ: "))

if kwh <= 100:
    tong_tien = kwh * 1678
elif kwh <= 200:
    tong_tien = 100 * 1678 + (kwh - 100) * 1734
else:
    tong_tien = 100 * 1678 + 100 * 1734 + (kwh - 200) * 2014

print(f"Tổng tiền điện phải trả: {tong_tien:.2f} VND")
