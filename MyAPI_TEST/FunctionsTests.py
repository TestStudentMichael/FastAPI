import requests

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
    country_code = "RU"  # Запускаем по стране
    divisions = get_administrative_divisions(country_code)
    print(divisions)