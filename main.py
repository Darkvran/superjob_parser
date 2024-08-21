from parser import SuperjobParser

def main():
    keywords = input('Введите ключевые слова:\n')

    parser = SuperjobParser(keywords)
    print(parser.vacancy_filtered)

if __name__ == '__main__':
    main()