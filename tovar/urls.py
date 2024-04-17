from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<int:pk>/', views.TovarDetailView.as_view(), name='tovar-detail'),
]
