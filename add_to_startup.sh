#!/bin/bash

# Переменная для пути к директории, содержащей скрипт
script_dir=$(dirname "$(realpath "$0")")

# Путь к скрипту, который нужно добавить в автозагрузку
script_path="$script_dir/acsclientapplication.py"

# Проверяем, существует ли файл acsclientapplication.py
if [ ! -f "$script_path" ]; then
    echo "Error: acsclientapplication.py not found in the same directory as this script."
    exit 1
fi

# Добавляем скрипт в автозагрузку
echo "Adding $script_path to autostart..."
echo "[Desktop Entry]
Type=Application
Name=ACSClientApplication
Exec=python3 $script_path
Terminal=false
X-GNOME-Autostart-enabled=true
" > ~/.config/autostart/acsclientapplication.desktop

echo "Script added to autostart successfully."
