from django.shortcuts import render, redirect
from .forms import CreateBlog

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blogList(request):
    return render(request, 'blogList.html')

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
