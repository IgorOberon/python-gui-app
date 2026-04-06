# Школьное приложение на PyQt6

GUI-приложение для школы с карточкой ученика и информационными страницами. Построено на Python и PyQt6 с использованием принципов чистой архитектуры (Clean Architecture).

## Возможности

- Карточка ученика с фото, школой, классом и городом
- Навигация по страницам: Главная, О школе, О классе, Обо мне, Увлечения, Мечта
- Тёмная тема оформления
- Поддержка загрузки фото ученика (файл `student.jpg`)

## Требования

- Python 3.10+
- PyQt6

## Установка

1. Установите зависимости:

```bash
pip install PyQt6
```

2. Убедитесь, что Python установлен и доступен в PATH:

```bash
python --version
```

## Запуск

```bash
py school_app/main.py
```

Или через python:

```bash
python school_app/main.py
```

## Добавление фото ученика

Поместите файл `student.jpg` в корневую папку проекта (рядом с `school_app/`). Приложение автоматически загрузит его при запуске.

```
D:\PythonGUIApp/
├── student.jpg          <-- положите фото сюда
└── school_app/
```

## Структура проекта

```
school_app/
├── main.py                  # Точка входа
├── domain/                  # Слой домена (бизнес-логика)
│   ├── entities.py          # Student, PageInfo
│   └── repository.py        # ImageRepository (интерфейс)
├── infrastructure/          # Слой инфраструктуры
│   └── image_loader.py      # QtImageLoader (реализация)
└── presentation/            # Слой представления
    ├── styles.py            # QSS стили
    ├── main_window.py       # MainWindow (композиция)
    └── views/
        ├── header_view.py       # Заголовок
        ├── student_card_view.py # Карточка ученика
        ├── info_panel_view.py   # Информационная панель
        └── nav_bar_view.py      # Навигация
```

## Архитектура

Проект разделён на три слоя по принципам Clean Architecture:

- **Domain** — сущности (`Student`, `PageInfo`) и интерфейсы (`ImageRepository`). Не зависит от внешних библиотек.
- **Infrastructure** — реализации интерфейсов (`QtImageLoader`). Зависит от domain.
- **Presentation** — UI-компоненты PyQt6. Зависит от domain и infrastructure через интерфейсы.

Зависимости направлены только внутрь: presentation → domain, infrastructure → domain. Domain ничего не знает о внешних слоях.
