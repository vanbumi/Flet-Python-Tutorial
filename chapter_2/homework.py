import flet as ft

# define main function
def main(page: ft.Page):

    # setting page title
    page.title = "Greetings App with Reference"

    # change page theme
    page.theme_mode = ft.ThemeMode.LIGHT

    # taking first & last name from user
    first_name = ft.Ref[ft.TextField]()
    middle_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    # create column for greeting users
    greetings = ft.Ref[ft.Row]()

    # define button click button
    def on_btn_click(e):
        greetings.current.controls.append(ft.Text(f"Hello {first_name.current.value} {middle_name.current.value} {last_name.current.value}"))
        first_name.current.value = ""
        middle_name.current.value = ""
        last_name.current.value = ""
        first_name.current.focus()
        page.update()

    # menampilkan semua components pada page
    page.add(
        ft.TextField(ref= first_name, label="First Name", autofocus = True),
        ft.TextField(ref= middle_name, label="Middle Name"),
        ft.TextField(ref= last_name, label = "Last Name"),
        ft.ElevatedButton("Say Hello!", on_click = on_btn_click),
        ft.Row(ref = greetings) # all the Flet controls have 'ref' property
    )

ft.app(target = main)