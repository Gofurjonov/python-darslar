# 14 LUG'AT BILAN TANISHUV
# Yangi ma'lumot turi - Dictionary bilan tanishamiz.

# car_0 = {'model': 'ferari', 'color': 'red'}
# print(car_0['model'])
# print(car_0['color'])

# en_uz = {'apple': 'olma', 'banana': 'banan', 'apricot': "o'rik"}
# print(en_uz)
# print(en_uz['banana'])

# mevalar = {'olma': 10000, 'banan': 22000, 'apelsin': 12000, 'nok': 6000}
# print(f'Apelsinning narxi {mevalar['apelsin']} so\'m')

# talaba_0 = {'ismi': 'asadbek yuldashev', 'yoshi': 19, 't_yili': 2006}
# print(f"{talaba_0['ismi'].title()},\
#       {talaba_0['t_yili']} - yilda tug\'ilgan, \
#       {talaba_0['yoshi']} yoshda")
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'iqtisod'
# print(talaba_0)
# talaba_1 = {}
# print(talaba_1)
# talaba_1['ism'] = 'Dilmurod Sattorov'
# talaba_1['kurs'] = 2
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} bu yil {talaba_1['kurs']} kursda o'qidi")
# talaba_1['kurs'] = 3
# print(f"Talaba {talaba_1['ism'].title()} bu yil {talaba_1['kurs']} kursda o'qidi")

# talaba_0 = {'ismi': 'asadbek yuldashev', 'yoshi': 19, 't_yili': 2006}
# print(talaba_0)
# del talaba_0['yoshi']
# print(talaba_0)

# telefonlar = {
#     'ali': "iphone xs",
#     'vali': "iphone 11",
#     'jamshid': 'iphone 12',
#     'davron': "iphone 14"
# }
# print(telefonlar['davron'])

# uy ishi

# akam = {'ism': "Behruz", 't_yil': 2004, 'shahar': "Toshkent"}
# ukam = {'ism': "Begzod", 't_yil': 2007, 'shahar': "Toshkent"}
# ukam2 = {'ism': "Bahrom", 't_yil': 2008, 'shahar': "Toshkent"}
# print(f"Akamning ismi {akam['ism'].title()} tug'ilgan yili {akam['t_yil']}, {akam['shahar']} da tug'ilgan")
# print(f"Ukamning ismi {ukam['ism'].title()} tug'ilan yili {ukam['t_yil']}, {ukam['shahar']} da tug'ilgan")
# print(f"Kichkina ukamning ismi {ukam2['ism'].title()} tug'ilgan yili {ukam2['t_yil']} {ukam2['shahar']} da tug'ilgan")
#
# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
#     'husan':"mastava",
#     'olim':"somsa"
#     }
#
# taom = taomlar['ali']
# print(f"Alining sevimli taomi {taom}")
#
# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])
#
# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))
#
# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")