from django.urls import path, include
from . import views
from tovar import views as tovar_views

urlpatterns = [
    path('', tovar_views.index, name='index'),
]

