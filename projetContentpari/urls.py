
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # Gestion
    path('', views.index, name="index"),
    path('inscription', views.inscription, name='inscription'),
    path('connexion', views.connexion, name='connexion'),
    url(r'^register/$', views.user_register, name='user_register'),
    url('logout',views.logout, name='logout'),


    # Page d'action
    path('profil', views.profil, name='profil'),
    url('parier',views.parier, name='parier'),

    # path('ivoirien', views.ivoirien, name='ivoirien'),
    # path('tennis', views.tennis, name='tennis'),
    # path('match', views.match, name='match'),
]   