import requests


class Currency:
    """

    Класс содержит функции, обнавляющие файлы с валютой
    """
    # Информация о компьютере
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.111 Safari/537.36'}

    def __init__(self):
        pass

    def get_currency_price(self, number):
        """

        Фунция, позволяет найти обновленную валюту.
        :param number: номер, позволяющий находить конкретную необходимую валюту
        :return: возвращает список с найденными новыми валютами
        """
        response_letter = []
        if number == 10:
            for i in range(6):
                # Подключение ссылки
                full_page = requests.get(LINKS[i], headers=self.headers)
                soup = BeautifulSoup(full_page.content, 'html.parser')
                # Поиск нужной иформации в строках хода
                convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})[0].text
                convert = convert.replace(" ", "")
                response_letter.append(float(convert.replace(",", ".")))
        else:
            full_page = requests.get(LINKS[number], headers=self.headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')
            convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})[0].text
            convert = convert.replace(" ", "")
            response_letter.append(float(convert.replace(",", ".")))
        return response_letter