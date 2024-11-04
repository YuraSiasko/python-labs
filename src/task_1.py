class Parfum:

    def __init__(self, volume = 0, price = 0.0, manufacturer = "", publicInteger = 0, publicString = ""):
        self.__volume = volume
        self.__price = price
        self.__manufacturer = manufacturer
        self.publicInteger = publicInteger
        self.publicString = publicString

    def __init__(self, volume = 0, price = 0.0, manufacturer = ""):
        self.__volume = volume
        self.__price = price
        self.__manufacturer = manufacturer
        self.publicInteger = 50
        self.publicString = "unknownPublic"

    def get_volume(self):
        return self.__volume

    def get_price(self):
        return self.__price

    def get_manufacturer(self):
        return self.__manufacturer

    def set_volume(self, volume):
        self.__volume = volume

    def set_price(self, price):
        self.__price = price

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def __del__(self):
        print(f"Об'єкт {self.__manufacturer} видалено.")
        print(f"об'єкт {self.__volume} видалено.")
        print(f"об'єкт {self.__price} видалено.")

    def __str__(self):
        return f"Виробник: {self.__manufacturer}, Об'єм: {self.__volume} мл, Ціна: {self.__price} грн." 

    def __repr__(self):
        return f"Parfum(volume = {self.__volume}, price = {self.__price}, manufacturer = {self.__manufacturer})"

def main():
    firstParfum = Parfum(100, 500, "Chanel")
    secondParmun = Parfum(50, 300, "Vercase")
    thirdParfum = Parfum(75, 4000, "Zara")

    print(firstParfum)
    print(secondParmun)
    print(thirdParfum)

    print("Ціна других парфумів:", secondParmun.get_price())
    print("Виробник третіх парфумів:", thirdParfum.get_manufacturer())

    thirdParfum.set_volume(25)
    firstParfum.set_price(75)
    print(f"Оновлена ціна перших парфумів: {firstParfum.get_price()}")
    print("Оновлений об'єм третіх парфумів:", thirdParfum.get_volume())



if __name__ == "__main__":
    main()
