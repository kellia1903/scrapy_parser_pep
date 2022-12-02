# Scrapy PEP Parser

## Описание

Учебный проект для практики создания асинхронных парсеров и работы во фреймворке Scrapy.

Парсится список Python Enhancement Proposals (PEP). С каждой страницы PEP парсер собирает номер, название, статус и формирует два файла в формате .csv:
- Список PEP с указанием статуса;
- Сводка по статусам.

## Ключевые технологии и библиотеки:
- [Python](https://www.python.org/);
- [Scrapy](https://pypi.org/project/Scrapy/);

## Установка
1. Склонируйте репозиторий:
```
git clone https://github.com/kellia1903/scrapy_parser_pep.git
```
2. Активируйте venv и установите зависимости:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Проект готов к запуску.

## Управление:

Запуск парсера:
```
scrapy crawl pep
```
После завершения работы парсера файлы с результатами доступны в директории /results:
- pep_YYYY-mm-DDTHH-MM-SS.csv
- status_summary_YYYY-mm-DD_HH-MM-SS.csv

### Автор
Никита Цыбин
