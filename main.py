import bar_plot
import pie_plot

import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD


# Проверка условий входящей последовательности
def is_valid_sequence(text):
    valid_chars = set('ATGC')
    lines = text
    if not lines:
        return False              # Пустой текст

    reference_length = len(lines[0])

    for line in lines:
        if len(line) != reference_length:
            return False
        if not all(char in valid_chars for char in line):
            return False

    return True


# Работа с файлом при перетаскивании
def on_drop(event):
    file = event.data
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            lines = f.readlines()
            global seqs
            seqs = []
            for line in lines:
                seqs.append(line.strip())           # Сразу передаем список из последовательностей
        if is_valid_sequence(seqs):
            text_widget.delete('1.0', tk.END)  # Очищаем текстовое поле
            text_widget.insert('1.0', '\n'.join(seqs))  # Вставляем содержимое файла
            open_file_window()
        else:
            show_error_message()


# Открытие файла
def open_file_window():
    file_window = tk.Toplevel(root)
    file_window.title('Выбор действия')
    file_window.geometry('200x150')

    label = tk.Label(file_window, text='Какой график нарисовать?')

    button1 = tk.Button(file_window, text='Столбики', command=action1, width=10, height=3)
    button1.pack(side='left', padx=10)

    button2 = tk.Button(file_window, text='Пирожок', command=action2, width=10, height=3)
    button2.pack(side='right', padx=10)


# Ошибка при несоблюдении условий
def show_error_message():
    error_window = tk.Toplevel(root)
    error_window.title('Ошибка')
    error_window.geometry('300x100')
    error_label = tk.Label(error_window, text='Ошибка: неверный формат данных')
    error_label.pack()
    error_button = tk.Button(error_window, text='Попробовать снова', command=error_window.destroy)
    error_button.pack()


def action1():
    bar_plot.paint_plot(seqs)


def action2():
    pie_plot.paint_plot(seqs)




if __name__ == '__main__':
    root = TkinterDnD.Tk()
    root.title('Перетащите текстовый файл')

    text_widget = tk.Text(root)
    text_widget.pack(fill='both', expand=True)

    text_widget.drop_target_register(DND_FILES)
    text_widget.dnd_bind('<<Drop>>', on_drop)

    root.mainloop()

# Скомпилить в exe'шнки не смог. Pyinstaller'у tkndnd не нравился. Мб из-за 12 версии питона.
# Но если запустить сам скрипт, то будет красиво.
# Остальные два модула можно запустить самостоятельно.