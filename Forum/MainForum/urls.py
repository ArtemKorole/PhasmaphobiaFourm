from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('ghost_cat/<int:id>',views.ghost_category,name = 'ghost_cat'),
    path('ghosts/<int:id>',views.ghost,name = 'ghost'),
    path('ghosts/<slug:ghost_slug>',views.ghost_slug,name = 'slug_ghost'),
    path('journal',views.journal,name = 'journal'),
    path('cart/<int:id>',views.cart,name = 'cart'),
    path('about_us',views.about,name = 'about'),
    path('tag/<slug:tag_slug>',views.get_ghosts_by_tag,name = 'tag'),
    path('tags/',views.show_tags,name = 'tags'),
]