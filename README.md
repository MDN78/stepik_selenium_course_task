# Автотест для разных языков интерфейса

## Задание
Вам как разработчику автотестов нужно реализовать решение, которое позволит запускать автотесты для разных языков пользователей, передавая нужный язык в командной строке.

1. Создайте GitHub-репозиторий, в котором будут лежать файлы [conftest.py](https://github.com/MDN78/stepik_selenium_course_task/blob/d42d85db43746439ce909470e83ae8ec34cc88b9/conftest.py) и [test_items.py](https://github.com/MDN78/stepik_selenium_course_task/blob/d42d85db43746439ce909470e83ae8ec34cc88b9/test_items.py).
2. Добавьте в файл `conftest.py` обработчик, который считывает из командной строки параметр `language`.
3. Реализуйте в файле `conftest.py` логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
4. В файл `test_items.py` напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по ссылке:
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/

5. Тест должен запускаться с параметром language следующей командой:
`pytest --language=es test_items.py`
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.

# Что проверяем

1. Тест в репозитории можно запустить командой `pytest --language=es`, тест успешно проходит.
2. Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду `time.sleep(30)` сразу после открытия ссылки. Запустите тест с параметром `--language=fr` и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: `"Ajouter au panier"`.
3. Браузер должен объявляться в фикстуре `browser` и передаваться в тест как параметр.
4. В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы. Есть `assert`.
5. Название тестового метода внутри файла test_items.py соответствует задаче. Название `test_something` не удовлетворяет требованиям.

# Особенности

1. Реализован запуск теста на разных браузерах: `Chrome`, `Firefox`. Каждому браузеру надо установить свой вебдрайвер. Для выбора используется параметр коммандной строки `browser_name`.<br>Например:
`pytest --browser_name=Firefox test_items.py`
2. По умолчанию используются:
- язык - `ru, en`
- браузер - `Chrome`

# Параметры
Пример с параметрами: `pytest -s -v --tb=line test_parser.py`

`--tb=line` - чтобы сократить лог с результатами теста<br>
`-s` - выводить результат работы команды `print()`<br>
`-v` - подробная информация о прохождении тестов
