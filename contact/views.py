from django.shortcuts import render


def contacto(request):
    return render(request, 'contact/contacto.html')
