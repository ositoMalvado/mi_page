import flet as ft
import math
import random



class Zoomtainer(ft.Container):


    def zoom_hover(self, e):
        self.scale = self.zoom if e.data == "true" else 1
        self.update()


    def __init__(self, contenido, zoom):
        super().__init__()
        self.content = contenido
        self.scale = 1
        self.zoom = zoom
        self.animate_scale = ft.Animation(duration=100, curve=ft.AnimationCurve.FAST_OUT_SLOWIN)
        self.on_hover = self.zoom_hover    


class CalculadoraPremio(ft.Container):


    def update_premio(self, e):
        # Aplicar el descuento del 15%
        self.sonido.play()
        if self.text_field_premio.value == '':
            self.valor_final.value = "0"
            self.valor_final.update()
            if e.control.data == "descuento":
                return
        self.intervalo_display.value = "$" + str(int(self.intervalo_slider.value))
        self.intervalo_display.update()
        if self.text_field_premio.value == '':
            return

        discounted_value = int(float(self.text_field_premio.value) * (1 - self.descuento / 100))
        
        intervalo = int(self.intervalo_slider.value)
        # Redondear al múltiplo de 300 más cercano, siempre hacia arriba
        rounded_value = int(math.ceil(discounted_value / intervalo) * intervalo)

        # Asegurarse de que el valor redondeado no sea menor que el valor descontado
        final_value = max(rounded_value, math.ceil(discounted_value))
            
        self.valor_final.value = str(int(final_value))
        self.valor_final.update()

    def slider_handle(self, e):
        self.descuento = self.slider.value
        self.descuento_display.value = str(int(self.slider.value)) + "%"
        self.descuento_display.update()
        if e.control.data == "descuento":
            self.slider.label = "Descuento: " + str(int(self.slider.value)) + "%"
            self.slider.update()
        else:
            self.intervalo_slider.label = "Intervalo: $" + str(int(self.intervalo_slider.value))
            self.intervalo_slider.update()
        self.update_premio(e)
        self.sonido.play()

    def copy_premio(self, e):
        self.copy_sound.play()
        self.page.set_clipboard(self.valor_final.value)
        self.sb_copiado.open = True
        self.page.update()

    def did_mount(self):
        self.page.overlay.append(self.sb_copiado)
        self.page.overlay.append(self.sonido)
        self.page.overlay.append(self.copy_sound)
        self.page.update()
        return super().did_mount()

    def __init__(self):
        super().__init__()

        self.sonido = ft.Audio(src="bamboo.mp3")
        self.copy_sound = ft.Audio(src="copy.mp3")

        self.sb_copiado = ft.SnackBar(
            content=ft.Text("Copiado al portapapeles"),
            bgcolor=ft.colors.GREEN
        )

        self.descuento = 15

        self.slider = ft.Slider(
            value=self.descuento,
            min=0,
            max=15,
            divisions=15,
            on_change=self.slider_handle,
            label="Descuento: 15%",
            data="descuento",
        )

        self.valor_final = ft.Text("0", size=40, expand=True, text_align=ft.TextAlign.CENTER)

        self.text_field_premio = ft.TextField(
            label="Premio",
            prefix_icon=ft.icons.ATTACH_MONEY_ROUNDED,
            hint_text="Ingresa el premio",
            # height=100,
            content_padding=ft.padding.all(5),
            text_style=ft.TextStyle(
                size=24,
            ),
            hint_style=ft.TextStyle(
                size=24,
            ),
            label_style=ft.TextStyle(
                size=24,
            ),
            on_change=self.update_premio,
            input_filter = ft.InputFilter(
                regex_string=r"[1-9][0-9]*",
                allow=True,
                replacement_string="",
            )
        )
        self.boton_copiar = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.icons.ATTACH_MONEY_ROUNDED),
                    self.valor_final,
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            tooltip="Copiar premio con descuento",
            on_click=self.copy_premio,
        )

        self.descuento_display = ft.Text(str(self.descuento) + "%", weight=ft.FontWeight.BOLD, size=20)

        self.intervalo = 300
        self.intervalo_slider = ft.Slider(
            value=self.intervalo,
            min=0,
            max=1000,
            divisions=20, # i need each division be by 50
            on_change=self.slider_handle,
            label="Intervalo: 300",
            data="intervalo"
        )
        self.intervalo_display = ft.Text("$" + str(self.intervalo), weight=ft.FontWeight.BOLD, size=20)

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Calculadora de Premio", size=30, weight=ft.FontWeight.BOLD),
                self.text_field_premio,
                ft.Row(
                    [
                        ft.Text("Descuento: ", weight=ft.FontWeight.BOLD, size=18),
                        self.descuento_display,
                    ]
                ),
                self.slider,
                ft.Row(
                    [
                        ft.Text("Intervalo: ", weight=ft.FontWeight.BOLD, size=18),
                        self.intervalo_display,
                    ]
                ),
                self.intervalo_slider,
                ft.Text("Premio con descuento: ", weight=ft.FontWeight.BOLD, size=18),
                self.boton_copiar
            ],
            spacing=2,
        )
        self.border_radius=10
        self.border=ft.border.all(1, ft.colors.BLACK12)
        self.bgcolor=ft.colors.PRIMARY_CONTAINER
        self.width=500
        self.padding=10


class ColorButton(ft.IconButton):

    def change_color(self, e):
        random_color = "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.page.theme.color_scheme_seed = random_color
        self.page.update()

    def __init__(self):
        super().__init__()
        self.icon = ft.icons.PALETTE_ROUNDED
        self.tooltip = "Cambiar color"
        self.on_click = self.change_color





class ThemeButton(ft.IconButton):

    def change_theme(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        self.icon = ft.icons.LIGHT_MODE_ROUNDED if self.page.theme_mode == ft.ThemeMode.DARK else ft.icons.DARK_MODE_ROUNDED
        self.page.update()

    def __init__(self):
        super().__init__()
        self.icon = ft.icons.DARK_MODE_ROUNDED
        self.tooltip = "Modo oscuro"
        self.on_click = self.change_theme


def main(page: ft.Page):
    page.add(CalculadoraPremio())


if __name__ == "__main__":
    ft.app(target=main)