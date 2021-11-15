from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('reserve/', views.reserve, name='reserve'),
    path('reserve/<int:tour>/', views.reserve, name='reserve'),
    path('tours/', views.tours, name='tours'),
    path('guest_page/', views.guest_page, name='guest_page'),
    path('send_email/<str:pk>/<int:nr>/', views.send_email, name='send_email'),
    path('list/', views.list_all, name='list'),
    path('list/<str:opt>/', views.list_all, name='list'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('rules/', views.rules, name='rules'),
    path('rodo/', views.rodo, name='rodo'),
    path('gallery/', views.gallery, name='gallery')
    ]
