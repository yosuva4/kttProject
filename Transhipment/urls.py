from django.urls import path

from . import views

urlpatterns = [
    path('Transhipment/',views.TransHome.as_view()),
    path('Transhipmentlist/',views.TranshList.as_view())
]