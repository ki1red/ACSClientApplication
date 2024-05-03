import subprocess
import time
import tkinter as tk
import threading

rtmp_url = "rtmp://localhost:1935/live/stream"

# Функция для закрытия окна Tkinter
def close_window():
    root.destroy()

# Функция для отображения окна Tkinter с изображением
def display_image():
    global root
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Отображаем окно на весь экран
    root.configure(bg='black')  # Устанавливаем черный фон окна
    # Запускаем цикл Tkinter
    root.mainloop()

# Запускаем отображение окна с изображением в отдельном потоке
display_thread = threading.Thread(target=display_image)
display_thread.start()

while True:
    try:
        # Запускаем ffplay для воспроизведения основного RTMP потока на весь экран
        process = subprocess.Popen(['ffplay', '-fs', '-autoexit', rtmp_url], stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Error: Failed to play RTMP stream. Playing alternative video...")
        
    except Exception as e:
        print(f"Error occurred: {e}")

    # Ждем перед следующей попыткой подключения
    time.sleep(0.5)
