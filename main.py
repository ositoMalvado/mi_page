import flet as ft
from Tabs import *
from Funciones import *
import random

def main(page: ft.Page):

    page.fonts = {
        "GasoekOne": github_to_raw("https://github.com/chrisbull/font-collection/blob/master/Circular/CircularStd-Medium.ttf")
    }

    page.theme = ft.Theme(font_family="GasoekOne")
    page.title = "Utilidades Oficina"


    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    

    def change_color():
        random_color = "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        page.theme.color_scheme_seed = random_color
        page.update()
    change_color()

    page.add(
        ft.Tabs(
            tabs=[
                ft.Tab(
                    text="Federación Patronal",
                    content=ft.Tabs(
                        [
                            TabFederacionFranquicias()
                        ],
                        tab_alignment=ft.TabAlignment.CENTER,
                        expand=True,
                        scrollable=True
                    )
                ),
                ft.Tab(
                    text="Río Uruguay",
                    content=ft.Tabs(
                        [
                            TabRioUruguayPremio()
                        ],
                        tab_alignment=ft.TabAlignment.CENTER,
                        expand=True,
                        scrollable=True
                    )
                ),
                ft.Tab(
                    text="General",
                    content=ft.Tabs(
                        [
                            TabGeneralPatentes()
                        ],
                        tab_alignment=ft.TabAlignment.CENTER,
                        expand=True,
                        scrollable=True
                    )
                )
            ],
            tab_alignment=ft.TabAlignment.CENTER,
            expand=True
        )
    )



ft.app(main, assets_dir="assets")