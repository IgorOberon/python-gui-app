ARCHITECTURE.md
===============

Краткое описание архитектуры проекта на Python + PyQt.

Цель
- Обеспечить устойчивую, тестируемую и расширяемую базу для GUI-приложения.

Структура слоёв (принцип Clean Architecture)
- Domain (сущности и интерфейсы)
  - school_app/domain/entities.py
    - Student: изображение карточки ученика (школа, имя, класс, город).
    - PageInfo: заголовок страницы и HTML-контент.
  - school_app/domain/repository.py
    - ImageRepository: абстрактный интерфейс загрузки изображений.
- Infrastructure (реализации зависимостей и внешних сервисов)
  - school_app/infrastructure/image_loader.py
    - QtImageLoader: реализация ImageRepository через PyQt6 QPixmap.
- Presentation (UI слой)
  - school_app/presentation/styles.py
    - STYLESHEET: стиль оформления приложения (QSS).
  - school_app/presentation/main_window.py
    - MainWindow: сборка главной формы из отдельных компонентов.
  - school_app/presentation/views/
    - header_view.py: заголовок и подзаголовок.
    - student_card_view.py: карточка ученика (с возможностью редактирования). Ввод-вывод реализуются через EditableField.
    - info_panel_view.py: панель с несколькими страницами (StackedWidget).
    - nav_bar_view.py: панель навигации внизу; переключает страницы в info_panel.
  - school_app/presentation/views/editable_field.py
    - EditableField: универсальный виджет для редактируемого поля (метка + значение, режим редактирования).
- Persistence (персистентность данных)
  - school_app/persistence/json_store.py
    - PersistedStudent, load_student, save_student: простой JSON-предикатив для сохранения текущего состояния карточки.

Точка входа
- school_app/main.py: создаёт доменные сущности, инфраструктуру и запускает UI через MainWindow.

Принципы работы и поток данных
- UI слои получают данные через domain/entities и интерфейсы (ImageRepository).
- Реализация загрузки изображения находится в infrastructure и зависит от PyQt.
- Сохранение изменений карточки ученика выполняется через persistence/json_store.py и вызывается из editables_field/StudentCardView.
- Тесты покрывают доменные сущности, базовую инфраструктуру загрузчика изображений и стили/фабрики презентации.

Как это помогает
- Упрощает замену инфраструктурных зависимостей без изменения бизнес-логики.
- Облегчает тестирование доменной логики и компонентов UI без необходимости полного рендера GUI.
