from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализация браузера
browser = webdriver.Firefox()

try:
    # Открываем страницу с потолочными светильниками
    browser.get("https://www.divan.ru/category/potolocnye-svetilniki")

    # Даем странице время для загрузки
    time.sleep(5)

    # Находим все элементы светильников
    ligths = browser.find_elements(By.CSS_SELECTOR, 'div.wYUX2')

    # Открываем файл для записи данных
    with open("ligths.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Записываем первую строку с заголовками
        writer.writerow(['название', 'цена', 'ссылка'])

        # Перебираем найденные светильники и извлекаем информацию
        for ligth in ligths:
            try:
                name = ligth.find_element(By.CSS_SELECTOR, 'div.wYUX2 span').text
            except Exception as e:
                print(f"Ошибка при получении названия: {e}")
                name = "Не удалось получить название"

            try:
                price = ligth.find_element(By.CSS_SELECTOR, 'div.q5Uds.fxA6s span').text
            except Exception as e:
                print(f"Ошибка при получении цены: {e}")
                price = "Не удалось получить цену"

            try:
                url = ligth.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            except Exception as e:
                print(f"Ошибка при получении ссылки: {e}")
                url = "Не удалось получить ссылку"

            # Записываем данные в CSV
            writer.writerow([name, price, url])

            # Выводим результаты в консоль
            print({
                'name': name,
                'price': price,
                'url': url
            })

finally:
    # Закрываем браузер после завершения работы
    browser.quit()
