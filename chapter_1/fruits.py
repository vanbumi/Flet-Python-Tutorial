import flet as ft 

def main(page: ft.Page):
    page.add(
        ft.Row(
            controls= [
                ft.Text("My Favorite Fruits: \n"),
            ]
        ),
        ft.Row(
            controls=[
                ft.Text("Apple"),
                ft.Text("Mango"),
                ft.Text("Guava")
            ]
        ),
        ft.Column(
            controls=[
                ft.Text("My Favorite Kroket: \n")
            ]
        ),
        ft.Column(
            controls = [
                ft.Text("Joko Sus"),
                ft.Text("Vini Vidi"),
                ft.Text("Mikel Gorbacef")
            ]
        )
    )



ft.app(target = main)