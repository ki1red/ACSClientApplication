import subprocess
import time
import tkinter as tk
import threading
from PIL import Image, ImageTk

rtmp_url = "rtmp://localhost:1935/live/stream"
image_path = "default.jpg"

# Функция для закрытия окна Tkinter
def close_window():
    root.destroy()

# Функция для отображения окна Tkinter с изображением
def display_image():
    global root, label
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Отображаем окно на весь экран
    root.configure(bg='black')  # Устанавливаем черный фон окна

    img = Image.open(image_path)
    img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

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
