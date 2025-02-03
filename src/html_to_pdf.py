import os
import pdfkit
from jinja2 import Environment, FileSystemLoader

def generar_certificado(data, output_pdf):
    # Configurar Jinja2 para cargar plantillas desde el directorio 'templates'
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('web.html')

    # Renderizar el HTML con los datos del certificado
    html_content = template.render(data)

    # Guardar el HTML renderizado en un archivo temporal
    temp_html = 'temp.html'
    with open(temp_html, 'w', encoding="utf-8") as f:
        f.write(html_content)
    
    # Opciones de pdfkit
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

    # Ruta a wkhtmltopdf
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # Generar el a partir del HTML renderizado
    css_path = os.path.join(template_dir, "style.css")
    try:
        pdfkit.from_file(temp_html, output_pdf, options=options, configuration=config, css=css_path)
        print(f"PDF generado correctamente: {output_pdf}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")
    finally:
        # Eliminar el archivo HTML temporal
        if os.path.exists(temp_html):
            os.remove(temp_html)


if __name__ == '__main__':
    # Datos de Ejemplo
    data = {
        'nombre': 'Juan Pérez',
        'diplomado': 'Python',
        'fecha': '10 de enero de 2021',
        'institucion': "Universidad PSM"
    }

    # Nombre del archivo de salida
    output_pdf = 'certificado.pdf'

    # Llamar a la función para generar el certificado
    generar_certificado(data, output_pdf)
