#15 LUG'AT ELEMENTLARI BILAN ISHLASH
# Lug'at ichida ro'yxat, lug'at ichida lug'at?

# talaba_0 = {
#     'ism': "Asadbek",
#     'familiya': "Yuldashev",
#     'yosh': 19,
#     'fakulteti': 'iqtisod',
#     'kurs' : 2
# }
# # print(talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")

# telefonlar = {
#     'ali': "iphone xs",
#     'vali': "iphone 11",
#     'jamshid': 'iphone 12',
#     'davron': "iphone 14"
# }
#
# for k, q in telefonlar.items():
#     print(f"{k.title()} ning telefoni {q}")

mahsulotlar = {
    'olma' : 5000,
    'nok' : 7000,
    'banan' : 12000,
    'uzum' : 23000,
    'qovun' : 10000
}
# print(mahsulotlar.keys())
# print("Do'kondagi mahsulotlar: ")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print("Do'kondagi mahsulotlar: ")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['qovun', 'uzum', 'banan', 'olma', 'nok', 'anor']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'konizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar: ")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# print(telefonlar.values())

# print("Foydalanuvchilar quyidagi telefonlarni ishlatadi: ")
# for tel in telefonlar.values():
#     print(tel)

telefonlar = {
    'ali': "iphone xs",
    'vali': "iphone 11",
    'jamshid': 'iphone 12',
    'davron': "iphone 14",
    'samir' : "iphone 14 pro",
    'dilmurod' : "iphone 11",
    'asadbek' : "iphone xs"
}
print("Foydalanuvchilar quyidagi telefonlarni ishlatadi: ")
for tel in set(telefonlar.values()):
       print(tel)