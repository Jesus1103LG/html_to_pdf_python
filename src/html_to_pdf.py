import os
import pdfkit

current_dir = os.path.dirname(os.path.abspath(__file__))

html = os.path.join(current_dir, "web.html")
css = os.path.join(current_dir, "style.css")

if not os.path.exists(html):
    raise FileNotFoundError(f"El archivo {html_path} no existe")

if not os.path.exists(css):
    raise FileNotFoundError(f"El archivo {css_path} no existe")

options = {
    'page-size': 'A4',
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0in',
    'encoding': "UTF-8",
    'orientation': 'Landscape',
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None,
    '--enable-local-file-access': None,
    '--disable-smart-shrinking': None,
    '--zoom': '1.3'
}

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_file(html, "web.pdf", options=options , configuration=config, css=css)