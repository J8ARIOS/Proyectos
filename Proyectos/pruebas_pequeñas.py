import pandas as pd
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
import io



def generar_pdf_completo(pdf_plantilla, excel_path, pdf_salida):
    """
    Genera un PDF completo basado en una plantilla y datos de un archivo Excel.

    :param pdf_plantilla: Ruta del archivo PDF que actúa como plantilla.
    :param excel_path: Ruta del archivo Excel con los datos.
    :param pdf_salida: Ruta donde se guardará el PDF completo generado.
    """
    # Leer datos del Excel
    df = pd.read_excel(excel_path)

    # Leer el PDF original
    reader = PdfReader(pdf_plantilla)
    writer = PdfWriter()

    # Configuración de la fuente personalizada (si es necesario)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    for _, row in df.iterrows():
        # Crear un lienzo temporal para escribir los datos en la página actual
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)

        # Iterar sobre las columnas del Excel para insertar los datos
        for col_name in df.columns:
            value = row[col_name] if pd.notna(row[col_name]) else ""
            
            # Definir posiciones personalizadas para cada campo
            if col_name == "Nombre y apellidos":
                x, y = 100, 700  # Ejemplo de coordenadas
            elif col_name == "Tipo documento identidad":
                x, y = 100, 680
            elif col_name == "Nro. Documento":
                x, y = 100, 660
            else:
                continue

            # Dibujar el texto en el PDF
            c.setFont("Arial", 10)
            c.drawString(x, y, str(value))

        # Finalizar el lienzo
        c.save()

        # Fusionar la página generada con el PDF original
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page = reader.pages[0]
        page.merge_page(new_pdf.pages[0])
        writer.add_page(page)

    # Guardar el PDF final
    with open(pdf_salida, "wb") as output_file:
        writer.write(output_file)

# Parámetros de entrada y salida
pdf_plantilla = '/mnt/data/PDF.pdf'
excel_path = '/mnt/data/VADSAMU.xlsx'
pdf_salida = '/mnt/data/PDF_completo.pdf'

# Generar el PDF completo
generar_pdf_completo(pdf_plantilla, excel_path, pdf_salida)
print(f"PDF completo generado en: {pdf_salida}")import pandas as pd
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
import io



def generar_pdf_completo(pdf_plantilla, excel_path, pdf_salida):
    """
    Genera un PDF completo basado en una plantilla y datos de un archivo Excel.

    :param pdf_plantilla: Ruta del archivo PDF que actúa como plantilla.
    :param excel_path: Ruta del archivo Excel con los datos.
    :param pdf_salida: Ruta donde se guardará el PDF completo generado.
    """
    # Leer datos del Excel
    df = pd.read_excel(excel_path)

    # Leer el PDF original
    reader = PdfReader(pdf_plantilla)
    writer = PdfWriter()

    # Configuración de la fuente personalizada (si es necesario)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    for _, row in df.iterrows():
        # Crear un lienzo temporal para escribir los datos en la página actual
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)

        # Iterar sobre las columnas del Excel para insertar los datos
        for col_name in df.columns:
            value = row[col_name] if pd.notna(row[col_name]) else ""
            
            # Definir posiciones personalizadas para cada campo
            if col_name == "Nombre y apellidos":
                x, y = 100, 700  # Ejemplo de coordenadas
            elif col_name == "Tipo documento identidad":
                x, y = 100, 680
            elif col_name == "Nro. Documento":
                x, y = 100, 660
            else:
                continue

            # Dibujar el texto en el PDF
            c.setFont("Arial", 10)
            c.drawString(x, y, str(value))

        # Finalizar el lienzo
        c.save()

        # Fusionar la página generada con el PDF original
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page = reader.pages[0]
        page.merge_page(new_pdf.pages[0])
        writer.add_page(page)

    # Guardar el PDF final
    with open(pdf_salida, "wb") as output_file:
        writer.write(output_file)

# Parámetros de entrada y salida
pdf_plantilla = '/mnt/data/PDF.pdf'
excel_path = '/mnt/data/VADSAMU.xlsx'
pdf_salida = '/mnt/data/PDF_completo.pdf'

# Generar el PDF completo
generar_pdf_completo(pdf_plantilla, excel_path, pdf_salida)
print(f"PDF completo generado en: {pdf_salida}")