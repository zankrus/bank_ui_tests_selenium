[![Build Status](https://travis-ci.org/zankrus/diploma_worke.svg?branch=master)](https://travis-ci.org/zankrus/diploma_worke)


В качестве тестируемого ресурса используется - демо ресурс банка "Санкт-Петербург"

**URL -** https://idemo.bspb.ru/

СТЭК - Selenium WebDriver + Pytest.

## Установка

Используйте  [pip](https://pip.pypa.io/en/stable/) для установки зависимостей проекта. Рекомендуется использовать
виртуальное окружение

```bash
pip install -r requirements.txt
```
## Запуск тестов
1)Содайте и активируйте виртульное окружение

```bash
pip install virtualenv 
```

2)Активируйте вирутальное окружение
```bash
virtualenv <env_name>
<env_name>\Scripts\activate.bat
```

3)Запустите pytest для запуска всех тестов(*флаг **--headless** для режиме без GUI*)
```bash
pytest
```
4)Для запуска конкретного теста из файла :
```bash
pytest <filename>::<testclassname>::<testname>
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
