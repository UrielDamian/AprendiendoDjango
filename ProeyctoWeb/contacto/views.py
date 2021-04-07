from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

    Formulario_contacto = FormularioContacto()

    if request.method == "POST":
        Formulario_contacto = FormularioContacto(data = request.POST)

        if Formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            
            email = EmailMessage("Mensaje desde App django", 
            "El usuario con nombre: {} con la dirección {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
            "",["uriel.damian.montiel.yoo@gmail.com"],reply_to = [email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
               

          
    return render(request,"contacto/contacto.html", {"miFormulario":Formulario_contacto})