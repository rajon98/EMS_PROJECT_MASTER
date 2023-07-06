
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('adminclick',views.adminclick_view,name=''),
    path('adminsignup',views.admin_signup_view,name='admin-signup'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('logout',LogoutView.as_view(template_name='index.html'),name='logout'),
    path('admin-dashboard',views.admin_dashboard_view,name='admin-dashboard'),
    path('event_category_create',views.event_category_create_view,name=''),
    path('event_category_list',views.event_category_list_view,name='event_category_list'),

    path('organizerclick',views.organizerclick_view,name='organizer'),
    path('organizersignup',views.organizer_signup_view,name=''),
    path('organizerlogin',LoginView.as_view(template_name='organizerlogin.html')),
    path('logout',LogoutView.as_view(template_name='index.html')),
    
    path('attendeeclick',views.attendeeclick_view,name=''),
    path('attendeesignup',views.attendee_signup_view,name=''),
    path('attendeelogin',LoginView.as_view(template_name='attendeelogin.html')),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),


]
