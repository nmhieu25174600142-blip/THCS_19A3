# Bài 10 - Tính tổng lương thực nhận
# Học sinh: Ngô Minh Hiếu
# Lớp: THCS 19A3
# STT: 21
# Ngôn ngữ: Python 3

luong_co_ban = float(input("Nhập lương cơ bản (VND): "))
ngay_cong = int(input("Nhập số ngày công trong tháng: "))

luong_mot_ngay = luong_co_ban / 22
luong_thuc_te = luong_mot_ngay * ngay_cong

thuong = 0
phat = 0

if ngay_cong > 22:
    thuong = 0.1 * luong_thuc_te
elif ngay_cong < 22:
    phat = 0.05 * luong_thuc_te

tong_thuc_nhan = luong_thuc_te + thuong - phat

print(f"Tổng lương thực nhận: {tong_thuc_nhan:.2f} VND")
