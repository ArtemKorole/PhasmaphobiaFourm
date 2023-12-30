from MainForum.models import *

def get_ghosts_by_cat_id(id):
    ghosts_this_category = Ghost.objects.filter(category_id = id)
    return ghosts_this_category

def get_ghost_by_id(id):
    ghost = Ghost.objects.get(id = id)
    return ghost

def get_cart_by_id(id):
    cart = Map.objects.get(id = id)
    return cart
