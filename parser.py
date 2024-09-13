import requests
from bs4 import BeautifulSoup


def fetch_and_parse_vacancies(url):
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем успешность запроса

        # Парсим HTML с помощью BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим блок с результатами вакансий
        results_block = soup.find('div', {'data-qa': 'vacancy-serp__results'})

        if not results_block:
            print("Блок с результатами не найден.")
            return

        # Находим все ссылки с вакансиями
        vacancy_elements = results_block.find_all('a', {'data-qa': 'serp-item__title'})

        vacancy_data = []
        for vacancy in vacancy_elements:
            try:
                # Извлечение заголовка и ссылки
                link = vacancy.get('href')
                title_span = vacancy.find('span', {'data-qa': 'serp-item__title-text'})
                title = title_span.get_text(strip=True) if title_span else 'Без заголовка'

                vacancy_data.append({'title': title, 'link': link})
            except Exception as e:
                print(f"Ошибка при обработке вакансии: {e}")

        # Выводим результаты
        for item in vacancy_data:
            print(f"Вакансия: {item['title']}, Ссылка: {item['link']}")

    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")


# Вызов функции
if __name__ == '__main__':
    url = 'https://hh.ru/vacancies/junior-python-developer'
    fetch_and_parse_vacancies(url)
