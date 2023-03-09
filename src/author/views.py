from django.views.generic import ListView, DetailView

from author.models import Author


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author
