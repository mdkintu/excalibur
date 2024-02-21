from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('job-post/', views.post_job, name='job-post'),
    path('job-search/', views.post_find, name='job-search'),
    path('inbox/', views.inbox_new, name='inbox'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('message/<str:pk>', views.viewMessage, name='message'),
]
