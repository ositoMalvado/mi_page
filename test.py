import flet as ft
import random
from datetime import datetime
from datetime import timedelta
from typing import Union, Any

class DateTimePicker(ft.Container):

    def get_time(self):
        return self.timer_picker.value

    def get_date(self):
        return self.date_picker.value

    def date_handler(self, e):
        print(e.control.value)
        if self.date_time_on_button:
            self.button_date_picker.text = e.control.value.strftime(self.date_format)
        else:
            self.button_date_picker.tooltip = e.control.value.strftime(self.date_format)
        self.page.update()

    def time_handler(self, e):
        if self.date_time_on_button:
            self.button_time_picker.text = e.control.value.strftime(self.time_format)
        else:
            self.button_time_picker.tooltip = e.control.value.strftime(self.time_format)
        self.page.update()

    def on_button_click(self, e):
        if e.control.data == "date":
            self.page.open(self.date_picker)
            self.page.update()
        elif e.control.data == "time":
            self.timer_picker.open = True
            self.page.update()

    def did_mount(self):
        self.page.overlay.append(self.timer_picker)
        return super().did_mount()

    def __init__(
            self,
            time_init: datetime = datetime.now().time(),
            date_init: datetime = datetime.now().date(),
            date_min: datetime = datetime.now().date() - timedelta(days=365*100),
            date_max: datetime = datetime.now().date() + timedelta(days=365*100),
            date_format: str = "%d/%m/%Y",
            time_format: str = "%H:%M",
            altor: int = 40,
            date_time_on_button: bool = True,
            data: Any = "",
            expand: Union[bool, int, float] = 0,
        ):
        super().__init__()
        self.border_radius = 5
        self.anchor = 150
        self.altor = altor
        self.date_format = date_format
        self.time_format = time_format
        self.date_time_on_button = date_time_on_button
        self.data = data
        self.expand = expand
        self.timer_picker = ft.TimePicker(
            on_change=self.time_handler,
            value=time_init,
        )
        self.date_picker = ft.DatePicker(
            on_change=self.date_handler,
            value=date_init,
            first_date=date_min,
            last_date=date_max,
        )
        self.button_style = ft.ButtonStyle(
            shape=ft.ContinuousRectangleBorder(10),
            bgcolor=ft.colors.with_opacity(0.8, ft.colors.BACKGROUND),
            
        )
        self.button_date_picker = ft.ElevatedButton(
            icon=ft.icons.CALENDAR_TODAY_ROUNDED,
            expand=True,
            text=date_init.strftime(date_format),
            style=self.button_style,
            data="date",
            height=self.altor,
            on_click=self.on_button_click,
        ) if self.date_time_on_button else ft.IconButton(
            icon=ft.icons.CALENDAR_TODAY_ROUNDED,
            tooltip=date_init.strftime(date_format),
            expand=True,
            on_click=self.on_button_click,
            data="date",
            style=self.button_style
        )
        self.button_time_picker = ft.ElevatedButton(
            icon=ft.icons.TIMER_ROUNDED,
            expand=True,
            height=self.altor,
            text=time_init.strftime(time_format),
            style=self.button_style,
            data="time",
            on_click=self.on_button_click,
        ) if self.date_time_on_button else ft.IconButton(
            icon=ft.icons.TIMER_ROUNDED,
            tooltip=time_init.strftime(time_format),
            expand=True,
            on_click=self.on_button_click,
            data="time",
            style=self.button_style
        )
        self.border = ft.border.all(1, ft.colors.PRIMARY)
        self.content=ft.Container(
            ft.Row(
                [
                    self.button_date_picker,
                    # ft.VerticalDivider(width=1, color=ft.colors.PRIMARY),
                    # self.button_time_picker,
                ],
                width=self.anchor if self.date_time_on_button else 50,
                height=self.altor,
                spacing=0,
                expand=True
            ),
            width=self.anchor if self.date_time_on_button else 50,
            height=self.altor,
            bgcolor=ft.colors.PRIMARY
        )


