import flet as ft 

def main(page: ft.Page):
    page.title = "Chapter 3 Homework"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.Margin(20, 20, 20, 20)
    page.bgcolor = ft.colors.LIGHT_BLUE
    page.window.width = 450
    page.window.height = 700
    page.window.resizable = False

    # Create a text field & judul
    text_judul = ft.Text("Homework App", size=40, weight="bold", color="white")
    text_field_l = ft.TextField(value = 0, width=50, text_align="center")
    text_field_2 = ft.TextField(value = 100, width=50, text_align="center")

    # Create button functions
    def women_click(e):
        text_field_l.value = int(text_field_l.value) + 5
        page.update()

    def man_click(e):
        text_field_2.value = int(text_field_2.value) - 5
        page.update()

    def reset_click(e):
        text_field_l.value = 0
        text_field_2.value = 0
        page.update()

    page.add(
        ft.Row(
            controls=[
                text_judul
            ],
            alignment="center"
        ),
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.WOMAN, on_click=women_click),
                text_field_l,
                text_field_2,
                ft.IconButton(ft.icons.MAN, on_click=man_click)        
            ], 
            alignment = "spaceEvenly",
            expand = True
        ), ft.Row(
            controls=[
                ft.ElevatedButton(text="Reset", on_click= reset_click)
            ],
            alignment= "center"
        )   
    )

ft.app(target = main)