from django.shortcuts import render
from django.views.generic import ListView

# models
from .models import User


def listado_users(request):
    lista_usuarios = User.objects.all()
    titulo = 'Listado de usuarios 2'
    return render(request, 'user/users.html', {'lista_usuarios': lista_usuarios, 'titulo': titulo})


class ListUser(ListView):
    context_object_name = 'lista_usuarios'
    queryset = User.objects.all()
    template_name = 'user/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        titulo = 'Listado de usuarios 1'
        context = {
            'titulo': titulo,
        }
        kwargs.update(context)
        return super().get_context_data(object_list=object_list, **kwargs)

    # def get_queryset(self):
    #     return User.objects.all()
