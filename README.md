[![Build Status](https://travis-ci.org/zankrus/diploma_worke.svg?branch=master)](https://travis-ci.org/zankrus/diploma_worke)

# Дипломный проект 
Хей йоу, куэй братишки. А теперь официальная часть:

В качестве тестируемого ресурса используется - демо ресурс банка "Санкт-Петербург"

**URL -** https://idemo.bspb.ru/
## Установка

Используйте  [pip](https://pip.pypa.io/en/stable/) для установки зависимостей проекта. Рекомендуется использовать  
виртуальное окружение

```bash
pip install -r requirements.txt
```
## Запуск
1)Содайте и активируйте виртульное окружение

2)Запустите pytest для запуска всех тестов(*флаг **--headless** для режиме без GUI*)
```bash
virtualenv <env_name>
<env_name>\Scripts\activate.bat
pytest
```
## Allure
Установка allure
Для генерации отчетов необходимо установить Scoop через PowerShell https://scoop.sh/

После чего нужно выполнить команду
```bash
scoop install allure
в окне PowerShell
```

Генерация отчетов
После прохождения тестов сформируется папка allure_result в корневой директории проекта

Для генерации отчета необходимо ввести команду в командной строке
```bash
allure serve {allure_dir}
```
## Контакты

- Telegram @ro_whale 
- [vk.com/ro_whale](https://vk.com/ro_whale)
