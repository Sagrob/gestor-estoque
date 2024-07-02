from django.urls import path

from .views import (
    adicionar_embalagem,
    adicionar_local,
    inicio,
    listar_embalagens,
    listar_locais,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar', adicionar_local, name='adicionar_local'),
    path('embalagens/', listar_embalagens, name='listar_embalagens'),
    path('embalagens/adicionar', adicionar_embalagem, name='adicionar_embalagem'),  # noqa: E501

]
