import flet as ft
import requests
import threading
import time
from Session import session

thread_running = False


def statusPage(page_buscar):
    global thread_running

    iconeStatus = ft.Icon(
        name=ft.icons.CIRCLE,
        color=ft.Colors.WHITE,
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

    def monitorar_status():
        global thread_running
        online_time = 0
        offline_time = 0

        while thread_running:
            try:
                response = requests.get(f"{session.user_data.get('url')}")
                if response.status_code == 200:
                    offline_time = 0
                    iconeStatus.color = ft.Colors.GREEN
                    online_time += 1
                else:
                    online_time = 0
                    iconeStatus.color = ft.Colors.RED
                    offline_time += 1
            except requests.exceptions.RequestException:
                online_time = 0
                iconeStatus.color = ft.Colors.RED
                offline_time += 1

            horasOnline.value = time.strftime(
                "%H:%M:%S", time.gmtime(online_time))
            horasOffline.value = time.strftime(
                "%H:%M:%S", time.gmtime(offline_time))

            iconeStatus.update()
            horasOnline.update()
            horasOffline.update()

            time.sleep(1)

    thread_running = True
    monitor_thread = threading.Thread(target=monitorar_status)
    monitor_thread.start()

    def voltar(event):
        global thread_running
        thread_running = False
        page_buscar(event)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    f"Status de {session.user_data['url']}",
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
                    on_click=voltar,
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
