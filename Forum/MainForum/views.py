from django.shortcuts import render
from MainForum.models import *
from .services import *


def index(request):
    data = {
        'categories':Ghost_category.objects.all(),
        'all_carts': Map.objects.all(),
        'all_ghost_events':Ghost_event.objects.all(),
        'all_evidences':Evidence.objects.all(),
    }
    return render(request,'MainForum/index.html',data)

def ghost_cat(request,id:int):
    data =  {
        'ghosts': get_ghosts_by_cat_id(id),
    }
    return render(request,'MainForum/ghost_categories.html',data)

def ghost(request,id:int):
    data = {
        'ghost': get_ghost_by_id(id),
    }
    return render(request,'MainForum/ghost.html',data)

def journal(request):
    data = {
        'all_ghosts':Ghost.objects.all(),
    }
    return render(request,'MainForum/journal.html',data)

def cart(request, id):
    data = {
        'cart':get_cart_by_id(id),
    }
    return render(request,'MainForum/cart.html',data)

def about(request):
    return render(request,'MainForum/about.html')