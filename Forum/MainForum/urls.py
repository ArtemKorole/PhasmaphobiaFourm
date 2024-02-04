from django.urls import path
from . import views

urlpatterns = [
    path('',views.MainPage.as_view(), name='main_page'),

    path('ghost_cat/<int:id>',views.Ghosts_by_Category.as_view(),name = 'ghost_cat'),
    path('ghosts/<slug:ghost_slug>',views.Ghost_by_Slug.as_view(),name = 'slug_ghost'),

    path('tag/<slug:tag_slug>', views.Ghosts_by_Tag.as_view(), name='tag'),
    path('tags/',views.Tags.as_view(),name = 'tags'),

    path('cart/<int:id>',views.Cart.as_view(),name = 'cart'),
    path('journal',views.Journal.as_view(),name = 'journal'),
    path('about_us',views.AboutPage.as_view(),name = 'about'),
]