from django.conf.urls import url
from.import views

app_name = 'contas'

urlpatterns = [
    url(r'^signup/$',views.signup_view,name='cadastrar'),
    url(r'^login/$',views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]