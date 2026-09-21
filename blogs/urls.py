from django.urls import path

from blogs.views import blog_list_view

urlpatterns = [
    path('', blog_list_view, name='blog_list'),
]
