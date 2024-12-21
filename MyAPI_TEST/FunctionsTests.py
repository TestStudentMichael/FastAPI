import requests

# получаем все доступные ISO-коды стран
def get_iso_country_codes():
    url = "https://restcountries.com/v3.1/all"  # Открытый API для получения данных о странах
    response = requests.get(url)
    
    if response.status_code == 200:
        countries_data = response.json()
        country_codes = []
        
        for country in countries_data:
            if 'cca2' in country:  # Проверяем наличие поля с двухбуквенным кодом
                country_codes.append(country['cca2'])
        
        return country_codes
    else:
        print("Ошибка при получении данных")
        return []

# получаем административные единицы выбранной страны
def get_administrative_divisions(country_code):
    # URL к API-сервису
    url = f"https://rawcdn.githack.com/kamikazechaser/administrative-divisions-db/master/api/{country_code}.json"
    
    try:
        # Запрос на получение от API-сервис
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибку

        # Обрабатываем JSON
        divisions = response.json()
        return divisions

    except requests.exceptions.HTTPError as err:
        print(f"Произошла ошибка HTTP: {err}")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

# Работа кода
if __name__ == "__main__":
    '''
    # Запускаем по стране
    country_code = "RU"
    divisions = get_administrative_divisions(country_code)
    print(divisions)
    # Запускаем доступные
    available_countries = get_available_countries()
    print("Доступные страны:", available_countries)
    '''

    country_codes = get_iso_country_codes()
    print("Доступные двухбуквенные коды стран:")
    print(country_codes)