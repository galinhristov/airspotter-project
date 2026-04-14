from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from sightings.forms import SightingCreateForm, SightingEditForm, SightingDeleteForm
from sightings.models import Sighting



class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user



class SightingListView(ListView):
    model = Sighting
    template_name = 'sightings/sighting-list.html'
    context_object_name = 'sightings'

    def get_queryset(self):
        return Sighting.objects.filter(
            status=Sighting.StatusChoices.PUBLISHED,
            visibility=Sighting.VisibilityChoices.PUBLIC,
        ).select_related('owner', 'aircraft', 'airport').prefetch_related('tags')



class SightingDetailView(DetailView):
    model = Sighting
    template_name = 'sightings/sighting-details.html'
    context_object_name = 'sighting'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Sighting.objects.filter(
                status=Sighting.StatusChoices.PUBLISHED,
                visibility=Sighting.VisibilityChoices.PUBLIC,
            ) | Sighting.objects.filter(owner=self.request.user)

        return Sighting.objects.filter(
            status=Sighting.StatusChoices.PUBLISHED,
            visibility=Sighting.VisibilityChoices.PUBLIC,
        )


class SightingCreateView(LoginRequiredMixin, CreateView):
    model = Sighting
    form_class = SightingCreateForm
    template_name = 'sightings/sighting-create.html'
    success_url = reverse_lazy('sighting-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class SightingUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Sighting
    form_class = SightingEditForm
    template_name = 'sightings/sighting-edit.html'

    def get_success_url(self):
        return reverse_lazy('sighting-details', kwargs={'pk': self.object.pk})



class SightingDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Sighting
    template_name = 'sightings/sighting-delete.html'
    success_url = reverse_lazy('sighting-list')
    context_object_name = 'sighting'










