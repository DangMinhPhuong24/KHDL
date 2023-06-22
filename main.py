import pandas as pd
# col_test = pd.read_csv('test.csv')
df1 = pd.read_excel('khachhang.xlsx')
df2 = pd.read_excel('dssp.xlsx')
col_test = pd.read_excel('test.xlsx')

Ten_kh = df1['Khach hang']
Ten_sp = df2['Ten san pham']
Ds_sp =[]
SP = []
ID_kh = 0
TenKH ='Hoàng'
ID_gt = 0   
Gioi_tinh ='Giới tính Nam'
for i in range(len(Ten_kh)):
    if Ten_kh[i] == TenKH:
        ID_kh = i

for i in range(len(Ten_kh)):
    if Ten_kh[i] == Gioi_tinh:
        ID_gt = i

if ID_kh == 0 and ID_gt == 0:
    
    print('Khách hàng tên : ',TenKH)
    print('Giới tính : ',Gioi_tinh)
    print('Không có dữ liệu')

elif ID_kh != 0 and ID_gt == 0:
    for i in range(len(col_test['Ten khach hang'])):
        if ID_kh == col_test['Ten khach hang'][i]:
            Ds_sp.append(int(col_test['San pham mua'][i]))
    for i in range(len(Ds_sp)):
        if Ten_sp[Ds_sp[i]] not in SP:
            SP.append(Ten_sp[Ds_sp[i]])

    print('khách hàng tên : ',TenKH)
    print('Các sản phẩm gợi ý  : ',SP)

elif ID_kh == 0 and ID_gt != 0:
    for i in range(len(col_test['Gioi tinh'])):
        if ID_gt == col_test['Gioi tinh'][i]:
            Ds_sp.append(int(col_test['San pham mua'][i]))
    for i in range(len(Ds_sp)):
        if Ten_sp[Ds_sp[i]] not in SP:
            SP.append(Ten_sp[Ds_sp[i]])

    print('Giới tính : ',Gioi_tinh)
    print('Các sản phẩm gợi ý  : ',SP)

else:
    for i in range(len(col_test['Ten khach hang'])):
        if ID_kh == col_test['Ten khach hang'][i]:
            Ds_sp.append(int(col_test['San pham mua'][i]))
    for i in range(len(col_test['Gioi tinh'])):
        if ID_gt == col_test['Gioi tinh'][i]:
            Ds_sp.append(int(col_test['San pham mua'][i]))
    for i in range(len(Ds_sp)):
        if Ten_sp[Ds_sp[i]] not in SP:
            SP.append(Ten_sp[Ds_sp[i]])

    print('khách hàng tên : ',TenKH)
    print('Giới tính : ',Gioi_tinh)
    print('Các sản phẩm gợi ý  : ',SP)























# --------------------------đọc file txt-------------------------------
# name = open("Name.txt",'r',encoding='utf-8')

# def load_name(name):
#     ten_kh =[]
#     ten_sp =[]
#     ten =''
#     X = name.readline()
#     for i in range(len(X)):
#         if X[i] == ',' or X[i] == ']':
#             ten_kh.append(ten)
#             ten =''
#         if X[i] != ',' and X[i] != ']' and X[i] != '\n':
#             ten = ten+X[i]
#     X = name.readline()
#     for i in range(len(X)):
#         if X[i] == ',' or X[i] == ']':
#             ten_sp.append(ten)
#             ten =''
#         else:
#             ten =ten+X[i]
#     return ten_kh,ten_sp
# Ten_kh,Ten_sp = load_name(name)

# ---------------------------Theo Tên-------------------------------

# ID_kh = 0
# TenKH = 'Hoàng'
# for i in range(len(Ten_kh)):
#     if Ten_kh[i] == TenKH:
#         ID_kh = i
        
# if ID_kh == 0:
#     print('khách hàng tên : ',TenKH)
#     print('Không có dữ liệu')
# else:
#     for i in range(len(col_test['Ten khach hang'])):
#         if ID_kh == col_test['Ten khach hang'][i]:
#             Ds_sp.append(int(col_test['San pham mua'][i]))
#     for i in range(len(Ds_sp)):
#         if Ten_sp[Ds_sp[i]] not in SP:
#             SP.append(Ten_sp[Ds_sp[i]])

#     print('khách hàng tên : ',TenKH)
#     print('Các sản phẩm gợi ý  : ',SP)


# ----------------------------Theo Giới tính-----------------------------------
# ID_gt = 0
# Gioi_tinh = 'Nam'
# for i in range(len(Ten_kh)):
#     if Ten_kh[i] == Gioi_tinh:
#         ID_gt = i
        
# if ID_gt == 0:
#     print('Giới tính : ',Gioi_tinh)
#     print('Không có dữ liệu')
# else:
#     for i in range(len(col_test['Gioi tinh'])):
#         if ID_gt == col_test['Gioi tinh'][i]:
#             Ds_sp.append(int(col_test['San pham mua'][i]))
#     for i in range(len(Ds_sp)):
#         if Ten_sp[Ds_sp[i]] not in SP:
#             SP.append(Ten_sp[Ds_sp[i]])

#     print('Giới tính : ',Gioi_tinh)
#     print('Các sản phẩm gợi ý  : ',SP)