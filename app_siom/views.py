from django.shortcuts import render
from .models import Usuario, Medicamento

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()
        medicamentos = {
            'medicamentos': Medicamento.objects.all()
        }

        return render(request, 'usuarios/medicamentos.html',medicamentos)
    else:
        usuarios = {'usuarios': Usuario.objects.all()}
        return render(request, 'usuarios/usuarios.html', usuarios)


def medicamentos(request):
    context = {'medicamentos': Medicamento.objects.all()}

    return render(request, 'usuarios/medicamentos.html',context)    

def receber_compra(request,id):
    context = {'medicamentos': Medicamento.objects.all()}
    medicamento = Medicamento.objects.get(id=id)
    if medicamento.quantidade > 0:
        medicamento.quantidade -= 1
        medicamento.save()

    return render(request, 'usuarios/medicamentos.html',context)
        



    