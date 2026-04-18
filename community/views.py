from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from community.forms import CollectionCreateForm, CollectionEditForm
from community.models import Collection


class CollectionOwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'community/collection-list.html'
    context_object_name = 'collections'

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user).prefetch_related('sightings')


class CollectionDetailView(LoginRequiredMixin, DetailView):
    model = Collection
    template_name = 'community/collection-details.html'
    context_object_name = 'collection'

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user).prefetch_related('sightings')


class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CollectionCreateForm
    template_name = 'community/collection-create.html'
    success_url = reverse_lazy('collection-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['sightings'].queryset = self.request.user.sightings.all()
        return form


class CollectionUpdateView(LoginRequiredMixin, CollectionOwnerRequiredMixin, UpdateView):
    model = Collection
    form_class = CollectionEditForm
    template_name = 'community/collection-edit.html'
    context_object_name = 'collection'

    def get_success_url(self):
        return reverse_lazy('collection-details', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['sightings'].queryset = self.request.user.sightings.all()
        return form


class CollectionDeleteView(LoginRequiredMixin, CollectionOwnerRequiredMixin, DeleteView):
    model = Collection
    template_name = 'community/collection-delete.html'
    success_url = reverse_lazy('collection-list')
    context_object_name = 'collection'