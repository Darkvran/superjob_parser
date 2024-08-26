from SJ_api import SuperJob_API
from dadata_api import Dadata_api
import pandas

def main():
    keywords = input('Введите ключевые слова:\n')

    superjob_data = SuperJob_API(keywords).get_vacancies()

    dadata = Dadata_api()
    dadata.get_companies_info(superjob_data)

    pandas.DataFrame.from_dict(superjob_data).to_excel(F'{keywords}.xlsx', index=False)

if __name__ == '__main__':
    main()