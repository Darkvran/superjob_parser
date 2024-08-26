from dadata import Dadata

token = "e983f48127a55e4f4ffe9b521f2fefa1156b7730"
class Dadata_api:
    def __init__(self):
        self.dadata = Dadata(token)


    def get_companies_info(self, sj_data):
        for vac in sj_data:
            result = self.dadata.suggest("party", f"{vac['Название компании']}")
            if len(result) != 0:
                vac['ИНН'] = result[0].get('data').get('inn')
                vac['ЛПР'] = result[0].get('data').get('management')