from django.urls import path

from accounts.views import RegisterView, AirSpotterLoginView, AirSpotterLogoutView, ProfileDetailView, \
    ProfileUpdateView, DashboardView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', AirSpotterLoginView.as_view(), name='login'),
    path('logout/', AirSpotterLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-details'),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
)