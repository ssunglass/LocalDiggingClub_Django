from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog


# Create your views here.

def home(request):
    return render(request, 'home.html')

def blogList(request):
    blogs = Blog.objects.all()
    return render(request, 'blogList.html', {'blogs': blogs})

def blogDetail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogDetail.html', {'blog_detail': blog_detail})

def createBlog(request):

    if request.method == 'POST':
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogList')
        else:
            return redirect('home')

    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})


    # form = CreateBlog()
    # return render(request, 'createBlog.html', {'form': form})
