import flet as ft

# define main function
def main(page: ft.Page):

    # setting page title
    page.title = "Simple Greetings App"

    # change page theme
    page.theme_mode = ft.ThemeMode.LIGHT

    # taking first & last name from user
    first_name = ft.TextField(label = "First Name", autofocus=True)
    last_name = ft.TextField(label = "Last Name")

    # create column for greeting users
    greetings = ft.Column()

    # define button click button
    def on_btn_click(e):
        greetings.controls.append(ft.Text(f"Hello {first_name.value} {last_name.value}"))
        first_name.value = ""
        last_name.value = ""
        first_name.focus()
        page.update()

    # create button
    hello = ft.ElevatedButton("Say hello", on_click=on_btn_click)

    # menampilkan semua components pada page
    page.add(
        first_name,
        last_name,
        hello,
        greetings
    )

ft.app(target = main)