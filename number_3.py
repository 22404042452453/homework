class Translator:
    my_words = {}

    def add(self, eng, rus):
        if eng not in self.my_words.keys():
            self.my_words[eng] = [rus]
        elif eng in self.my_words.keys():
            if rus not in self.my_words[eng]:
                self.my_words[eng] += [rus]

    def remove(self, eng):
        del self.my_words[eng]

    def translate(self, eng):
        if eng in self.my_words.keys():
            return self.my_words[eng]
        else:
            return "Something was wrong"


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
print(*tr.translate('go'))
print(*tr.translate('car'))
