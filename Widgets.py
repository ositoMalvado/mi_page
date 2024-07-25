import flet as ft
import math
class CalculadoraPremio(ft.Container):


    def update_premio(self, e):
        # Aplicar el descuento del 15%
        # Actualizar el valor en la interfaz
        if final_value and self.text_field_premio.value:
            discounted_value = float(self.text_field_premio.value) * 0.85
            
            # Redondear al múltiplo de 300 más cercano, siempre hacia arriba
            rounded_value = math.ceil(discounted_value / 300) * 300
            
            # Asegurarse de que el valor redondeado no sea menor que el valor descontado
            final_value = max(rounded_value, math.ceil(discounted_value))
            
            self.valor_final.value = str(int(final_value))
        else:
            self.valor_final.value = "0"
        self.valor_final.update()

    def __init__(self):
        super().__init__()

        self.valor_final = ft.Text("0")

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
        )
        self.content = ft.Column(
            controls=[
                ft.Text("Calculadora de Premio"),
                self.text_field_premio,
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