# Пример проекта автотестов для магазина [HOMMY](https://myhommy.ru/)
###  Используемые технологии
<p align="center">
  <code><img src="resources/logo/python.svg" width="40" height="40"  alt="A-d-am" title="Python"></code>
  <code><img src="resources/logo/pytest.png" width="40" height="40"  alt="A-d-am" title="PyTest"></code>
  <code><img src="resources/logo/selene.png" width="40" height="40"  alt="A-d-am" title="Selene"></code>
  <code><img src="resources/logo/pycharm.png" width="40" height="40"  alt="A-d-am" title="PyCharm"></code>
  <code><img src="resources/logo/Jenkins.svg" width="40" height="40"  alt="A-d-am" title="Jenkins"></code>
  <code><img src="resources/logo/Selenoid.svg" width="40" height="40"  alt="A-d-am" title="Selenoid"></code>
  <code><img src="resources/logo/Allure_new.png" width="40" height="40"  alt="A-d-am" title="Allure Report"></code>
  <code><img src="resources/logo/allure_testops.png" width="40" height="40"  alt="A-d-am" title="Allure TestOps"></code>
</p>

## Покрываемый функционал
- Авторизация пользователя 
- Поиск товара в каталоге
- Добавление товаров в корзину
- Добавление товаров в Избранное

## Запуск тестов
#### Все API тесты можно запустить как удалённо (Jenkins), так и локально

### Локально
Важно! Перед запуском нужно создать файл .env и указать там selenoid_login 
и selenoid_password

Для запуска тестов локально, нужно выполнить следующие шаги
1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в териминале следующие команды
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
context=web pytest -m web  
```

### С помощью [Jenkins](https://jenkins.autotests.cloud/job/QA_guru_diploma_UI_HOMMY/)
#### Для запуска автотестов необходимо:
 - Открыть [джобу](https://jenkins.autotests.cloud/job/QA_guru_diploma_UI_HOMMY/) в jenkins
 - Нажать на Build
<img src="resources/screenshots/Jenkins_build.png">

## Отчет о прохождении тестов (Allure)

### Локально
Для получения отчета нужно:
 - Запустить тесты
 - Ввести команду 
```
allure serve allure-results
```
Ниже представлен пример allure отчета 
<img src="resources/screenshots/allure_report_example_api.png">

### Если тесты запускались в Jenkins

Для получения отчета нужно нажать на иконку allure report'a в строке билда 
<img src="resources/screenshots/jenkins_allure_report.jpg">
У него будет точно такой же формат, как и при получении локально
<img src="tests/images/screenshots/allure_report_example_api.png">

### В проекте реализована интеграция с Allure TestsOps
<img src="resources/screenshots/allure_test_ops.png">
