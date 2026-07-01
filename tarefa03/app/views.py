from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def usuarios(request):

    lista_usuarios = [
        {"nome": "Dutch Van Der Linge", "matricula": "01", "idade": 44, "cidade": "Filadélfia"},
        {"nome": "Hosea Matthews", "matricula": "02", "idade": 55, "cidade": "Montanhas Apalaches"},
        {"nome": "Arthur Morgan", "matricula": "03", "idade": 36, "cidade": "California"},
        {"nome": "John Marston", "matricula": "04", "idade": 26, "cidade": "Illinois"},
        {"nome": "Susan Grimshaw", "matricula": "05", "idade": 46, "cidade": "Ohio"}

    ]

    context = {
        "usuarios": lista_usuarios,
    }
    return render(request, "app/usuarios.html", context)