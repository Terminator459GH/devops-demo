#!/bin/bash
# ВКЛЮЧАЕМ ОТЛАДКУ
set -x  # ← Показывает все команды

python_script="analyze_logs.py"
python_cmd="python3"

echo "🔍 ОТЛАДКА: Начинаю..."
echo "🔍 Файл: $python_script"
echo "🔍 Python: $python_cmd"

if [ ! -f "$python_script" ]; then
    echo "❌ ОШИБКА: Файл не найден"
    echo "📁 Папка: $(pwd)"
    exit 1
fi

echo "🚀 Запускаю..."
$python_cmd "$python_script"
exit_code=$?

echo "📊 Код выхода: $exit_code"

if [ $exit_code -eq 0 ]; then
    echo "✅ Успешно"
    exit 0
else
    echo "❌ Ошибка"
    exit 1
fi