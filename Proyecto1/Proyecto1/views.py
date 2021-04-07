from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona (object):
    
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #primera vista

    Persona1 = Persona("Uriels", "Damian")

    ahora = datetime.datetime.now()
    temas = ["Plantillas","Modelos","Formularios","Vistas","Despleiegue"]
    
    #doc_externo = get_template('miPlantilla.html')


    #doc_externo = open("/home/uriel/Documentos/proyectos Django/Proyecto1/Proyecto1/plantilla/miPlantilla.html")

    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #ctx = Context({"Persona" : Persona1, "fecha":ahora, "temas": temas})

    #documento = doc_externo.render({"Persona" : Persona1, "fecha":ahora, "temas": temas})

    return render(request, "miPlantilla.html",{"Persona" : Persona1, "fecha":ahora, "temas": temas})

def despedida(request):
    return HttpResponse("Adios que les vaya bien")


def damefecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>
    """ %fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, edad,agno):
    
    periodo = agno - 2021
    edadFutura = edad + periodo
    
    documento = """<html>
    <body>
    <h1>
    Fen el año %s tendarás %s
    </h1>
    </body>
    </html>
    """ %(agno, edadFutura)
    return HttpResponse(documento)

def curso_C(request):
    ahora = datetime.datetime.now()
    return render(request, "CursoC.html",{"dameFecha":ahora})