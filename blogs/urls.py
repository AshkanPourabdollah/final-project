from django.urls import path

from blogs.views import blog_list_view, blog_details_view

urlpatterns = [
    path('', blog_list_view, name='blog_list'),
    path('<int:pk>/', blog_details_view, name='blog_detail'),
]
