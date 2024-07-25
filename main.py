import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Te amo ana")))


ft.app(main, view=ft.WEB_BROWSER)