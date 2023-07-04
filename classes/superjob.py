import requests
import os
import json

URL = 'https://api.superjob.ru/2.0/vacancies/'
SUPERJOB_API_KEY = os.environ.get('SUPERJOB_API_KEY')


class SuperJobAPI:

    def __init__(self):
        self.vacancies = None

    def get_vacancies(self, query):
        print(f'Получаем данные с {URL}...')
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        params = {
            'keyword': query,
            'page': 0,
            'count': 100,
            # 'only_with_salary': True
        }
        response = requests.get(URL, headers=headers, params=params)
        result_page = response.json()
        self.vacancies = result_page['objects']
        while len(result_page['objects']) == 100:
            print(f"Загружено страниц c вакансиями: {params['page']}")
            params['page'] += 1
            response = requests.get(URL, headers=headers, params=params)
            result_page = response.json()
            if result_page.get('objects'):
                self.vacancies.extend(result_page['objects'])
            else:
                break
        print(f"Загружено {len(self.vacancies)}")
        return self.vacancies

        # time.strftime('%d.%m.%Y %H:%M', time.gmtime(1688029859))

        # with open("result.json", "w") as json_file:
        #     json_file.write(json.dumps(self.vacancies, indent=2, ensure_ascii=False))
        # print(len(self.vacancies))