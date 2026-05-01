import flet as ft

def main_page(page: ft.Page):
    hello_text = ft.Text(value='Hello World')
    
    page.add(hello_text)

ft.app(main_page)