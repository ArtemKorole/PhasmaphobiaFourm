from django.db.models import Count
from django.shortcuts import get_object_or_404
from MainForum.models import *


def get_ghosts_by_cat_id(cat_id):
    category = Ghost_category.objects.get(pk=cat_id)
    ghosts_this_category = category.ghosts.all()
    return ghosts_this_category


def get_ghost_by_id(id):
    ghost = Ghost.objects.filter(id=id)
    return ghost


def get_ghost_by_slug(slug):
    ghost = Ghost.objects.filter(slug=slug)
    return ghost


def get_cart_by_id(id):
    cart = Map.objects.get(id=id)
    return cart


def get_ghosts_by_tag_slug(slug):
    tag = get_object_or_404(TagGhost, slug=slug)
    ghosts = tag.tags.all()
    data = {
        'ghosts': ghosts,
        'tag': tag.tag
    }
    return data


def get_ghost_by_name(name):
    ghost = Ghost.objects.filter(name=name)
    if ghost.exists():
        return ghost


def get_all_tags():
    return TagGhost.objects.annotate(ghosts=Count('tags')).filter(ghosts__gt=0)


def get_tags_by_ghost_id(id):
    ghost = get_ghost_by_id(id)
    return get_tags_by_ghost(ghost)


def get_tags_by_ghost_slug(slug):
    ghost = get_ghost_by_slug(slug)
    return get_tags_by_ghost(ghost)


def get_tags_by_ghost(ghost_obj):
    return ghost_obj[0].tags.all()
