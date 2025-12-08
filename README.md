# DevOps Log Analyzer

Проект для анализа логов приложений с использованием Python и Go.

## Компоненты:

### Python:
- `analyze_logs.py` - анализ лог-файлов
- `app_analyzer.py` - тесты и дополнительные функции

### Go:
- `status_server.go` - HTTP сервер мониторинга
- `status_server_test.go` - unit-тесты

### Bash скрипты:
- `run_analyze.sh` - основной скрипт запуска
- `run_analyze_db.sh` - отладочная версия
- `run_analyze_test.sh` - тестовый скрипт

## Использование:

```bash
# Анализ логов
python analyze_logs.py

# Запуск сервера
go run status_server.go

# Запуск через bash