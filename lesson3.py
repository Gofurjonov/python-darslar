#11 BIR NECHTA SHARTLARNI TEKSHIRISH
# if-elif-else zanjiri, "and", "or" operatorlari bilan tanishamiz
# yosh = int(input("Yoshingiz nechida? "))
# if yosh <= 4:
#     print("4 yoshgacha bo'lganlarga bepul")
# elif yosh <=12:
#     print("Sizga kirish 5000 som")
# else:
#     print("Sizga kirish 10000")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# else:
#     price = 10000
#
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun nima kun? ")
# if kun.lower() == "shanba" or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")

# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower() == "yakshanba" or kun.lower() == "shanba" and harorat >= 30:
#     print("Bugun cho'milgani boramiza !")
# elif kun.lower() == "yakshanba" or kun.lower() == "shanba" and harorat <=30:
#     print("Tinchkina uyda qolamiz")

# narh = 15000
# choy = True
# salat = False
# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
# print(f"jami {narh} so'm")

# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
#
# if choy:
#     print("Mijoz choy oldi")
#     narh = narh + 5000
# if salat:
#     print("Mijoz salat oldi")
#     narh = narh + 15000
# if non:
#     print("Mijoz non oldi")
#     narh = narh + 3000
# if kompot:
#     print("Mijoz kompot oldi")
#     narh = narh + 10000
# if assorti:
#     print("Mijoz assorti oldi")
#     narh = narh + 20000
# print(f"Jami {narh} so'm")

# menu = ["somsa", "manti", "kabob", "osh", "mastava"]
# ovqat = input("Nima ovqat buyurasiz? ")
# if ovqat.lower() in menu:
#     print("Sizning buyurtmangiz qabul qilindi!")
# else:
#     print("Afsuski bunday ovqat yoq bizda !!")

menu = ["somsa", "manti", "kabob", "osh", "mastava"]
buyurtma = ["norin", "manti", "shorva", "shashlik", "osh", "somsa"]

if buyurtma:
    for taom in buyurtma:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else:
    print("Savatchangiz bo'sh")