import flet as ft
from Tabs import *
from Funciones import *
from Widgets import ThemeButton, ColorButton
import random

# class Example(ft.Column):
#         def __init__(self):
#             super().__init__()
#             self.audio1 = ft.Audio(
#                 src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True
#             )

#             async def pause_audio(e):
#                 await self.audio1.pause()

#             self.controls = [
#                 ft.Text(
#                     "This is an app with background audio. Note: this example doesn't work in Safari browser."
#                 ),
#                 ft.ElevatedButton("Stop playing", on_click=pause_audio),
#             ]

#         # happens when example is added to the page (when user chooses the Audio control from the grid)
#         def did_mount(self):
#             self.page.overlay.append(self.audio1)
#             self.page.update()

#         # happens when example is removed from the page (when user chooses different control group on the navigation rail)
#         def will_unmount(self):
#             self.page.overlay.remove(self.audio1)
#             self.page.update()

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