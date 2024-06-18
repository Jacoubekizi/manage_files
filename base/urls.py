from django.urls import path
from django.contrib.auth import views as auth_views
from System_management_folders import settings
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('new-file/', upload_file, name='new_file'),
    path('my-files/', get_my_files, name='my_files'),
    path('all-files/', all_files, name='all_files'),
    path('track-files/', track_files, name='track_files'),
    path('edit-file/<str:file_id>/', edit_file, name='edit_file'),
    path('info-file/<str:file_id>/', get_info_file, name='file_info'),
    path('accept-file/<str:file_id>/', accept_file, name='accept_file'),
    path('review-file/<str:file_id>/', review, name='review_file'),
    path('refuse-file/<str:file_id>/', refuse_file, name='refuse_file'),
    path('review-file/', order_file, name='order_file'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'auth/login.html', next_page = 'home', redirect_authenticated_user = True), name='login'),
    path('logout/',logout_user, name = 'logout'),
]