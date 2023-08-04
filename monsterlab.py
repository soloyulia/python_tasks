# ЛАБОРАТОРИЯ ФРАНКЕНШТЕЙНА
class Monster:
    # инициализация атрибута
    def __init__(self,name,charakter):
        self.__Name = name
        self.__Charakter = charakter
    # метод
    def _type(self):
        return 'Монстр'
    def show(self):
        print('Имя: ' + self.__Name)
        print('Особенность: ' + self.__Charakter)
        print('Тип: '+self._type())

class GMonster(Monster):
    def _type(self):
        return 'Дух монстра'
class SMonster(Monster):
    def _type(self):
        return 'Душа монстра'