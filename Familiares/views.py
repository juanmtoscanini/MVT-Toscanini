from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.

def familiar(request):

    familiar1=Familiar(nombre="Fernando", apellido="Toscanini", relacion="Hermano", edad=26, fecha_nacimiento="1996-3-12")
    familiar2=Familiar(nombre="Josefina", apellido="Toscanini", relacion="Prima", edad=27, fecha_nacimiento="1995-1-20")
    familiar3=Familiar(nombre="Jose", apellido="Vissi", relacion="Tio", edad=50, fecha_nacimiento="1972-9-17")
    familiar4=Familiar(nombre="Maria", apellido="Gamba", relacion="Abuela", edad=70, fecha_nacimiento="1952-8-25")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    familiares_guardados=[
        "Familiar agendado: "+familiar1.nombre+" "+familiar1.apellido+", relacion: "+familiar1.relacion+", edad: "+str(familiar1.edad),
        "Familiar agendado: "+familiar2.nombre+" "+familiar2.apellido+", relacion: "+familiar2.relacion+", edad: "+str(familiar2.edad),
        "Familiar agendado: "+familiar3.nombre+" "+familiar3.apellido+", relacion: "+familiar3.relacion+", edad: "+str(familiar3.edad),
        "Familiar agendado: "+familiar4.nombre+" "+familiar4.apellido+", relacion: "+familiar4.relacion+", edad: "+str(familiar4.edad),
        ]
    
    diccionario_familiares={"Familiares":familiares_guardados}
    template_familiares=loader.get_template("template1.html")
    render_familiares=template_familiares.render(diccionario_familiares)
    return HttpResponse(render_familiares)