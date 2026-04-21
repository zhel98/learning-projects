from colorama import Fore, Style, init #импорт библиотеки

# инициализация colorama иначе эта дичь не запускается
init()

# Эта библиотека нужна для изменения цвета текста в консоли для красоты короче

print(Fore.RED + "Кровь")
print(Fore.GREEN + "Светофор")
print(Fore.BLUE + "цвет двух самцов")

# сброс цвета обратно
print(Style.RESET_ALL + "Обычный текст")