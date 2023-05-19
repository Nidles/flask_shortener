# Укорачиватель ссылок
с этим проектом вы сможете укорачивать длинные ссылки для удобного пользования

## Технологии
- Flask
- Flask WTF
- Flask SQLAlchemy

## Установка
1. Скопируйте репозиторий
```text
git clone [link]
```
2. Установите виртуальное окружение внутри папки проекта. Запустите виртуальное окружение
```text
python -m venv venv
Windows: venv\Scripts\activate
GitBash: source venv/Scripts/activate
Linux: source venv/bin/activate
```
3. Установите зависимости
```text
pip install -r requirements.txt
```
4. Добавить файл .env
```text
nano .env

Содержимое файла:
    SECRET_KEY=SECRET_KEY
    DATABASE_URI=sqlite:///db.sqlite3
```
5. Запустите программу
```text
flask --debug run
```
6. Улыбаемся и машем
```text
:)
```