#Foydalanuvchi kiritgan ikki sonni qo'shish algoritmi:

# def addNums(a,b):
#     summa = a + b
#     return summa

#Uchta sondan eng kattasini topish algoritmi

# def getlargest(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     else:
#         if a<b:
#             if b>c:
#                 return b
#             else:
#                 return c
#
# print(getlargest(1,3,4))

#N faktorialni hisoblash algoritmi

def faktorial(N):
    i=1
    fakt=1
    while i != N + 1:
        fakt = fakt * i
        i += 1
    return fakt
print(faktorial(8))