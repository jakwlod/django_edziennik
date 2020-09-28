from django.urls import path, include
from django.contrib.auth import views as auth_views
from .import views
from django.urls import  get_urlconf

urlpatterns = [
    path('', views.index, name='index'),
     path('accounts/', include('django.contrib.auth.urls')),
     path('logout/', auth_views.LogoutView.as_view() , name="logout"),
     path('abc',views.abc,name='abc'),
    # path('abcd', views.abcd, name='abcd'),
     path('szczegol/<int:idp>',views.szczegoly,name='szczegoly' ),
     path('edytuj/<int:idp>', views.edytuj, name='edytuj' ),
     path('zatwierdze/<int:idp>', views.zatwierdze, name='zatwierdze' ),
     path('dodajo/<int:idp>', views.dodajo, name='dodajo'),
     path('zatwierdzo/<int:idp>', views.zatwierdzo, name='zatwierdzo' ),
]
