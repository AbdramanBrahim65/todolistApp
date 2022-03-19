from django.urls import path
from todoapp.views import detail,creation_affichage,supprimer_views


urlpatterns = [
    path('',creation_affichage,name="home"),
    path('detail/<str:pk>',detail,name='detail'),
    path('supprimer/<str:pk>',supprimer_views,name='supprimer'),

]
