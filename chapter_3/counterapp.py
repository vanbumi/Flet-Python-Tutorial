import flet as ft 

def main(page: ft.Page):
    # Configure page properties
    page.title = "Counter App"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    # Configure window size and constraints
    page.window.width = 400
    page.window.height = 700
    page.window.resizable = False  # Prevent resizing the window

    txt_number = ft.TextField(value=0, width=100, height=50, text_align="center")


    # Create button functions
    def minus_click(e):
        txt_number.value = int(txt_number.value) -1
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) +1
        page.update()


    # Add content (optional placeholder for future widgets)
    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE_SHOPPING_CART_SHARP, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD_SHOPPING_CART_SHARP, on_click=plus_click)
            ],
            alignment="center",
        )
        
    )


ft.app(target=main)  # Run the app


'''
last video times: 32:29
Icon browser: https://gallery.flet.dev/icons-browser/
icons.ADD_A_PHOTO
icons.ADD_SHOPPING_CART_SHARP
icons.REMOVE_SHOPPING_CART_SHARP

'''