[![Build Status](https://travis-ci.org/zankrus/diploma_worke.svg?branch=master)](https://travis-ci.org/zankrus/diploma_worke)


В качестве тестируемого ресурса используется - демо ресурс банка "Санкт-Петербург"

**URL -** https://idemo.bspb.ru/

СТЭК - Selenium + Pytest
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

После чего нужно выполнить команду в окне PowerShell
```bash
scoop install allure
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
- Донаты кидайте на сбер
