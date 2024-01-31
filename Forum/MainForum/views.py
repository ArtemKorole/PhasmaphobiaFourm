from django.shortcuts import render
from MainForum.models import *
from .services import *


def index(request):
    data = {
        'categories': Ghost_category.objects.all(),
        'all_carts': Map.objects.all(),
        'all_ghost_events': Ghost_event.objects.all(),
        'all_evidences': Evidence.objects.all(),
    }

    # yurei = Ghost.objects.get(pk=2)
    # defaultTeg = TagGhost.objects.get(pk=3)
    # # hardTag = TagGhost.objects.get(pk=1)
    # yurei.tags.set([defaultTeg])

    return render(request, 'MainForum/index.html', data)


def ghost_category(request, id: int):
    data = {
        'ghosts': get_ghosts_by_cat_id(id),
    }
    return render(request, 'MainForum/ghost_categories.html', data)

def ghost_slug(request, ghost_slug: str):
    data = {
        'ghost': get_ghost_by_slug(ghost_slug)
    }
    return render(request, 'MainForum/ghost.html', data)

def ghost(request, id: int):
    data = {
        'ghost': get_ghost_by_id(id),
    }
    return render(request, 'MainForum/ghost.html', data)


def journal(request):
    data = {
        'all_ghosts': Ghost.objects.all(),
    }
    return render(request, 'MainForum/journal.html', data)


def cart(request, id: int):
    data = {
        'cart': get_cart_by_id(id),
    }
    return render(request, 'MainForum/cart.html', data)


def about(request):
    return render(request, 'MainForum/about.html')

def get_ghosts_by_tag(request, tag_slug):
    return render(request, 'MainForum/ghosts_by_tag.html', get_ghosts_by_tag_slug(tag_slug) )

def show_tags(request):
    data = {
        'tags':get_all_tags()
    }
    return render(request, "MainForum/tags_list.html", data)