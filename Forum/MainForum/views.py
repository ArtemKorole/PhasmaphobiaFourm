from typing import Any
from django.shortcuts import render, redirect
from MainForum.models import *
from .services import *
from .forms import GhostSearchForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView


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


class Ghosts_by_Category(ListView):
    model = Ghost
    template_name = 'MainForum/ghost_categories.html'
    context_object_name = 'ghosts'
    allow_empty = False

    def get_queryset(self):
        return get_ghosts_by_cat_id(self.kwargs['id']).select_related('category')


class Ghost_by_Slug(DetailView):
    model = Ghost
    template_name = 'MainForum/ghost.html'
    slug_url_kwarg = 'ghost_slug'
    context_object_name = 'ghost'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tags'] = get_tags_by_ghost_slug(
            context['ghost'].slug).prefetch_related('tags')
        return context


class Journal(ListView):
    model = Ghost
    template_name = 'MainForum/journal.html'
    context_object_name = 'all_ghosts'
    allow_empty = False

    def get_queryset(self):
        return Ghost.objects.all().order_by('number')


class Cart(DetailView):
    model = Map
    template_name = 'MainForum/cart.html'
    context_object_name = 'cart'
    pk_url_kwarg = 'id'


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
