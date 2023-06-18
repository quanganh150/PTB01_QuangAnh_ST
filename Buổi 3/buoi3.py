#"/n" = xuống dòng
#sep = tạo khoảng cách bằng một dấu gạch ẩn
#VD
#lệnh Input
#Ten = input("Nhập tên của bạn")
#Tuoi = input("Nhập tuổi của bạn")
#Lop = input("Lớp")
#so_thich = input("sở thích")
#print("Phỏng vấn nhận việc",Ten, Tuoi, Lop, so_thich)

# Cách để biến một giá trị thành kiểu dữ liệu mong muốn
#n = (int(input("n là một số nguyên")))

# tạo phép tính với chữ và số
# phep cộng và phép nhân dành cho chữ
#VD:print("O" + "M" + "G") = OMG
#print("O*3") = OOO
#print(("O")*3)
#Số
#VD: print (3+3)
#print (3*7)

#BTVN
dola = 1500
vnd = 35205000
kq1 = vnd/dola
print("Số tiền VND của 1$ là: " + str(kq1) + "VND")

tqd = float(input("Số đô la cần quy đổi: "))
kq2 = tqd * kq1
print("Số tiền VND của "+ str(tqd) +"đô la: " + str(kq2))

mot_t = 1340233
tien_t = 367329673
kq3_1 = tien_t//mot_t
print("Số tháng kiếm được hơn 367.329.673 VND là: " + str((kq3_1 + 1)) + "tháng")
kq3_2 = ((kq3_1 + 1)*mot_t)/kq1
print("Số đô la của tháng hơn đó là: " + str(kq3_2)+ "$")