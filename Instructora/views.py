from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, "index.html")


def edificios(request):
    # edificio=Edificios.objects.all()
    # print(edificios)
    return render(request, "edificios.html")
# , {"edificios":edificio})

def apartamentos(request):
    # edificio=Edificios.objects.all()
    # print(edificios)
    return render(request, "apartamentos.html")
# , {"edificios":edificio})


def personas_Apto(request):
    # edificio=Edificios.objects.all()
    # print(edificios)
    return render(request, "personasApto.html")
# , {"edificios":edificio})



