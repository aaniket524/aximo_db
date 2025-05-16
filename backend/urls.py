from django.urls import path
from django.conf.urls.static import static  
from .views import get_workprocess_data
from .views import get_htesti_data
from .views import get_team_data

from . import views




urlpatterns = [
    path('workprocess/', get_workprocess_data),
    path('testimonials/', get_htesti_data),
    path('team/', get_team_data),
    path('services/', views.get_all_services),
    path('services/<slug:slug>/', views.get_single_service_by_slug),
    path('single-services/', views.get_all_single_services),
    path('single-services/<slug:slug>/', views.get_single_service_detail),
    path('blogs/', views.get_all_blogs),
    path('blogs/<slug:category_slug>/<slug:blog_slug>/', views.get_blog_detail),
    path('blogs/category/<slug:category_slug>/', views.get_blogs_by_category),
    path('blogs/tag/<slug:tag_slug>/', views.get_blogs_by_tag),
]

