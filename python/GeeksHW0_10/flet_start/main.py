import flet as ft

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    hello_text = ft.Text(value='Hello World')

    
    def on_button_click(_):
        # print(name_input.value)
        # print(f'{_}')
        name = name_input.value.strip()
        
        if name:
            hello_text.color= None
            hello_text.value= f'Hello {name}'
            name_input.value = None
            # print(name)
        else:
            # print("Error")
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
    name_input = ft.TextField(max_length=5, label='ты пидор', on_submit=on_button_click)
    elevated_button = ft.ElevatedButton(text = 'SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    # text_button = ft.TextButton(text='SEND', icon=ft.Icons.SEND)
    # icon_button = ft.IconButton(icon=ft.Icons.SEND) #не прнимает текст в отличии от своих соседей
    
    page.add(hello_text, name_input, elevated_button, change_theme_button)




ft.app(main_page)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)