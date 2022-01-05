class Buffer:
    def __init__(self):
        self.my_sum = tuple()

    def add(self, *a):
        self.my_sum = self.my_sum + a
        if len(self.my_sum) >= 5:
            while len(self.my_sum) >= 5:
                print(sum(self.my_sum[:5]))
                self.my_sum = self.my_sum[5:]

    def get_current_part(self):
        print(list(self.my_sum))


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]
