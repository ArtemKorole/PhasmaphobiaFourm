from typing import Any
from django.shortcuts import render
from MainForum.models import *
from .services import *
from django.shortcuts import redirect
from .forms import GhostSearchForm
from django.views import View
from django.views.generic import TemplateView, ListView


class MainPage(View):
    def get(self, request):
        data = {
            'categories': Ghost_category.objects.all(),
            'all_carts': Map.objects.all(),
            'all_ghost_events': Ghost_event.objects.all(),
            'all_evidences': Evidence.objects.all(),
            'form': GhostSearchForm()
        }
        return render(request, 'MainForum/index.html', data)

    def post(self, request):
        id = request.POST['name']
        ghost = get_ghost_by_id(id)[0]
        return redirect(ghost.get_absolute_url())


def ghost_category(request, id: int):
    data = {
        'ghosts': get_ghosts_by_cat_id(id).select_related('category'),
    }
    return render(request, 'MainForum/ghost_categories.html', data)


class Ghost_by_Slug(View):
    def get(self, request, ghost_slug):
        data = {
            'ghost': get_ghost_by_slug(ghost_slug).select_related('category')[0],
            'tags': get_tags_by_ghost_slug(ghost_slug).prefetch_related('tags')
        }
        return render(request, 'MainForum/ghost.html', data)


class Ghost_by_Id(View):
    def get(self, request, id):
        data = {
            'ghost': get_ghost_by_id(id).select_related('category')[0],
            'tags': get_tags_by_ghost_id(id).prefetch_related('tags')
        }
        return render(request, 'MainForum/ghost.html', data)


class Journal(ListView):
    model = Ghost
    template_name = 'MainForum/journal.html'
    context_object_name = 'all_ghosts'

    def get_queryset(self):
        return Ghost.objects.all().order_by('number')


def cart(request, id: int):
    data = {
        'cart': get_cart_by_id(id),
    }
    return render(request, 'MainForum/cart.html', data)


class AboutPage(TemplateView):
    template_name = 'MainForum/about.html'


class Ghosts_by_Tag(View):
    def get(self, request, tag_slug):
        return render(request, 'MainForum/ghosts_by_tag.html', get_ghosts_by_tag_slug(tag_slug))


class Tags(ListView):
    model = TagGhost
    template_name = 'MainForum/tags_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return get_all_tags()
