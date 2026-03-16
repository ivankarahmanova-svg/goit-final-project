# Personal Assistant Bot

CLI застосунок для керування контактами та нотатками.

## Опис

Personal Assistant Bot — це консольний застосунок на Python, який дозволяє зберігати контакти та нотатки.  
Програма працює через командний рядок і зберігає всі дані у файл, тому після перезапуску застосунку інформація не втрачається.

Застосунок реалізований з використанням об'єктно-орієнтованого програмування та модульної структури проєкту.

---

## Основні можливості

### Робота з контактами

- додавання нового контакту
- додавання телефону
- редагування телефону
- видалення контакту
- додавання дня народження
- перегляд дня народження
- додавання email
- перегляд email
- перегляд усіх контактів
- пошук контактів за ім'ям

### Робота з нотатками

- створення нотатки
- редагування нотатки
- видалення нотатки
- перегляд усіх нотаток
- пошук нотатки за назвою
- додавання тегів
- пошук нотаток за тегом
- сортування нотаток за тегами

## Основні команди

Contacts:
add <name> <phone>
change <name> <old_phone> <new_phone>
phone <name>
all
search <name>
delete contact <name>
add birthday <name> <DD.MM.YYYY>
show birthday <name>
birthdays
add email <name> <email>
show email <name>

Notes:
add note <title> <content>
edit note <title> <new content>
delete note <title>
show notes
find note <title>
add tag <title> <tag>
find tag <tag>
sort notes


## Встановлення і запуск

```bash
git clone https://github.com/ivankarahmanova-svg/goit-final-project.git
cd goit-final-project
pip install -r requirements.txt
pip install .
python3 main.py