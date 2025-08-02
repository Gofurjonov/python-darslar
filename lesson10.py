#20 QIYMAT QAYTARUVCHI FUNKSIYA
# Funksiyadan qiymat qaytarishni o'rganamiz
# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism
#
# talaba1 = toliq_ism_yasa('dilmurod', 'sattorov')
# talaba2 = toliq_ism_yasa('amirbek', 'muhammadaliyev')
#
# print(f"Darsga kelmagan talabalar: {talaba2} va {talaba1}")

# def toliq_ism_yasa(ism, familiya, otasining_ismi=""):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism.title()} {otasining_ismi.title()} {familiya.title()}"
#     else:
#         toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('dilmurod', 'sattorov')
# talaba2 = toliq_ism_yasa('shahrizod', 'boyqulov', 'begzodivich')
# print(f"Darsga kelmagan talabalar: {talaba2} va {talaba1}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narh = None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rang' : rangi,
#         'korobka' : korobka,
#         'yili' : yili,
#         'narh' : narh
#     }
#     return avto
# avto1 = avto_info('Gm', 'Malibu', 'Qora', 'Avtomat', 2024)
# avto2 = avto_info('Gm', 'Gentra', 'Qora', 'Avtomat', 2024, 14000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar: ')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(1,11))
# print(oraliq(10,21))

def avto_info(kompaniya, model, rangi, korobka, yili, narh = None):
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang' : rangi,
        'korobka' : korobka,
        'yili' : yili,
        'narh' : narh
    }
    return avto

print("Saytimizdagi avtolar ro'yhatini shakillantiramiz.")
avtolar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end=' ')
    kompaniya = input("ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == "no":
        break
print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang'].title()}, {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")