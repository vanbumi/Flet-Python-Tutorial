import flet as ft 

def main(page: ft.Page):
    page.Title = "To Do App"

    # taking input from user
    input_text = ft.TextField(hint_text="What you want todo", width=300)

    # function button
    def button_clicked(e):
        if input_text.value:
            page.add(ft.Checkbox(label = input_text.value))
            input_text.value = ""
            input_text.focus()
            page.update()
        
    # aligning the input text and button in a row
    page.add(
        ft.Row(
            [
                input_text,
                ft.ElevatedButton("Add", on_click=button_clicked),
            ]))

ft.app(target=main)