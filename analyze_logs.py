def read_log_file(log_file):
    """Читает лог-файл и возвращает список строк"""
    print(f"🔍 DEBUG: Пытаюсь прочитать файл: {log_file}")
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"✅ DEBUG: Успешно прочитано строк: {len(lines)}")
        return lines
    except FileNotFoundError:
        print(f"❌ ERROR: Файл {log_file} не найден!")
        return []
    except UnicodeDecodeError:
        print(f"❌ ERROR: Проблема с кодировкой файла {log_file}")
        return []
    except Exception as e:
        print(f"❌ ERROR: Неожиданная ошибка при чтении файла: {e}")
        return []


def count_errors(lines):
    """Подсчитывает количество строк с ошибками"""
    print(f"🔍 DEBUG: Анализирую {len(lines)} строк")
    
    # Улучшим поиск ошибок
    errors = 0
    for i, line in enumerate(lines, 1):
        if "ERROR" in line.upper():
            errors += 1
            print(f"   Найдена ошибка в строке {i}: {line.strip()}")
    
    print(f"✅ DEBUG: Найдено ошибок: {errors}")
    return errors


def analyze_error_logs(log_file="app.log"):
    """Основная функция анализа логов"""
    print(f"🚀 ЗАПУСК: Анализ файла {log_file}")
    
    lines = read_log_file(log_file)
    
    if not lines:
        print("⚠️  ВНИМАНИЕ: Файл пуст или не может быть прочитан")
        return 0
    
    errors = count_errors(lines)
    print(f"📊 ИТОГ: Всего ошибок найдено: {errors}")
    
    # Добавим простую статистику
    if lines:
        error_percentage = (errors / len(lines)) * 100
        print(f"📈 Процент ошибок: {error_percentage:.1f}%")
    
    return errors


if __name__ == "__main__":
    analyze_error_logs()
