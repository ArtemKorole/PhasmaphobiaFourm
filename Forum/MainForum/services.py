from django.shortcuts import get_object_or_404
from MainForum.models import *

def get_ghosts_by_cat_id(cat_id):
    category = Ghost_category.objects.get(pk=cat_id)
    ghosts_this_category = category.ghosts.all()
    return ghosts_this_category

def get_ghost_by_id(id):
    ghost = Ghost.objects.get(id = id)
    return ghost

def get_ghost_by_slug(slug):
    ghost = Ghost.objects.get(slug=slug)
    return ghost

def get_cart_by_id(id):
    cart = Map.objects.get(id = id)
    return cart

def get_ghosts_by_tag_slug(slug):
    tag = get_object_or_404(TagGhost, slug=slug)
    ghosts = tag.tags.all()
    data = {
        'ghosts': ghosts,
        'tag': tag.tag
    }
    return data

def get_all_tags():
     return TagGhost.objects.all()
