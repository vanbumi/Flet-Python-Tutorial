import flet as ft 
from time import sleep

def main(page: ft.Page):
    page.title = "Counter App"

    #text = ft.Text()
    text = ft.Text(text_align="center", width=400, font_family="Monaco", size=80)

    page.add(text)

    for i in range (11):
        text.value = f"Count {i}"
        page.update()
        sleep(1)




ft.app(target=main)