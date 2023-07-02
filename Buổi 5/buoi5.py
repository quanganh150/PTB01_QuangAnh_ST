a = ("1: Luận văn")
b = ("2: Giáo trình giảng dạy")
print(a)
print(b)
a = 1
b = 2
T = int(input("Loại tài liệu: "))
P = int(input("Số trang: "))
C = int(input("Số bản cần in: "))
if(T == 1):
   k = 1 * P * C
   print("Số lượng giấy cần dùng: " + str(k))
if(T == 2):
   k = ((P - 1) / 2 +1) * C
   print("Số lượng giấy cần dùng: " + str(k))