# Import library
import flet as ft 

# Define main function
def main(page: ft.Page ):
    # 1. Page title
    page.title = "Hello world!"

    # 2. Text control
    text = ft.Text(value="My first Flat app!", size=30, color="Blue")

    # 3. Append to page
    page.controls.append(text)

    # 4. Update the page
    page.update()

    # 5. Run the app
    # python hello.py or
    # flet run hello.py ==> HOT RELOAD!
    # flet hello.py ==> HOT RELOAD!
    # flet hello.py --web ==> TAMPILAN DI WEB BROWSER
    










ft.app(target=main) 
#ft.app (target=main, view=ft.WEB_BROWSER)  # Optional