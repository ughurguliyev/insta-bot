from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboardPageView.as_view(), name='dashboard-page'),
    path('instagram-search/', views.searchFormPageView.as_view(), name='search-form-page'),
    path('login/', views.loginPageView.as_view(), name='login-page'),
    path('user/logout/', views.LogoutView.as_view(), name='logout-page')
]