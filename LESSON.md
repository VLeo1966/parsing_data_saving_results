Вот отформатированный текст в формате Markdown:

# Теория на сегодня

## 1. Очистка, преобразование, фильтрация данных

Сегодня заключительный урок по теме парсинга. Мы научились получать информацию, теперь нам нужно научиться её сохранять и обрабатывать, чтобы потом использовать.

Сегодня мы:

- научимся обрабатывать данные;
- рассмотрим различные методы сохранения данных;
- поймём, когда и какие форматы хранения данных использовать.

Когда мы парсим данные с различных веб-страниц, мы часто получаем сырые данные, которые неудобно (или вообще нельзя) использовать и которые нуждаются в обработке.

### В обработку входят:

- **Очистка данных** — удаление лишних пробелов, специальных символов, лишней информации, исправление некорректных, повреждённых данных и т.д. Когда мы регулируем парсинг, лишней информации может почти не быть.
- **Преобразование данных** — перевод строк в числа и т.п.
- **Фильтрация данных** — отбор только нужных случаев.

### Проделываем очистку данных:

Пишем простой парсер. В итоге мы получим коллекцию со всеми рядами таблицы.

```python
import requests
from bs4 import BeautifulSoup

url = "https://"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all("tr")
# tr - каждый ряд таблицы
# td - каждая ячейка внутри ряда таблицы
data = []
```

Теперь нам нужно перебрать коллекцию. Используем цикл `for`:

```python
for row in rows:
    cols = row.find_all("td")
    # Используем укороченный вариант цикла for
    # Для удаления пробелов и других лишних символов используем функцию strip
    cleaned_cols = [col.text.strip() for col in cols]
    # Чтобы удалить пробелы, оставляем ()
    # Чтобы удалить какие-то символы из начала и конца, пишем ('то-что-надо-удалить')
    data.append(cleaned_cols)
    # Функция append добавляет в список.
print(data)
```

Также можно удалять символы из списка при помощи метода `pop` и других.

### Преобразуем данные (цены)

Представим, что мы уже достали информацию из списков, и теперь у нас два списка, которые находятся внутри друг друга (вложенные списки, двумерные массивы).

```python
data = [
    ['100', '200', '300'],
    ['400', '500', '600']
]
# С сайта мы получаем именно списки.
numbers = []
```

Используем функции `float` или `int`, чтобы преобразовать данные:

```python
for row in data:
    for text in row:
        number = int(text)
        numbers.append(number)
print(numbers)
```

Чаще всего преобразования — это просто преобразование одного типа данных в другой.

### Отфильтруем данные

Отфильтруем данные — это можно делать через обычные условия. У нас также есть двумерный список, содержащий другие списки.

```python
data = [
    [100, 110, 120],
    [400, 500, 600],
    [150, 130, 140]
]
filtered_list = []
```

Используем цикл `for` и условие:

```python
for row in data:
    for item in row:
        if item > 190:
            filtered_list.append(item)
print(filtered_list)
```

## 2. Сохранение данных

После обработки данных их необходимо сохранить для дальнейшего анализа или использования.

Существует множество методов и форматов для сохранения данных, каждый из которых имеет свои преимущества и недостатки.

### Форматы:

- **txt** — текстовый формат.
- **csv (Comma-Separated Values)** — также текстовый формат; один из наиболее простых и распространённых форматов для хранения табличных данных. В нём мы можем сохранить самые простые структуры (например, таблицу из двух столбцов: имя пользователя, телефон пользователя). Нельзя загрузить большие объёмы данных. Можем легко читать этот формат. Формат совместим, открывается через текстовые редакторы или Excel.
- **json (JavaScript Object Notation)** — формат, удобный для передачи данных между сервером и клиентом. Формат похож на словари в Python, удобен для работы со сложными структурами (вложенные объекты, вложенные массивы). Также удобен для чтения человеком.
- **База данных SQLite** — легковесная база данных, удобно для небольших объёмов данных, можно посылать такой базе запросы, базу можно масштабировать.
- **Электронные таблицы** (например, Google Sheets) — удобны для визуализации данных и выполнения расчётов. Основное удобство в том, что мы можем иметь доступ к этим таблицам с различных устройств.

## 3. Разрабатываем программу

Результаты урока

Разрабатываем программу с учётом всего того, что мы изучили. Мы будем парсить данные с сайта [https://tomsk.hh.ru/vacancies/programmist](https://tomsk.hh.ru/vacancies/programmist) и сохранять их в CSV-файл.

### Пример программы:

```python
# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Firefox()
# Если мы используем Chrome, пишем
# driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://tomsk.hh.ru/vacancies/programmist"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)

# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')

# Выводим вакансии на экран
print(vacancies)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for vacancy in vacancies:
    try:
        # Находим элементы внутри вакансий по значению
        # Находим названия вакансии  
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        # Находим названия компаний
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
        # Находим зарплаты
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        # Находим ссылку с помощью атрибута 'href'
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except:
        print("Произошла ошибка при парсинге")
        continue

    # Вносим найденную информацию в список
    parsed_data.append([title, company, salary, link])

# Закрываем подключение браузера
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])

    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)
```

Чтобы удобнее просмотреть результат, открываем файл через программу для чтения и редактирования таблиц.

## 4. Результаты урока

Сегодня мы:

- изучили обработку данных;
- рассмотрели различные методы сохранения данных;
- поняли, когда и какие форматы использовать.

## Время выполнить задание

Попробуйте спарсить данные с сайта [divan.ru](https://divan.ru), как в прошлом домашнем задании (можно использовать либо Scrapy, либо Selenium), но теперь ещё и сохраните информацию в CSV-файл.

К ДЗ прикрепляем ссылку на репозиторий с файлом CSV и кодом.
```

Этот