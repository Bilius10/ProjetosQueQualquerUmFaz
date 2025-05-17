import flet as ft
from docx2pdf import convert
from PIL import Image
from reportlab.pdfgen import canvas
import time

def main(page: ft.Page):
    page.title = "Conversor para PDF"
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    arquivoSelecionado = ft.Text(value="Nenhum arquivo selecionado", color="#FFFFFF", size=20)

    mensagem = ft.Text(value="", color="#FFFFFF", size=20)

    def selecionar_arquivo(e):
        file_picker.pick_files(allow_multiple=False)

    def arquivo_selecionado(e):
        global arquivo
        if file_picker.result and file_picker.result.files:
            arquivo = file_picker.result.files[0].path 

            arquivoSelecionado.value = f"Arquivo selecionado: {file_picker.result.files[0].name}"
            arquivoSelecionado.update()

    def converter_arquivo(e):

        ext = arquivo.split(".")[-1].lower()

        try:
            if ext == "docx":
                convert(arquivo)

            elif ext in ["jpg", "jpeg", "png"]:
                img = Image.open(arquivo).convert("RGB")
                img.save(arquivo + ".pdf")

            elif ext == "txt":
                with open(arquivo, 'r') as f:
                    texto = f.read()

                c = canvas.Canvas(arquivo + ".pdf")
                c.drawString(100, 750, texto[:100])  
                c.save()
            
            else:
                mensagem.value = "Formato de arquivo não suportado!"
                mensagem.color = "#FF0000"
                mensagem.update()

                time.sleep(2)

                mensagem.value = ""
                mensagem.update()
                arquivoSelecionado.value = "Arquivo selecionado:"
                arquivoSelecionado.update()

                return
            
            mensagem.value = "Arquivo convertido com sucesso!"
            mensagem.color = "#00FF00"
        except:
            mensagem.value = "Erro ao converter arquivo!"
            mensagem.color = "#FF0000"
    
        mensagem.update()

        time.sleep(2)

        mensagem.value = ""
        mensagem.update()
        arquivoSelecionado.value = "Arquivo selecionado:"
        arquivoSelecionado.update()
        
    file_picker = ft.FilePicker(on_result=arquivo_selecionado)
    page.overlay.append(file_picker)

    containerPrincipal = ft.Container(
        content=ft.Column(
            [
                ft.Text(value="Conversor para PDF", color="#FFFFFF",
                        size=50, text_align=ft.TextAlign.CENTER),
                
                ft.Container(height=200),

                arquivoSelecionado,

                ft.Container(height=150),

                mensagem, 

                ft.ElevatedButton(
                    text="Selecionar Arquivo",
                    color="#FFFFFF",
                    width=200,
                    height=50,
                    on_click=selecionar_arquivo,
                ),

                ft.ElevatedButton(
                    text="Converter",
                    color="#FFFFFF",
                    width=200,
                    height=50,
                    on_click=converter_arquivo,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
        ),
        width=500,
        height=700,
        padding=20,
        border_radius=ft.border_radius.all(50),
        bgcolor="#1E1E1E",
        alignment=ft.alignment.center,
        image_fit=ft.ImageFit.COVER,
    )

    page.add(containerPrincipal)


ft.app(target=main)
