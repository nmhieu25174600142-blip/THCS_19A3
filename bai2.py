# Bài 2 - Tính số kẹo mỗi học sinh nhận
# Học sinh: Ngô Minh Hiếu
# Lớp: THCS 19A3
# STT: 21
# Ngôn ngữ: Python 3

tong_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập số học sinh: "))
keo_moi_hs = tong_keo // so_hoc_sinh
keo_thua = tong_keo % so_hoc_sinh
print(f"Mỗi học sinh nhận được: {keo_moi_hs} viên kẹo")
print(f"Số kẹo còn thừa: {keo_thua}")
