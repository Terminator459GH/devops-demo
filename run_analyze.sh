#!/bin/bash
python_script="analyze_logs.py"
python_cmd="python3"

if [ ! -f "$python_script" ]; then
    echo "Error: $python_script not found"
    exit 1
fi

echo "Running $python_script..."
$python_cmd "$python_script"

if [ $? -eq 0 ]; then
    echo "Python скрипт выполнен успешно"
    exit 0
else
    echo "Ошибка при выполнении Python скрипта"
    exit 1
fi