from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from sightings.forms import (SightingCreateForm,
                             SightingEditForm,
                             SightingDeleteForm,
                             SightingPhotoCreateForm,
                             SightingPhotoEditForm,
                             )
from sightings.models import Sighting, SightingPhoto


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


class SightingPhotoCreateView(LoginRequiredMixin, CreateView):
    model = SightingPhoto
    form_class = SightingPhotoCreateForm
    template_name = 'sightings/photo-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.sighting = get_object_or_404(Sighting, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        form.instance.sighting = self.sighting
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sighting-details', kwargs={'pk': self.sighting.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sighting'] = self.sighting
        return context


class SightingPhotoUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = SightingPhoto
    form_class = SightingPhotoEditForm
    template_name = 'sightings/photo-edit.html'
    context_object_name = 'photo'

    def test_func(self):
        obj = self.get_object()
        return obj.uploaded_by == self.request.user

    def get_success_url(self):
        return reverse_lazy('sighting-details', kwargs={'pk': self.object.sighting.pk})


class SightingPhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = SightingPhoto
    template_name = 'sightings/photo-delete.html'
    context_object_name = 'photo'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.uploaded_by != self.request.user:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden('You are not allowed to delete this photo.')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('sighting-details', kwargs={'pk': self.object.sighting.pk})