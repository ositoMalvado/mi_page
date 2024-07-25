import flet as ft
import math
class CalculadoraPremio(ft.Container):


    def update_premio(self, e):
        # Aplicar el descuento del 15%
        if self.text_field_premio.value == '':
            self.valor_final.value = "0"
            self.valor_final.update()
            return
        discounted_value = int(float(self.text_field_premio.value) * (1 - self.descuento / 100))
        
        # Redondear al múltiplo de 300 más cercano, siempre hacia arriba
        rounded_value = int(math.ceil(discounted_value / 300) * 300)

        # Asegurarse de que el valor redondeado no sea menor que el valor descontado
        final_value = max(rounded_value, math.ceil(discounted_value))
            
        self.valor_final.value = str(int(final_value))
        self.valor_final.update()

    def slider_handle(self, e):
        self.descuento = self.slider.value
        self.descuento_display.value = str(int(self.slider.value)) + "%"
        self.descuento_display.update()
        self.slider.label = "Descuento: " + str(int(self.slider.value)) + "%"
        self.slider.update()
        self.update_premio(e)

    def copy_premio(self, e):
        self.page.set_clipboard(self.valor_final.value)
        self.sb_copiado.open = True
        self.page.update()

    def did_mount(self):
        self.page.overlay.append(self.sb_copiado)
        return super().did_mount()

    def __init__(self):
        super().__init__()

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
        )

        self.valor_final = ft.Text("0", size=30)

        self.text_field_premio = ft.TextField(
            label="Premio",
            prefix_icon=ft.icons.ATTACH_MONEY_ROUNDED,
            hint_text="Ingresa el premio",
            on_change=self.update_premio
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

        self.content = ft.Column(
            controls=[
                ft.Text("Calculadora de Premio", size=30, weight=ft.FontWeight.BOLD),
                self.text_field_premio,
                ft.Row(
                    [
                        ft.Text("Descuento: ", weight=ft.FontWeight.BOLD),
                        self.descuento_display,
                    ]
                ),
                self.slider,
                ft.Text("Premio con descuento: ", weight=ft.FontWeight.BOLD),
                self.boton_copiar
            ]
        )
        self.border_radius=10
        self.border=ft.border.all(1, ft.colors.BLACK12)
        self.bgcolor=ft.colors.PRIMARY_CONTAINER
        self.width=500
        self.padding=10


def main(page: ft.Page):
    page.add(CalculadoraPremio())


if __name__ == "__main__":
    ft.app(target=main)