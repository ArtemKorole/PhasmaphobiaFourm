from django.urls import path
from . import views

urlpatterns = [
    path('',views.MainPage.as_view(), name='main_page'),
    path('ghost_cat/<int:id>',views.ghost_category,name = 'ghost_cat'),
    path('ghosts/<int:id>',views.Ghost_by_Id.as_view(),name = 'ghost'),
    path('ghosts/<slug:ghost_slug>',views.Ghost_by_Slug.as_view(),name = 'slug_ghost'),
    path('journal',views.Journal.as_view(),name = 'journal'),
    path('cart/<int:id>',views.cart,name = 'cart'),
    path('about_us',views.AboutPage.as_view(),name = 'about'),
    path('tag/<slug:tag_slug>', views.Ghosts_by_Tag.as_view(), name='tag'),
    path('tags/',views.Tags.as_view(),name = 'tags'),
]