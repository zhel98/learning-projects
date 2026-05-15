import flet as ft
from db import main_db

def main_page(page: ft.Page):
    page.title = 'ToDo list'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    task_list = ft.Column()
    
    def view_task(task_id, task_text):
        task_field = ft.TextField(value=task_text)
        
        def save_edit(_):
            main_db.upadte_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()
        
        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click = save_edit)
        
        def enable_edit(_):
            if task_field.read_only == True:
                task_field.read_only = False
            else:
                task_field.read_only = True
                
        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click= enable_edit)
        
        return ft.Row([task_field, edit_button,save_button])
    
    def add_task_flet(_):
        if task_input.value:
            task_text = task_input.value.strip()
            task_id = main_db.add_task(task=task_text)
            task_input.value = None
            task_list.controls.append(view_task(task_id = task_id,task_text = task_text))
            page.update()
    
    task_input = ft.TextField(label='введите задачу', on_submit = add_task_flet)
    
    page.add(task_input, task_list)
    

if __name__ == '__main__':
    main_db.init_db()
    ft.app(main_page)