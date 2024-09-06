from django.urls import path
from apps.usuarios.views import login, cadastro, logout

urlpatterns = [ 
    path('login',login, name='login'),
    path('cadastroPaciente',cadastro, name='cadastroPaciente'),
    path('cadastroAdm',cadastro, name='cadastroAdm'),
    path('logout',logout, name='logout')
]