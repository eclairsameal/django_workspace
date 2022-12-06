from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')[:5]   # 照日期編排取前5個
    return render(request, "blog/all_blogs.html", {"blogs":blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) # pk 是主鍵的縮寫
    # return render(request, "blog/detail.html", {"id": blog_id})
    return render(request, "blog/detail.html", {"blog": blog})
