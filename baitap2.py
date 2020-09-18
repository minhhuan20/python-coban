# in ra màng hình câu hello python
print("Hello Pthon",end="")

# in ra màng hình tên của bạn
print("Nguyễn Minh Huân",end="")

# nhập và in ra màng hình thông tin sinh viên
name ="Nguyễn Minh Huân"
mssv = 1906020149
lop = "13thc"
chuyennganh = "Công Nghệ Thông Tin"
malop = "13thc"
print("ho ten: " + name + "\nmssv: " + str(mssv) +"\nMa lop: "+malop+"\nchuyen nganh: " + chuyennganh)

# cộng 2 số nguyên
print("nhap so nguyen thu nhat: ",end="")
a=int(input())
print("nhap so nguye thu hai: ",end="")
b=int(input())
print("a + b= " + str(a+b))

x = range(3, 9)
for n in x:
  print(n)

# vẽ tam giác
mang = int(input("nhap so luong: "))
for cdoc in range(mang):
 for cngang in range(mang):
     if cngang == range(mang) or cngang < cdoc or cngang == cdoc :
      print("*",end="")
 print()    

# hinh chu nhat dat ruotruot
chieu_dai = int(input("nhap chieu dai: "))
chieu_rong = int(input("nhap chieu rong: "))
for cdai in range(chieu_dai):
    for crong in range(chieu_rong):
        print("*",end="")
    print()