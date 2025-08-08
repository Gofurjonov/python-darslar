# 28 dars Klasslar
class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya} tug'ilgan yilim {self.tyil}"
    def get_name(self):
        return self.ism
    def get_age(self, yil):
        return yil - self.tyil


talaba1 = Talaba("Asadbek", "Yuldashev", 2006)
talaba2 = Talaba("Dilmurod", "Sattorov", 2004)
talaba3 = Talaba("Siroj", "Anvarov", 2007)
print(talaba1.ism)
print(talaba1.familiya)
print(talaba1.tyil)

print(talaba1.tanishtir())
print(talaba2.tanishtir())
