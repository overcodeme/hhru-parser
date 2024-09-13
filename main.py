from parser import fetch_and_parse_vacancies


def generate_url(query):
    base_url = 'https://hh.ru/vacancies/'
    query = query.replace(' ', '-')
    return base_url+query


if __name__ == '__main__':
    user_input = input('Введите ваш запрос: ')

    url = generate_url(user_input)
    vacancies = fetch_and_parse_vacancies(url)
