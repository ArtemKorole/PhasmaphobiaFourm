from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('ghost_cat/<int:id>',views.ghost_cat,name = 'ghost_cat'),
    path('ghost/<int:id>',views.ghost,name = 'ghost'),
    path('journal',views.journal,name = 'journal'),
    path('cart/<int:id>',views.cart,name = 'cart'),
    path('about_us',views.about,name = 'about'),
]