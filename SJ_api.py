import requests
sj_key = 'v3.r.138544739.9e37eb60a99d8d7b6ac373392edf7f89f3c9b853.6cb7d19f919cb3c11852a632b94c5093aead9429'

class SuperJob_API:
    def __init__(self, keywords):
        self.headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': sj_key
        }
        self.params = {
            'keywords': keywords
        }

    def get_vacancies(self):
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', params = self.params, headers = self.headers)
        response_json = response.json()
        vacancies = []
        for vacancy in response_json['objects']:
            vac_title = vacancy.get('profession')
            vac_referrer = vacancy.get('firm_name')
            vac_email = vacancy.get('email')
            vac_phone = vacancy.get('phone')
            vac_ref_site = vacancy.get('url')

            vacancies.append({'Название вакансии': vac_title, 'Название компании': vac_referrer,
                              'Почта компании': vac_email, 'Телефон компании': vac_phone,
                              'Сайт компании': vac_ref_site})

        return vacancies