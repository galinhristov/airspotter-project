from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView

from accounts.forms import (
    AirSpotterUserCreationForm,
    AirSpotterLoginForm,
    AirSpotterUserEditForm,
)
from core.tasks import send_welcome_email, send_welcome_email_async

UserModel = get_user_model()



class RegisterView(CreateView):
    model = UserModel
    form_class = AirSpotterUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.object.email:
            send_welcome_email_async(self.object.email)
        return response



class AirSpotterLoginView(LoginView):
    authentication_form = AirSpotterLoginForm
    template_name = 'accounts/login.html'



class AirSpotterLogoutView(LogoutView):
    next_page = reverse_lazy('home')



class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = AirSpotterUserEditForm
    template_name = 'accounts/profile-edit.html'


    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


    def get_queryset(self):
        return UserModel.objects.filter(pk=self.request.user.pk)



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['own_sightings_count'] = user.sightings.count()
        context['own_collections_count'] = user.collections.count()
        context['favourite_sightings_count'] = user.favorite_sightings.count()
        return context













