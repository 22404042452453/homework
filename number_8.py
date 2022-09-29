class AbstractClass:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            return "Ошибка: нельзя создавать объекты абстрактного класса"



obj = AbstractClass()
print(obj)
