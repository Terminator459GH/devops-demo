# app_analyzer.py - ДЛЯ TEST EXPLORER
import unittest


class TestAnalyzeLogs(unittest.TestCase):
    """Простой тест для Test Explorer"""

    def test_count_errors(self):
        """Тестируем подсчёт ошибок"""
        # Импортируем твою функцию
        from analyze_logs import count_errors

        # Тест 1
        test_lines = ["ERROR: test", "INFO: ok", "ERROR: another"]
        result = count_errors(test_lines)
        self.assertEqual(result, 2, "Должно быть 2 ошибки")

    def test_empty_list(self):
        """Тест пустого списка"""
        from analyze_logs import count_errors
        result = count_errors([])
        self.assertEqual(result, 0, "Пустой список = 0 ошибок")


if __name__ == '__main__':
    # Запуск тестов
    unittest.main()
