import requests
from bs4 import BeautifulSoup


class SuperjobParser:

    def __init__(self, keywords):
        self.page = requests.get(f'https://www.superjob.ru/vacancy/search/?keywords={keywords}')
        soup = BeautifulSoup(self.page.text, "html.parser")
        self.vacancies = soup.findAll('div', class_='f-test-search-result-item')
        self.vacancy_filtered = {}

        for data in self.vacancies:
            if data.find('a', class_='EWWny') is not None and data.find('a', class_='XHlOg') is not None:
                vacancy_name = data.find('a', class_='EWWny').text
                vacancy_referrer = data.find('a', class_='XHlOg').text
                company_page_url = F"https://www.superjob.ru{data.find('a', class_='XHlOg').get('href')[:-5]}/about.html"

                company_page = requests.get(company_page_url)
                company_page_soup = BeautifulSoup(company_page.text, "html.parser")
                if company_page_soup.find('a', class_='pGi4i') is not None:
                    company_site_url = company_page_soup.find('a', class_='pGi4i').get('href')
                else:
                    company_site_url = '-'

                self.vacancy_filtered[vacancy_name] = {'vacancy_referrer': vacancy_referrer, 'company_page_url':company_page_url, 'company_site_url':company_site_url}


#class="EruXX pGi4i f-test-link-www_sogaz_ru _1+j9e" - sogaz
# class="fGJmW hI4F1" - ВТБ




