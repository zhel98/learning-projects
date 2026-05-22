import flet as ft
from db import main_db

def main_page(page: ft.Page):
    page.title = 'ToDo list'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    task_list = ft.Column(spacing=10,scroll=ft.ScrollMode.AUTO, expand=True)
    
    filter_type = 'all'
    
    def load_tasks():
        task_list.controls.clear()
        for task_id, task, completed in main_db.get_tasks(filter_type):
            task_list.controls.append(view_task(task_id=task_id, task_text=task, completed=completed))
            page.update()
            
    
    def view_task(task_id, task_text, completed = None):
        task_field = ft.TextField(value=task_text, expand=True)

        checkbox = ft.Checkbox(value=bool(completed), on_change = lambda e: toggle_task(task_id=task_id, is_completed=e.control.value))
        
        def save_edit(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()
        
        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click = save_edit)
        
        def enable_edit(_):
            if task_field.read_only == True:
                task_field.read_only = False
            else:
                task_field.read_only = True
                
        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click= enable_edit)
        
        
        def delete_existing_task(_):
            main_db.delete_task(task_id)
            task_list.controls.remove(_.control.parent)
            page.update()
        
        delete_button = ft.IconButton(icon= ft.Icons.DELETE, style=ft.ButtonStyle(bgcolor=ft.Colors.RED), on_click = delete_existing_task)
            
        
        return ft.Row([checkbox, task_field, edit_button,save_button, delete_button])
    
    def toggle_task(task_id, is_completed):
        print(is_completed)
        main_db.update_task(task_id = task_id, completed = int(is_completed))
        load_tasks()
        print(int(is_completed))
        
    def add_task_flet(_):
        if task_input.value:
            task_text = task_input.value.strip()
            task_id = main_db.add_task(task=task_text)
            task_input.value = None
            task_list.controls.append(view_task(task_id = task_id,task_text = task_text))
            page.update()
    
    task_input = ft.TextField(label='введите задачу', on_submit = add_task_flet)
    
    def set_filter(filter_value):
        nonlocal filter_type
        print(filter_type)
        filter_type = filter_value
        print(filter_type)
        load_tasks()
    
    filter_buttons = ft.Row(
    [
        ft.ElevatedButton(
            'Все задачи',
            on_click=lambda e: set_filter('all')
        ),
        ft.ElevatedButton(
            'В работе',
            on_click=lambda e: set_filter('uncompleted')
        ),
        ft.ElevatedButton(
            'Готово',
            on_click=lambda e: set_filter('completed')
        ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )
        
    
    page.add(ft.Column([task_input, filter_buttons, task_list],spacing=10,expand=True))
    load_tasks()
    

if __name__ == '__main__':
    main_db.init_db()
    ft.app(main_page)