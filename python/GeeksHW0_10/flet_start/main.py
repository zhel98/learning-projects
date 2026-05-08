import flet as ft
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    hello_text = ft.Text(value='Hello World')
    greeting_history=[]
    history_text = ft.Text(value='история приветствий:')
    favorite_history = []
    fav_names = ft.Text(value='любимки:')
    
    def on_button_click(_):
        # print(name_input.value)
        # print(f'{_}')
        name = name_input.value.strip()
        current_time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        print(f"{current_time} - Привет, {name}!")
        
        if name:
            hello_text.color= None
            hello_text.value= f'Hello {name}'
            name_input.value = None
            greeting_history.append(name)
            if len(greeting_history) > 5:
                greeting_history.pop(0)
            print(greeting_history)
            history_text.value = 'история изменений: \n-' + '\n-' .join(greeting_history)
        else:
            hello_text.value = 'Ошибка введите имя'
            hello_text.color = ft.Colors.RED
        page.update()
        
    def change_them(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()
        
    change_theme_button = ft.IconButton(ft.Icons.BRIGHTNESS_6, on_click=change_them)
    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    # text_button = ft.TextButton(text='SEND', icon=ft.Icons.SEND)
    # icon_button = ft.IconButton(icon=ft.Icons.SEND) #не прнимает текст в отличии от своих соседей
    
    def clear_history(_):
        greeting_history.clear()
        favorite_history.clear()
        history_text.value = 'история приветствий: '
        fav_names.value = 'любимки: '
        page.update()
    
    clear_button = ft.IconButton(icon=ft.Icons.CLEAR, on_click = clear_history)
    
    def fav_history(_):
      if greeting_history:
          last_name = greeting_history[-1] 
          if last_name not in favorite_history:
              favorite_history.append(last_name)
          fav_names.value = 'любимки: \n-' + '\n-' .join(favorite_history)
      page.update()
      
    fav_button = ft.IconButton(icon=ft.Icons.FAVORITE, on_click = fav_history)
    
    
    page.add(hello_text, name_input,ft.Row([elevated_button, change_theme_button, fav_button, clear_button]), history_text, fav_names)




ft.app(main_page)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)