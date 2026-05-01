import flet as ft

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    hello_text = ft.Text(value='Hello World')

    name_input = ft.TextField(max_length=5, label='ты пидор')
    
    page.add(hello_text, name_input)


ft.app(main_page)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)