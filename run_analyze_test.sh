#!/bin/bash
# test_run_analyze.sh - тестирует run_analyze.sh

echo "🧪 ТЕСТИРУЮ run_analyze.sh"
echo "=========================="

# Создаём временную папку для тестов
TEST_DIR="test_temp_$(date +%s)"
mkdir "$TEST_DIR"
cd "$TEST_DIR" || exit 1

echo "1. Тест: Файл analyze_logs.py отсутствует"
echo "-----------------------------------------"
../run_analyze.sh
EXIT_CODE=$?
if [ $EXIT_CODE -eq 1 ]; then
    echo "✅ PASS: Корректно сообщил об ошибке"
else
    echo "❌ FAIL: Должен вернуть код 1, вернул $EXIT_CODE"
fi
echo ""

echo "2. Тест: Файл analyze_logs.py существует и работает"
echo "---------------------------------------------------"
cat > analyze_logs.py << 'EOF'
#!/usr/bin/env python3
print("✅ Python скрипт работает")
EOF

../run_analyze.sh
EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ PASS: Скрипт выполнился успешно"
else
    echo "❌ FAIL: Должен вернуть код 0, вернул $EXIT_CODE"
fi
echo ""

echo "3. Тест: Python скрипт с ошибкой"
echo "--------------------------------"
cat > analyze_logs.py << 'EOF'
#!/usr/bin/env python3
import sys
print("Начинаю...")
sys.exit(1)  # Имитируем ошибку
EOF

../run_analyze.sh
EXIT_CODE=$?
if [ $EXIT_CODE -eq 1 ]; then
    echo "✅ PASS: Корректно обработал ошибку Python"
else
    echo "❌ FAIL: Должен вернуть код 1, вернул $EXIT_CODE"
fi

# Возвращаемся и чистим
cd ..
rm -rf "$TEST_DIR"

echo ""
echo "=========================="
echo "✅ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО"