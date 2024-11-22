import flet as ft 

def main(page: ft.Page):
    page.title = "Error Handling in Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 100
    page.window.width = 400
    page.window.height = 700
    page.window.resizable = False

    user_name = ft.TextField(label="Enter your name", width=300)
    print_name_column = ft.Column()

    def call_hello(e):
        if not user_name.value:
            user_name.error_text = "Please enter your name"
            page.update()
        else:
            page.clean()        
            print_name_column.controls.append(ft.Text(f"Hello {user_name.value}", weight="bold", size=20))
            page.add(print_name_column)
    
    # PR CREATE BUTTON TO GO BACK TO MAIN PAGE
 
    page.add(
        user_name,
        ft.ElevatedButton("Say hello", on_click=call_hello),
        print_name_column
    )






ft.app(target=main)