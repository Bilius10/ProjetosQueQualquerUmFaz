import flet as ft
import requests
import time
from Session import session


def statusPage(page_buscar):

    iconeStatus = ft.Icon(
        name=ft.icons.CIRCLE,
        color=ft.colors.WHITE,
        size=50,
    )


    horasOnline = ft.Text(
        value="00:00:00",
        size=18,
        color=ft.Colors.GREEN,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD,
    )

  
    horasOffline = ft.Text(
        value="00:00:00",
        size=18,
        color=ft.Colors.RED,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD,
    )

    try:
        response = requests.get(f"{session.user_data.get('url')}")
        if response.status_code == 200:
            iconeStatus.color = ft.Colors.GREEN
        else:
            iconeStatus.color = ft.Colors.RED
            iconeStatus.update()
    except requests.exceptions.RequestException as e:
        iconeStatus.color = ft.Colors.RED
        iconeStatus.update()
    
    

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    f"{session.user_data['url']}",
                    size=24,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=20),  

                
                iconeStatus,

                ft.Container(height=10),  
                ft.Text(
                    "Status Atual",
                    size=16,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=20),  

             
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Horas Online", size=14,
                                        color=ft.Colors.GREEN),
                                horasOnline,
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Column(
                            [
                                ft.Text("Horas Offline", size=14,
                                        color=ft.Colors.RED),
                                horasOffline,
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                ft.Container(height=30),  

                ft.ElevatedButton(
                    text="Voltar",
                    on_click=page_buscar,
                    bgcolor=ft.Colors.BLUE_GREY_700,
                    color=ft.Colors.WHITE,
                    width=200,
                    height=50,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12),
                    ),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        width=400,
        height=550,
        padding=20,
        bgcolor=ft.Colors.BLACK,
        alignment=ft.alignment.center,
        border_radius=12,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 4),
        ),
    )
