# Changelog

## 1.1.1 (2026-04-07)
- Fix: ensure both text fields (school, name, grade, city) and photo_path are persisted together in student_data.json.
- Load persisted photo on startup in UI and save photo paths when a new photo is uploaded.

## 1.1.0 (2026-04-06)
- Реализация фичи редактирования карточки ученика в UI. Поля: Школа, Учениk, Класс, Город можно редактировать напрямую. Изменения сохраняются в JSON-файл student_data.json в корне проекта.
- Добавлен модуль Persisted JSON Store (school_app/persistence/json_store.py) и интеграция в UI через EditableField (school_app/presentation/views/editable_field.py).
- Обновлены карточки ученика: теперь поддерживают inline-редактирование и сохранение данных.
- Добавлены новые тесты: тест загрузки реального изображения через QtImageLoader (tests/test_image_loader_load_existing.py).
