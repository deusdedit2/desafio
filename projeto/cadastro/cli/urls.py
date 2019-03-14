from django.conf.urls import url, include
from .views import *

app_name = 'clientes'

urlpatterns = [
    url(r'^cliente_list/', cliente_list, name='listar_clientes'),
    url(r'^cliente_new/', cliente_new, name='cliente_new'),
    url(r'^cliente_edit/(?P<pk>[0-9]+)', cliente_edit, name='cliente_edit'),
    url(r'^cliente_remove/(?P<pk>[0-9]+)', cliente_remove, name='cliente_remove')
]


### ^ para o início do texto
# $ para o final do texto
# \d para um dígito
# + para indicar que o item anterior deve ser repetido pelo menos uma vez
## () para capturar parte do padrão