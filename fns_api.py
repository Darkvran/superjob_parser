import requests

def get_company_info_by_name(company_name):
    params = {
        "q": company_name,
        "key": '12e6d3e2bfa55300cb5dd8b0d501e8fd2930130f'
    }
    response = requests.get("https://api-fns.ru/api/search", params=params)

    if response.status_code == 200:
        data = response.json()

        if data.get('items'):
            company_data = data['items'][0]
            inn = company_data.get('ЮЛ').get('ИНН')
            address = company_data.get('ЮЛ').get('АдресПолн')

            return {
                "ИНН": inn,
                "Адрес": address
            }
        else:
            print(F"Компания {company_name} не найдена.")
            return None
    else:
        print(f"Ошибка запроса: {response.status_code}")
        return None



