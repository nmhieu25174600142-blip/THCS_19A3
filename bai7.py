# Bài 7 - Kiểm tra quyền truy cập
# Học sinh: Ngô Minh Hiếu
# Lớp: THCS 19A3
# STT: 21
# Ngôn ngữ: Python 3

ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")

if ten_dang_nhap == "admin" and mat_khau == "password123":
    print("Đăng nhập thành công!")
else:
    print("Sai tên đăng nhập hoặc mật khẩu.")
