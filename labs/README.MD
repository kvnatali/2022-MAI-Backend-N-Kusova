# Лабораторная работа 1

## Описание

Класс cache содержит словарь:
- **elements** - сами кешируемые элементы `Ключ : Значение`

Словарь в python сам перезаписывает значение, если ключ совпадает, поэтому эту ситуацию специально обрабатывать не нужно.


## Запуск лр 1

Для запуска в виртуальном окружении:
- Активировать виртуальное окружение
- запустить файл main.py
```
source ~/venv/bin/activate
python3 ./git/2022-MAI-Backend-N-Kusova/labs/main.py 
```

Для запуска с командной строки
```
/bin/python3 /home/natali/git/2022-MAI-Backend-N-Kusova/labs/main.py
```

# Лабораторная работа 2

## Домашнее задание №2

- Установить nginx и gunicorn — 2 балла;
- Настроить nginx для отдачи статический файлов из public/ — 2 балла;
- Создать простейшее WSGI-приложение и запустить его с помощью gunicorn — 2 балла;
- Настроить проксирование запросов на nginx — 2 балла;
- Измерить производительность nginx и gunicorn c помощью ab или wrk — 2 балла.

### Шаги реализации

```
source ~/venv/bin/activate
pip install gunicorn
pip freeze > requirements.txt
cat ./sampleApp.py
    def app(environ, start_response):
        data = b"Hi! This is my backend!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
gunicorn --workers 4 sampleApp:app
```
#### Проверка, что работает

Открыть в браузере:

- http://127.0.0.1:8000/ и получить ответ `Hi! This is my backend!`

- http://localhost/data/ и получить ответ `Success! Server block is working!`

- http://localhost/backend/ и получить ответ `Hi! This is my backend!`

- http://localhost/public/image.jpg

### Результаты тестирования производительности
#### Статика
```
wrk -t12 -c400 -d30s http://localhost/public/index.html

Running 30s test @ http://localhost/public/index.html
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    11.69ms    6.90ms 190.44ms   86.08%
    Req/Sec     2.92k   486.64    14.87k    78.13%
  1047929 requests in 30.10s, 394.71MB read
  
Requests/sec:  34815.32
Transfer/sec:     13.11MB
```
#### Gunicorn через nginx
```
wrk -t12 -c400 -d30s http://localhost/backend/

unning 30s test @ http://localhost/backend/
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    80.21ms   22.79ms 290.40ms   84.72%
    Req/Sec   414.58    107.97     0.90k    69.99%
  148633 requests in 30.10s, 25.65MB read
Requests/sec:   4938.79
Transfer/sec:      0.85MB
```
#### Gunicorn напрямую
```
wrk -t12 -c400 -d30s http://localhost:8000

Running 30s test @ http://localhost:8000
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    46.58ms    9.95ms 129.98ms   74.06%
    Req/Sec   711.08    141.99     1.07k    73.61%
  255210 requests in 30.06s, 39.67MB read
Requests/sec:   8489.35
Transfer/sec:      1.32MB
```

# Лабораторная работа 3

## Домашнее задание №3

1. Создать и запустить Django-проект — 2 балла;
2. Реализовать «заглушки» для всех методов API, используя
JsonResponse — 3 баллов:
a. Профиль;
b. Список продуктов;
c. Страница категории;
d. и т.д.
3. В конфиге nginx создать location, которые будет ходить на Djangoприложение — 3 балла;
4. Обрабатывать только нужные методы (GET/POST) — 2 балла.

```
cd /home/natali/git/2022-MAI-Backend-N-Kusova/labs/
Django-admin startproject project
cd ./project
python manage.py migrate
./manage.py startapp shop

python manage.py runserver
```

показать 
- views.py
- settings.py
- urls.py
- my_domain (location на Django приложение)

Обрабатывать только нужные методы: views.py - @require_http_methods(["GET", "POST"])

# Лабораторная работа 4

## Домашнее задание №4

# Лабораторная работа 5

## Домашнее задание №5

# Лабораторная работа 6

## Домашнее задание №6

# Лабораторная работа 7

## Домашнее задание №7

# Лабораторная работа 8

## Домашнее задание №8

# Лабораторная работа 9

## Домашнее задание №9
