from django.views.generic import DetailView
from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from taggit.models import Tag
from urllib.parse import unquote
from .models import TovarCreate, Carousel


class SearchView(generic.ListView):
    model = TovarCreate
    template_name = 'tovar/tovar_search.html'
    context_object_name = 'tovars'

    def get_queryset(self):
        query = self.request.GET.get('q')
        tags = self.request.GET.getlist('tags')

        queryset = TovarCreate.objects.all().order_by('title')

        if query:
            queryset = queryset.filter(Q(title__iregex=query))

        if tags:
            for tag in tags:
                queryset = queryset.filter(tags__name=tag)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = unquote(self.request.GET.get('q', ''))
        search_tags = self.request.GET.get('search_tags', '')

        context['q'] = query
        context['selected_tags'] = self.request.GET.getlist('tags')
        if search_tags:
            # use iregex to ignore case sensitivity
            context['all_tags'] = Tag.objects.filter(name__iregex=search_tags).order_by('name')
        else:
            context['all_tags'] = Tag.objects.all().order_by('name')
        return context


def index(request):
    main_carusel = Carousel.objects.all()
    tovars_popular = TovarCreate.objects.filter(category='Popular')
    tovars_collection = TovarCreate.objects.filter(category='Collection')
    return render(request, 'main/index.html', {'tovars_popular': tovars_popular, 'tovars_collection': tovars_collection, 'main_carusel': main_carusel})


class TovarDetailView(DetailView):
    model = TovarCreate
    template_name = 'tovar/tovar_index.html'
    context_object_name = 'tovar'
