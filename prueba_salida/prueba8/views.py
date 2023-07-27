from django.shortcuts import render
from prueba8.models import *
from .forms import Buscar

def index(request):
    if request.method == 'POST':
        form = Buscar(request.POST)
        businessentityid_buscado = request.POST.get("businessentityid_buscar")
        jobtitle_buscado = request.POST.get("jobtitle_buscar")
        gender_buscado = request.POST.get("gender_buscar")
        
        if businessentityid_buscado != "":
            datos = Person.objects.filter(businessentityid = businessentityid_buscado).values('firstname', 'lastname','employee__businessentityid','employee__jobtitle','employee__gender')

        if jobtitle_buscado != "" and businessentityid_buscado == "":
            datos = Employee.objects.filter(jobtitle = jobtitle_buscado).values('firstname', 'lastname','employee__businessentityid','employee__jobtitle','gender')

        if gender_buscado != "" and businessentityid_buscado == "" and jobtitle_buscado == "":
            datos = Employee.objects.filter(gender = gender_buscado).values('firstname', 'lastname','employee__businessentityid','employee__jobtitle','employee__gender')

        context = {'empleado' : datos, 'form' : form}

    else:
        #crear instancia vacia de formulario
        form = Buscar
        datos = []
        context = {'empleado' : datos, 'form' : form}
        pass
    return render(request, 'formulario.html', context)
# Create your views here.
