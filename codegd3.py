#Bài 1
# ma_sv = "B26DCTV097" # Thay Mã SV bạn
# x = 97 # 3 số cuối Mã SV
# cc = 9
# bt = 8
# kt = 7.5
# thi = 6.0
# t = 7385 + x
# #Thoigian
# gio = t // 3600
# phut = (t%3600)//60
# giay = (t%3600)%60
# print(f'{gio} gio {phut} phut {giay} giay')
# thieu = 3*3600-t
# print('Còn thiếu để đủ 3 giờ:', thieu)
# hp = round(0.1 *cc+0.1*bt+0.2*kt+0.6*thi,2)
# print('Điểm học phần:', hp)
# if hp >= 8:
#     print('Xếp loại: Giỏi')
# elif hp < 8 and hp >= 6.5:
#     print('Xếp loại: Khá')
# elif hp < 6.5 and hp >=5:
#     print('Xếp loại: Trung bình')
# elif hp < 5:
#     print('Xếp loại: Yếu')
# diem = round((8-(0.1 *cc+0.1*bt+0.2*kt))/0.6,2)
# print('Điểm thi tối thiểu để đạt 8.0: ',diem)

#Bài 2
# A = [23, 45, 17, 88, 101, 64, 37,
# 45, 59, 120, 73, 17, 91, 2]

# def snt(n):
#     B = []
#     for i in n:
#         count = 0
#         for j in range(1,i+1):
#             if i%j == 0:
#                 count+=1
#         if count == 2:
#             B.append(i)
#     return B
# q = snt(A)
# print(q)
# print('Tổng các số nguyên tố:', sum(q))

# def hamtong(q):
#     for i in q:
#         tong = 0
#         goc = i
#         while i >0:
#             chuso = i%10
#             i = i//10
#             tong += chuso
#         count = 0
#         for j in range(1,tong+1):
#             if tong % j == 0:
#                 count+=1
#         if count == 2:
#             yield(goc, tong)
# c = hamtong(A)
# print(list(c))

#Bài 3
# A = [5, 3, 8, 3, 9, 1, 5, 7, 8, 2, 9, 4]
# B = [6, 3, 2, 9, 5, 7, 5, 12, 8, 15, 7, 4]
# C = []
# M = []
# K = []
# N= []
# for i in A:
#     if i not in C:
#         C.append(i)
# print('Danh sách C:', C)
# for i in A:
#     if i in B and i not in M:
#         M.append(i)
# for i in range(len(M)):
#     for j in range(i+1, len(M)):
#         if M[i] > M[j]:
#             a = M[i]
#             M[i] = M[j]
#             M[j] = a
# print('Chung A và B', M)
# for i in range(len(A)):
#     if A[i] == B[i]:
#         c = (i, A[i])
#         K.append(c)
# print('Cùng vị trí:', K)
# max = 0
# count = 0
# max2 = 0
# for i in range(len(A)):
#     while max < A[i]:
#         max = A[i]
# for i in A:
#     if i == max:
#         count+=1
# for i in A:
#     if i != max and i not in N:
#         N.append(i)
# for i in N:
#     if max2 < i:
#         max2 = i
# print('Lớn nhất: ',max, f'({count} lần)', '|', 'Lớn thứ 2:', max2)

#Bai4
ma_sv = "B26DCCC123" # Thay Mã SV bạn
ds = [
" nguyEN vaN an ",
"tran THI   binh",
" le  hoang NAM",
"pham  minh  duc ",
" nguyen  THI an",
" le  duc tung    " # Họ tên bạn
]
ds1 = []
for i in ds:
    q = i.strip().lower().split()
    c = ' '.join(q).title()
    ds1.append(c)
print('Sau chuẩn hóa:', ds1)
for i in ds1:
    m = i.rfind(' ')
    n = i[m:].lower()
    q = ''
    for j in range(m):
        if i[j].isupper():
            q=q+i[j].lower()
    n=n+q
    if i == ds1[len(ds1)-1]:
        n = n+'_'+ma_sv.lower()
    print(n)


    
