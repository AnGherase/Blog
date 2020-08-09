from django.urls import path
from . import views

app_name = 'payment'
#defining URL patterns for the product lists and detail views
urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]