class PlanillaRow(ft.DataRow):

    def __init__(
        self,
        fecha: str,
        compañía: str,
        ramo: str,
        poliza: str,
        asegurado: str,
        cobrado: str,
        diferencia: str,
        call_eliminar: callable = None,
        call_editar: callable = None,
        call_guardar: callable = None,
    ):
        self.fecha = fecha
        self.compañía = compañía
        self.ramo = ramo
        self.poliza = poliza
        self.asegurado = asegurado
        self.cobrado = cobrado
        self.diferencia = diferencia
        self.call_eliminar = call_eliminar
        self.call_editar = call_editar
        self.call_guardar = call_guardar
        self.cells = [
            ft.DataCell(ft.Text(fecha)),
            ft.DataCell(ft.Text(compañía)),
            ft.DataCell(ft.Text(ramo)),
            ft.DataCell(ft.Text(poliza)),
            ft.DataCell(ft.Text(asegurado)),
            ft.DataCell(ft.Text(cobrado)),
            ft.DataCell(ft.Text(diferencia)),
            ft.DataCell(ft.Text("acciones")),
        ]
        super().__init__(cells=self.cells)

class PlanillaCobranza(ft.Container):


    def change_iconbutton(self, e):
        # icons.HORIZONTAL_RULE_OUTLINED
        if self.iconbutton_add_min.icon == ft.icons.ADD_ROUNDED:
            self.iconbutton_add_min.icon = ft.icons.HORIZONTAL_RULE_ROUNDED
            self.iconbutton_container.bgcolor = ft.colors.RED_200
            self.iconbutton_add_min.tooltip = "Negativo"
        else:
            self.iconbutton_add_min.icon = ft.icons.ADD_ROUNDED
            self.iconbutton_container.bgcolor = ft.colors.GREEN_200
            self.iconbutton_add_min.tooltip = "Positivo"
        self.iconbutton_container.update()


    def on_boton_agregar_click(self, e):
        for campo_obligatorio in self.datos_obligatorios:
            if not campo_obligatorio.value:
                campo_obligatorio.focus()
                self.sb_completar.open = True
                self.page.update()
                return
        dinero_diferencia = self.dinero_diferencia.value if self.dinero_diferencia.value else 0
        self.data_table.rows.append(
            PlanillaRow(
                self.fecha_picker.get_date().strftime("%d/%m/%Y"),
                self.drop_compañía.value,
                self.drop_ramo.value,
                self.poliza.value,
                self.asegurado.value,
                self.dinero_cobrado.value,
                f"-{dinero_diferencia}" if self.iconbutton_add_min.icon == ft.icons.HORIZONTAL_RULE_ROUNDED else f"{dinero_diferencia}",
            )
        )
        self.data_table.update()
        self.update_totales()
    
    def update_totales(self):
        # i need get total for every PlanillaRow.cobrado
        total = 0
        total_diferencia = 0
        for row in self.data_table.rows:
            total += int(float(row.cobrado))
            total_diferencia += int(float(row.diferencia))
        self.floating_total.text = f"${total}"
        self.floating_total_diferencia.text = f"${total_diferencia}"
        self.floating_total.update()
        self.floating_total_diferencia.update()

    def did_mount(self):
        self.page.overlay.append(self.sb_completar)
        return super().did_mount()

    def __init__(self):
        super().__init__()
        self.sb_completar = ft.SnackBar(content=ft.Text("Completa todos los campos"), bgcolor=ft.colors.RED_400)
        self.padding=5
        self.border_radius = 5
        self.border = ft.border.all(1, ft.colors.BLACK12)
        self.fecha_picker = DateTimePicker(expand=False, altor=47)
        self.drop_compañía = ft.Dropdown(
            label="Compañía",
            padding=0,
            content_padding=ft.padding.only(left=10, right=2, top=2, bottom=2),
            options=[
                ft.dropdown.Option("Río Uruguay"),
                ft.dropdown.Option("Federación Patronal"),
                ft.dropdown.Option("Galeno"),
                ft.dropdown.Option("Orbis"),
            ],
            expand=True
        )
        self.drop_ramo = ft.Dropdown(
            label="Ramo",
            padding=0,
            content_padding=ft.padding.only(left=10, right=2, top=2, bottom=2),
            options=[
                ft.dropdown.Option("Auto"),
                ft.dropdown.Option("Moto"),
                ft.dropdown.Option("AP"),
                ft.dropdown.Option("Casa"),
                ft.dropdown.Option("Incendio"),
            ],
            expand=True
        )
        
        self.poliza = ft.TextField(
            label="Poliza",
            input_filter=ft.InputFilter(
                regex_string=r"[0-9]",
                allow=True,
                replacement_string="",
            ),
            expand=True,
            height=48
        )

        self.dinero_cobrado = ft.TextField(
            label="Cobrado",
            prefix_icon=ft.icons.ATTACH_MONEY_ROUNDED,
            input_filter=ft.InputFilter(
                regex_string=r"[0-9]",
                allow=True,
                replacement_string="",
            ),
            expand=True,
            height=48
        )


        self.iconbutton_add_min = ft.IconButton(
            icon=ft.icons.ADD_ROUNDED,
            tooltip="Positivo",
            on_click=self.change_iconbutton,
            icon_size=20,
            data="add_min",
        )

        self.iconbutton_container = ft.Container(
            self.iconbutton_add_min,
            bgcolor=ft.colors.GREEN_200,
            border_radius=100,
            margin=ft.margin.only(top=5),
            width=40,
            height=40
        )

        self.dinero_diferencia = ft.TextField(
            label="Diferencia",
            prefix_icon=ft.icons.ATTACH_MONEY_ROUNDED,
            suffix=self.iconbutton_container,
            input_filter=ft.InputFilter(
                regex_string = r"[0-9]",
                allow=True,
                replacement_string="",
            ),
            expand=True,
            height=48
        )
        self.asegurado = ft.TextField(
            label="Asegurado",
            expand=True,
        )

        self.datos_obligatorios = [
            self.drop_compañía,
            self.drop_ramo,
            self.poliza,
            self.asegurado,
            self.dinero_cobrado,
        ]

        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(expand=True,value="Fecha", weight=ft.FontWeight.BOLD), tooltip="Fecha"),
                ft.DataColumn(ft.Text(expand=True,value="Compañía", weight=ft.FontWeight.BOLD), tooltip="Compañía"),
                ft.DataColumn(ft.Text(expand=True,value="Ramo", weight=ft.FontWeight.BOLD), tooltip="Ramo"),
                ft.DataColumn(ft.Text(expand=True,value="Poliza", weight=ft.FontWeight.BOLD), tooltip="Poliza"),
                ft.DataColumn(ft.Text(expand=True,value="Asegurado", weight=ft.FontWeight.BOLD), tooltip="Asegurado"),
                ft.DataColumn(ft.Text(expand=True,value="Dinero Cobrado", weight=ft.FontWeight.BOLD), tooltip="Dinero Cobrado"),
                ft.DataColumn(ft.Text(expand=True,value="Diferencia", weight=ft.FontWeight.BOLD), tooltip="Diferencia"),
                ft.DataColumn(ft.Text(expand=True,value="Acciones", weight=ft.FontWeight.BOLD), tooltip="Acciones"),
            ],
            expand=True,
            rows=[
            ],
            
        )


        self.floating_total = ft.FloatingActionButton(text="Total: $0",icon=ft.icons.ATTACH_MONEY_ROUNDED)
        self.floating_total_diferencia = ft.FloatingActionButton(text="Diferencia: $0",icon=ft.icons.ATTACH_MONEY_ROUNDED)


        self.content = ft.Stack(
            [
                ft.Column(
                    controls=[
                        ft.Row(
                            [
                                self.fecha_picker,
                                self.drop_compañía,
                                self.drop_ramo,
                                self.poliza,
                                self.asegurado,
                                self.dinero_cobrado,
                                self.dinero_diferencia,
                
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            # expand=True
                        ),
                        ResponsiveControl(
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            self.data_table
                                        ],
                                        # width=2000
                                        # expand=True
                                    )
                                ],
                                # expand=True,
                                scroll="auto",
                            ),
                            alignment=ft.alignment.top_center
                        )
                    ]
                ),
                ft.Column(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Container(
                                    margin=ft.margin.only(bottom=45),
                                    content=ft.Row(
                                        controls=[
                                            self.floating_total,
                                            self.floating_total_diferencia,
                                            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.on_boton_agregar_click),
                                        ]
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END
                        ),
                    ]
                )
            ]
        )
        self.expand = True

class ResponsiveControl(ft.canvas.Canvas):
    def __init__(self,
            content= None,
            resize_interval=1,
            on_resize=None,
            expand=1,
            padding:ft.padding=0,
            margin:ft.margin=0,
            debug:str="",
            alignment:ft.alignment=ft.alignment.center,
            **kwargs
        ):
        super().__init__(**kwargs)
        self.content = ft.Container(
                content=content,
                padding=5 if debug else padding,
                alignment=alignment,
                margin=5 if debug else margin,
                bgcolor=ft.colors.with_opacity(0.2, debug) if debug else None,
                border=ft.border.all(1, debug) if debug else None,
        )
        self.expand = expand
        self.resize_interval = resize_interval
        self.resize_callback = on_resize
        self.on_resize = self.__handle_canvas_resize

    def __handle_canvas_resize(self, e):
        pass

def main(page: ft.Page):
    page.spacing = 0
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.scroll = ft.ScrollMode.ALWAYS

    pc = PlanillaCobranza()
    page.add(pc)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)