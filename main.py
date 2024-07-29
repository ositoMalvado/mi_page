import flet as ft
from Tabs import *
from Funciones import *
from Widgets import ThemeButton, ColorButton

def main(page: ft.Page):

    page.fonts = {
        "GasoekOne": github_to_raw("https://github.com/chrisbull/font-collection/blob/master/Circular/CircularStd-Medium.ttf")
    }

    page.theme = ft.Theme(font_family="GasoekOne")
    page.title = "Utilidades Oficina"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    

    page.add(
        ft.Stack(
            [
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
                                    TabGeneralPatentes(),
                                    TabGeneralCobranza()
                                ],
                                tab_alignment=ft.TabAlignment.CENTER,
                                expand=True,
                                scrollable=True
                            )
                        )
                    ],
                    tab_alignment=ft.TabAlignment.CENTER,
                    expand=True
                ),
                ft.Row(
                    [
                        ColorButton(),
                        ThemeButton(),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    expand=True
                    
                ),
            ],
            expand=True
        )
    )



ft.app(main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)