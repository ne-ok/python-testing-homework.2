# Автоматизация тестирования с GitHub Actions

Проект демонстрирует настройку CI/CD с использованием GitHub Actions для автоматического тестирования функции вычисления среднего арифметического **с округлением в меньшую степень до целого числа**.


## 1. Структура репозитория
python-testing-homework.2
- 'github/workflows/tests.yml' # Конфигурация GitHub Actions
- 'main.py' # Реализация функции average()
- 'test_main_unit.py' # Тесты на unittest
- 'test_main_pytest.py' # Тесты на pytest
- 'github_actions.md' # Ответы на теоретические вопросы из 1 и 3 частей
- 'README.md' # Данный файл
- 'остальные файлы/' # Папка с файлами, оставшимися после прошлой лабораторной
- 
## 2. Тестирование
- **Unittest:**
  python -m unittest test_main_unit.py
- **Pytest:**
  pytest test_main_pytest.py -v
