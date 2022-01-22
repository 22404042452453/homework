import numpy as np
import matplotlib.pyplot as plt


def linefunction(function):
    try:
        func = lambda x: eval(function)
        x = np.linspace(-10, 10, 100)
        plt.figure(figsize=(13, 9))
        plt.plot(x, func(x), "-g", label="Функция")
        plt.xlabel("Х")
        plt.ylabel("Y")
        plt.title(f"График функции ${function}$")
        plt.grid()
        plt.show()
    except Exception as ex:

        return "Something_wrong"


def formation(function):
    dict_trig = {'sin': '180/np.pi*np.sin',
                 'cos(x)': '180/np.pi*np.cos',
                 'tg(x)': '180/np.pi*np.tan',
                 }

    ### раставляем звезды
    for i in range(len(function)-1):
        if function[i].isdigit() == True and function[i + 1].isalpha() == True:
            function.insert(i + 1, "*")
        else:
            continue

    function = ''.join(function)
    ### Проверка на звезды
    for i, j in dict_trig.items():
        if i in function:
            function = function.replace(i, j)

    return function


def main():
    function = list(input("Введите свою функцию :").replace("^", "**").strip())
    linefunction(formation(function))

if __name__ == "__main__":
    main()
