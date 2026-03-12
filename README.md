# goit-final-project#
# Personal Assistant Bot

CLI-застосунок для керування контактами та нотатками.

## Можливості

- Додавання контактів
- Додавання дня народження
- Перегляд списку контактів
- Створення нотаток
- Перегляд нотаток
- Збереження даних після перезапуску програми

## Встановлення

Клонувати репозиторій:

git clone https://github.com/USERNAME/personal-assistant.git

Перейти в папку проєкту:

cd personal-assistant

Встановити пакет:

pip install .

## Запуск

Запуск через Python:

python3 main.py

або після встановлення пакету:

assistant

## Приклади команд

add-contact Anna 0671234567  
add-birthday Anna 25.12.2000  
all-contacts  

add-note shopping buy milk  
show-notes  

exit

## Структура проєкту

personal-assistant/
│
├── main.py
├── setup.py
├── requirements.txt
├── README.md
│
└── assistant_bot/
    ├── __init__.py
    ├── address_book.py
    ├── notes.py
    ├── storage.py
    ├── utils.py
    └── handlers.py

## Технології

- Python 3
- ООП
- Pickle для збереження даних
- CLI інтерфейс