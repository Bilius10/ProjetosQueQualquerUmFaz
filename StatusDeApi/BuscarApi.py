import flet as ft
import requests
import time
from Session import session

def acharAPI(page_status):
    def buscarApi(e):
      
        try:
            
            response = requests.get(f"{endPoint.value}")
    
            if response.status_code == 200:
                respostaApi.value = "Endpoint Encontrado!"
                respostaApi.color = ft.Colors.GREEN_500
            else:
                respostaApi.value = "Endpoint Não Encontrado!"
                respostaApi.color = ft.Colors.RED_500
        except Exception as e:
            respostaApi.value = f"Erro: {str(e)}"
        
        respostaApi.update()
        time.sleep(1)

        if respostaApi.value == "Endpoint Encontrado!":

            session.user_data["url"] = endPoint.value
            page_status(e)
        
        respostaApi.value = ""
        respostaApi.update()

    endPoint = ft.TextField(
        label="Digite o EndPoint",
        autofocus=True,
        width=350,
        text_size=18,
        border_color=ft.Colors.GREY_600,
        border_radius=8,
        filled=True,
        fill_color=ft.Colors.GREY_800,
    )


    respostaApi = ft.Text(
        value="",
        size=16,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )


    buscarButton = ft.ElevatedButton(
        text="Buscar",
        on_click=buscarApi,
        bgcolor=ft.Colors.BLUE_GREY_700,
        color=ft.Colors.WHITE,
        width=200,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Status de API",
                    size=36,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(height=140),  
                endPoint,
                ft.Container(height=120),  
                buscarButton,
                ft.Container(height=20), 
                respostaApi,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
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