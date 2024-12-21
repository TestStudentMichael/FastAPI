import requests  # Импортируем модуль для работы с HTTP-запросами
from rich.console import Console  # Импортируем класс Console для красивого вывода текста
from rich.table import Table  # Импортируем класс Table для создания таблиц

console = Console()  # Создаем объект класса Console для вывода сообщений

# Функция для получения всех доступных ISO-кодов стран
def get_iso_country_codes():
    url = "https://restcountries.com/v3.1/all"  # URL открытого API для получения данных о странах
    response = requests.get(url)  # Отправляем GET-запрос к указанному URL
    
    if response.status_code == 200:  # Проверяем успешность запроса (статус-код 200 означает успех)
        countries_data = response.json()  # Преобразуем ответ сервера в формат JSON
        country_codes = []  # Создаем пустой список для хранения ISO-кодов стран
        
        for country in countries_data:  # Проходимся по каждому элементу списка стран
            if 'cca2' in country:  # Проверяем наличие ключа 'cca2', который содержит двухбуквенный код страны
                country_codes.append(country['cca2'])  # Добавляем этот код в наш список
        
        return country_codes  # Возвращаем список найденных ISO-кодов
    else:
        console.print("[bold red]Ошибка при получении данных[/]")  # В случае ошибки выводим сообщение красным цветом
        return []  # Возвращаем пустой список

# Функция для получения административных единиц выбранной страны
def get_administrative_divisions(country_code):
    # Формируем URL к API-сервису, подставляя код страны
    url = f"https://rawcdn.githack.com/kamikazechaser/administrative-divisions-db/master/api/{country_code}.json"
    
    try:
        # Отправляем GET-запрос к сформированному URL
        response = requests.get(url)
        response.raise_for_status()  # Проверяем статус ответа; если он не 200, выбрасывается исключение HTTPError
        
        # Преобразуем ответ сервера в формат JSON
        divisions = response.json()
        return divisions  # Возвращаем полученные данные

    except requests.exceptions.HTTPError as err:  # Обработка исключения HTTPError
        console.print(f"[bold red]Произошла ошибка HTTP: {err}[/]")  # Выводим сообщение об ошибке красным цветом
    except Exception as err:  # Обработка других исключений
        console.print(f"[bold red]Произошла ошибка: {err}[/]")  # Выводим сообщение об ошибке красным цветом

# Функция для вывода списка стран с доступными административными единицами
def display_available_countries(available_countries):
    table = Table(title="Страны с доступными административными единицами", show_header=False)  # Создаем таблицу без заголовков
    table.add_column(style="cyan")  # Добавляем колонку с синим стилем текста
    
    for country_code in available_countries:  # Проходимся по списку доступных стран
        table.add_row(country_code)  # Добавляем каждую страну как строку в таблицу
    
    console.print(table)  # Выводим таблицу на экран

# Функция для вывода списка недоступных стран
def display_unavailable_countries(unavailable_countries):
    table = Table(title="Недоступные страны", show_header=False)  # Создаем таблицу без заголовков
    table.add_column(style="red")  # Добавляем колонку с красным стилем текста
    
    for country_code in unavailable_countries:  # Проходимся по списку недоступных стран
        table.add_row(country_code)  # Добавляем каждую страну как строку в таблицу
    
    console.print(table)  # Выводим таблицу на экран

# Функция для вывода списка административных единиц выбранной страны
def display_administrative_units(admin_units):
    table = Table(title=f"Административные единицы для выбранной страны", show_header=True)  # Создаем таблицу с заголовками
    table.add_column("Название", style="green")  # Добавляем колонку с названием и зеленым стилем текста
    
    if isinstance(admin_units, list):  # Проверяем, является ли admin_units списком
        for unit in admin_units:  # Проходимся по каждому административному подразделению
            if isinstance(unit, dict):  # Проверяем, является ли unit словарем
                name = unit.get("name", "")  # Извлекаем название подразделения, если оно есть
                table.add_row(name)  # Добавляем название в строку таблицы
            elif isinstance(unit, str):  # Если unit - строка, просто выводим её
                table.add_row(unit)
    elif isinstance(admin_units, str):  # Если admin_units - строка, выводим её целиком
        table.add_row(admin_units)
    
    console.print(table)  # Выводим таблицу на экран

# Основная логика программы
if __name__ == "__main__":
    country_codes = get_iso_country_codes()  # Получаем список всех доступных ISO-кодов стран
    
    available_countries = []  # Создаем пустой список для доступных стран
    unavailable_countries = []  # Создаем пустой список для недоступных стран

    for code in country_codes:  # Проходимся по каждому полученному коду страны
        divisions = get_administrative_divisions(code)  # Пытаемся получить административные единицы для этой страны
        if divisions is not None and len(divisions) > 0:  # Если административные единицы найдены
            available_countries.append(code)  # Добавляем эту страну в список доступных
        else:
            unavailable_countries.append(code)  # Иначе добавляем ее в список недоступных

    display_available_countries(available_countries)  # Выводим список доступных стран
    display_unavailable_countries(unavailable_countries)  # Выводим список недоступных стран

    while True:  # Бесконечный цикл для выбора страны пользователем
        selected_country = console.input("\nВыберите страну (код): ")  # Спросить у пользователя код страны
        if selected_country in available_countries:  # Если страна доступна
            administrative_units = get_administrative_divisions(selected_country)  # Получаем административные единицы
            display_administrative_units(administrative_units)  # Выводим их на экран
            break  # Прерываем бесконечный цикл
        else:
            console.print(f"\n[bold yellow]Страна '{selected_country}' не найдена среди доступных.[/]\n")  # Сообщаем, что страна недоступна
