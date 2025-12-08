def read_log_file(log_file):
    print(f"🔍 DEBUG: Пытаюсь прочитать файл: {log_file}")  # ← Добавить
    try:
        with open(log_file, "r") as f:
            lines = f.readlines()
            # ← Добавить
            print(f"✅ DEBUG: Успешно прочитано строк: {len(lines)}")
            return lines
    except FileNotFoundError:
        print(f"❌ ERROR: Файл {log_file} не найден!")
        return []


def count_errors(lines):
    print(f"🔍 DEBUG: Анализирую {len(lines)} строк")  # ← Добавить
    errors = sum(1 for line in lines if "ERROR" in line)
    print(f"✅ DEBUG: Найдено ошибок: {errors}")  # ← Добавить
    return errors


def analyze_error_logs(log_file="app.log"):
    print(f"🚀 ЗАПУСК: Анализ файла {log_file}")  # ← Добавить
    lines = read_log_file(log_file)
    errors = count_errors(lines)
    print(f"📊 ИТОГ: Total errors found: {errors}")
    return errors


if __name__ == "__main__":
    analyze_error_logs()
