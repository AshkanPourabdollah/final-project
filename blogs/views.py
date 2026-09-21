from django.shortcuts import render

from blogs.models import Blog


# Create your views here.
def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, "blogs/blog_list_page.html", context={"blogs": blogs})
