import flet as ft
from Widgets import CalculadoraPremio
from Widgets import Zoomtainer

class TabFederacionFranquicias(ft.Tab):

    franquicias = [
        {"tipo": "Auto", "porcentaje": "1%", "Monto": "$300.000"},
        {"tipo": "Auto", "porcentaje": "2%", "Monto": "$400.000"},
        {"tipo": "Auto", "porcentaje": "4%", "Monto": "$500.000"},
        {"tipo": "Auto", "porcentaje": "6%", "Monto": "$630.000"},
        {"tipo": "Camiones", "porcentaje": "2%", "Monto": "$1.150.000"},
        {"tipo": "Acoplados", "porcentaje": "2%", "Monto": "$870.000"},
    ]


    def __init__(self):
        super().__init__()
        self.text = "Franquicias"
        self.mi_data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(expand=True,value="Tipo de Vehículo", weight=ft.FontWeight.BOLD), tooltip="Tipo de Vehículo"),
                ft.DataColumn(ft.Text(expand=True,value="% Suma Asegurada", weight=ft.FontWeight.BOLD), tooltip="% Suma Asegurada"),
                ft.DataColumn(ft.Text(expand=True,value="Monto mínimo de Franquicia", weight=ft.FontWeight.BOLD), tooltip="Monto mínimo de Franquicia"),
            ],
            rows=[],
            expand=True,
        )

        for i, franquicia in enumerate(self.franquicias):
            self.mi_data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(Zoomtainer(ft.Text(franquicia["tipo"], weight=ft.FontWeight.BOLD), zoom=1.5)),
                        ft.DataCell(Zoomtainer(ft.Text(franquicia["porcentaje"]), zoom=1.5)),
                        ft.DataCell(Zoomtainer(ft.Text(franquicia["Monto"]), zoom=1.5)),
                    ],
                    color=ft.colors.BLACK12 if i % 2 == 0 else None
                )
            )
        self.expand = True
        self.content = ft.Column(
            controls=[
                ft.Container(height=5),
                ft.Container(
                    self.mi_data_table,
                    border_radius=10,
                    border=ft.border.all(1, ft.colors.BLACK12),
                    bgcolor=ft.colors.PRIMARY_CONTAINER
                )
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll="auto",
            expand=True
        )
from test import PlanillaCobranza
class TabGeneralCobranza(ft.Tab):

    def __init__(self):
        super().__init__()
        self.text = "Cobranza"
        self.content = PlanillaCobranza()

class TabGeneralPatentes(ft.Tab):

    patentes = {
        "AG450AA": "Enero 2024",
        "AG300AA": "Octubre 2023",
        "AG000AA": "Mayo 2023",
        "AF770AA": "Enero 2023",
        "AF600AA": "Octubre 2022",
        "AF000AA": "Agosto 2021",
        "AE600AA": "Enero 2021",
        "AE100AA": "Enero 2020",
        "AE000AA": "Octubre 2019",
        "AD400AA": "Enero 2019",
        "AD000AA": "Julio 2018",
        "AC200AA": "Enero 2018",
        "AC000AA": "Noviembre 2017",
        "AB000AA": "Febrero 2017",
        "AA900AA": "Enero 2017",
        "AA000AA": "Abril 2016",
        "PMA000": "2016",
        "ONA000": "2015",
        "NMA000": "2014",
        "MBA000": "2013",
        "KUA000": "2012",
        "JNA000": "2011",
        "IMA000": "2010",
        "HTA000": "2009",
        "GVA000": "2008",
        "GBA000": "2007",
        "FIA000": "2006",
        "ETA000": "2005",
        "EIA000": "2004",
        "EDA000": "2003",
        "DXA000": "2002",
        "DOA000": "2001",
        "DCA000": "2000",
        "CMA000": "1999",
        "BUA000": "1998",
        "BDA000": "1997",
        "APA000": "1996",
        "AAA000": "1995",
    }

    def __init__(self):
        super().__init__()
        self.text = "Año de auto por patente"
        self.mi_data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Patente", weight=ft.FontWeight.BOLD), tooltip="Patente"),
                ft.DataColumn(ft.Text("Año", weight=ft.FontWeight.BOLD), tooltip="Año"),
            ],
            rows=[],
        )
        for i, patente in enumerate(self.patentes):
            self.mi_data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(Zoomtainer(ft.Text(patente, weight=ft.FontWeight.BOLD), zoom=1.2)),
                        ft.DataCell(Zoomtainer(ft.Text(self.patentes[patente]), zoom=1.2)),
                    ],
                    color=ft.colors.BLACK12 if i % 2 == 0 else None
                )
            )

        self.expand = True
        self.content = ft.Column(
            controls=[
                ft.Container(height=5),
                ft.Container(
                    self.mi_data_table,
                    border_radius=10,
                    border=ft.border.all(1, ft.colors.BLACK12),
                    bgcolor=ft.colors.PRIMARY_CONTAINER
                )
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll="auto",
            expand=True
        )

class TabRioUruguayPremio(ft.Tab):

    def __init__(self):
        super().__init__()
        self.text = "Premio"

        self.expand = True
        self.content = ft.Column(
            controls=[
                ft.Container(height=5),
                CalculadoraPremio()
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll="auto",
            expand=True
        )
