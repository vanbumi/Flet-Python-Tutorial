import flet as ft
from random import randint

def main(page: ft.Page):
    page.title = "Guess Me"
    page.window.width = 550
    page.window.max_width = 800
    page.window.height = 700
    page.window.resizable = True
    page.padding = 30

    # Generating a random number between 1 and 100
    answer = randint(1, 100)
    #print("=>", answer) # For debugging purposes


    # Insert fonts
    page.fonts = {
        "SpaceMission": "fonts/SpaceMission-rgyw9.otf",
        "Uncracked" : "fonts/Uncracked-X3WjK.otf",
    }

    # Players input
    player_1 = ft.TextField(hint_text="Guess a number 1-100...", label="Player 1", border_radius=20)
    player_2 = ft.TextField(hint_text="Guess a number 1-100...", label="Player 2", border_radius=20 )

    # Printing the result
    result = ft.Text(size=45, color="blue", font_family= "Uncracked")  

    # Button function
    def check_guess_player_1(e):
        if int(player_1.value) < answer:
            result.value = "Too low!"
        elif int(player_1.value) > answer:
            result.value = "Too high!"
        elif int(player_1.value) == answer:
            result.value = "Player 1 You won!"
        else:
            result.value = "Invalid input"
        page.update()

    def check_guess_player_2(e):
        if int(player_2.value) < answer:
            result.value = "Too low!"
        elif int(player_2.value) > answer:
            result.value = "Too high!"
        elif int(player_2.value) == answer:
            result.value = "Player 2 You won!"
        else:
            result.value = "Invalid input"
        page.update()

    # Checker button
    check_player_1 = ft.ElevatedButton("Check you Guess", on_click=check_guess_player_1)
    check_player_2 = ft.ElevatedButton("Check you Guess", on_click=check_guess_player_2)

    page.add(
        ft.Card(
            ft.Container(
            content = ft.Row(
                controls=[
                    ft.Text ("Guess Me", font_family="SpaceMission", size=30, color="blue"),
                ], alignment ="center"
                ), padding=20
            ),
        ),
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        player_1,
                        check_player_1,
                    ]
                ),
                ft.Row(
                    controls=[
                        player_2,
                        check_player_2,
                    ]
                ),
                result,
            ],
            horizontal_alignment= "center"
            
        )
        
    )

ft.app(target = main, assets_dir="assets")  # assets_dir is optional
