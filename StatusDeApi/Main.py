import flet as ft
import time
from BuscarApi import acharAPI
from StatusPage import statusPage

def main(page: ft.Page):
    page.title = "Status de API"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False
    
    def buscar_page(event=None):
        page.clean()
        page.add(acharAPI(status_page))


    def status_page(event):
        page.clean()
        page.add(statusPage(buscar_page))
       

    buscar_page(event=None)

if __name__ == "__main__":
    ft.app(target=main)
