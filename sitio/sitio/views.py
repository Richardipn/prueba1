from django.http import HttpResponse
import datetime
from django.template import Template, Context

def index(request):

    documento = "Hello, world. You're at the polls index."

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("goodbye")

def damefecha(request):

    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" %fecha_actual
    return HttpResponse(documento)


def calculaedad(request,agno,edad):
    periodo = agno-2020
    edadfutura = edad+periodo
    documento = """<html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>""" %(agno,edadfutura)
    return HttpResponse(documento)

def inicio(request):
    # traer archuivo html
    archivo = open("sitio/public/index.html") 
    # leer archivo
    html = archivo.read()
    # cerrar archivo
    archivo.close()

    # retornar archivo
    ctx= Context()
    documento = Template(html).render(ctx)
    return HttpResponse(documento)

