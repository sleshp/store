# Магазин одежды


## Описание

Проект представляет собой интернет-магазин одежды, реализованный на Django. Поддерживает:

- Регистрацию и авторизацию пользователей (включая верификацию по email)
- Просмотр и фильтрацию списка товаров
- Добавление товаров в корзину и оформление заказа
- Админ-панель для управления товарами, заказами и пользователями

### Установка и запуск

1. Клонировать репозиторий:  
   ```bash
   git clone https://github.com/sleshp/store.git
   cd store

2. Создать виртуальное окружение и активировать его:
    ```bash
   python -m venv .venv
    # Windows
    .\.venv\Scripts\Activate.ps1
    # macOS/Linux
    source .venv/bin/activate
   
3. Установить зависимости:
    ```bash
   pip install -r requirements.txt

4. Настроить переменные окружения. Создайте файл .env в корне проекта и укажите:
    ```bash
   DB_NAME=имя_бд
   DB_USER=пользователь
   DB_PASSWORD=пароль
   DB_HOST=localhost
   DB_PORT=5432
   
5. Применить миграции и загрузить тестовые данные:
    ```bash
   python manage.py migrate
   python manage.py loaddata products/fixtures/categories.json
   python manage.py loaddata products/fixtures/goods.json
   
6. Запустить сервер:
    ```bash
   python manage.py runserver
