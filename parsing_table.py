import requests as r
from bs4 import BeautifulSoup
import csv


def get_table(url):
    try:
        responce = r.get(url=url)
        """
        with open('html_test.html','w',encoding='utf-8') as f:
                f.write(responce.text)
        """
        with open('html_test.html', 'r', encoding='utf-8') as f:
            text = f.read()

        data = []
        prom_table = []
        soup = BeautifulSoup(text,'lxml')


        for i in soup.find(class_ = "wikitable").find_all('td',text = True):
            prom_table.append(i.text.strip().replace(',','.'))
            if len(prom_table)==21:
                data.append(prom_table)
                prom_table =[]
            else:
                continue

        with open(file = "result.csv",mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([i for i in range(1,22)])
            for i in data:
                writer.writerow(
                    (i)
                )




    except Exception as ex:

        return  "Something_wrong"


def main():
    url = 'https://powersystem.info/index.php?title=%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%B5_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2_%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2'
    get_table(url)



if __name__ == '__main__':
    main()