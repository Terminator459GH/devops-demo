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

def analyze_timestamps(lines):
    """УЛУЧШЕННАЯ ВЕРСИЯ: Анализирует временные метки с детализацией"""
    print(f"🔍 DEBUG: Расширенный анализ временных меток в {len(lines)} строках")
    
    import re
    from datetime import datetime
    from collections import Counter
    
    timestamps = []
    date_pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})'
    
    for line in lines:
        match = re.search(date_pattern, line)
        if match:
            try:
                date_str, time_str = match.groups()
                timestamp_str = f"{date_str} {time_str}"
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                timestamps.append(timestamp)
            except ValueError:
                continue
    
    if timestamps:
        earliest = min(timestamps)
        latest = max(timestamps)
        duration = latest - earliest
        
        # НОВОЕ: Анализ по дням
        days = [ts.date() for ts in timestamps]
        day_counts = Counter(days)
        busiest_day, day_count = day_counts.most_common(1)[0]
        
        print(f"📅 РАСШИРЕННЫЙ АНАЛИЗ ВРЕМЕННЫХ МЕТОК:")
        print(f"   Начало: {earliest.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Конец: {latest.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Длительность: {duration}")
        print(f"   Всего записей: {len(timestamps)}")
        print(f"   Самый активный день: {busiest_day} ({day_count} событий)")
        print(f"   Уникальных дней: {len(day_counts)}")
    else:
        print("⚠️  Не найдено временных меток в логах")
    
    return timestamps

def find_busiest_hour(timestamps):
    """Находит самый загруженный час по логам"""
    if not timestamps:
        return None
    
    hours = [ts.hour for ts in timestamps]
    from collections import Counter
    hour_counts = Counter(hours)
    
    busiest_hour, count = hour_counts.most_common(1)[0]
    
    print(f"🏆 Самый загруженный час: {busiest_hour}:00")
    print(f"   Количество событий в этот час: {count}")
    
    return busiest_hour

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

def count_warnings(lines):
    """Подсчитывает количество предупреждений в логах"""
    print(f"🔍 DEBUG: Ищу предупреждения в {len(lines)} строках")
    
    warnings = 0
    for i, line in enumerate(lines, 1):
        line_upper = line.upper()
        if "WARN" in line_upper or "WARNING" in line_upper:
            warnings += 1
            print(f"   ⚠️  Найдено предупреждение в строке {i}: {line.strip()}")
    
    print(f"✅ DEBUG: Найдено предупреждений: {warnings}")
    return warnings

def analyze_error_logs(filename="app.log"):
    """Основная функция анализа логов"""
    print(f"🚀 STARTING: ANALYZE FILE {filename}")
    lines = read_log_file(filename)
    
    if not lines:
        print("⚠️  ВНИМАНИЕ: Файл пуст или не может быть прочитан")
        return {"errors": 0, "warnings": 0, "timestamps": []}
    
    errors = count_errors(lines)
    warnings = count_warnings(lines)
    
    # НОВАЯ ФУНКЦИОНАЛЬНОСТЬ: анализ временных меток
    timestamps = analyze_timestamps(lines)
    if timestamps:
        busiest_hour = find_busiest_hour(timestamps)
    
    print("=" * 50)
    print(f"📊 ИТОГОВАЯ СТАТИСТИКА:")
    print(f"   Всего строк в файле: {len(lines)}")
    print(f"   Ошибок (ERROR): {errors}")
    print(f"   Предупреждений (WARN): {warnings}")
    
    if timestamps:
        print(f"   Записей с временными метками: {len(timestamps)}")
    
    if lines:
        error_percentage = (errors / len(lines)) * 100
        warning_percentage = (warnings / len(lines)) * 100
        print(f"📈 Процент ошибок: {error_percentage:.1f}%")
        print(f"📈 Процент предупреждений: {warning_percentage:.1f}%")
    
    return {
        "errors": errors, 
        "warnings": warnings, 
        "timestamps": timestamps,
        "total_lines": len(lines)
    }


if __name__ == "__main__":
    analyze_error_logs()
