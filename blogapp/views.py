from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog, Person
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import LoginForm
from django.http import JsonResponse
from django.views.generic import ListView, DetailView


# Create your views here.


# def blogList(request):
#    blogs = Blog.objects.all()
#    paginator = Paginator(blogs, 1)
#    page = request.GET.get('page')
#    posts = paginator.get_page(page)

#    return render(request, 'blogList.html', {'blogs': blogs, 'posts': posts})

class BlogPersonListview(ListView):
    model = Person
    template_name = 'blogPersonList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['blogs'] = Person.objects.all()
        paginator = Paginator(context['blogs'], 10)
        page = self.request.GET.get('page')
        context['posts'] = paginator.get_page(page)

        try:
            context['posts'] = paginator.page(page)
        except PageNotAnInteger:
            context['posts'] = paginator.page(1)
        except EmptyPage:
            context['posts'] = paginator.page(paginator.num_pages)

        return context



class BlogListview(ListView):
    model = Blog
    template_name = 'blogList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['blogs'] = Blog.objects.all()
        paginator = Paginator(context['blogs'], 10)
        page = self.request.GET.get('page')
        context['posts'] = paginator.get_page(page)

        try:
            context['posts'] = paginator.page(page)
        except PageNotAnInteger:
            context['posts'] = paginator.page(1)
        except EmptyPage:
            context['posts'] = paginator.page(paginator.num_pages)

        return context



def blogPersonDetail(request, blog_id):
    blogPerson_detail = get_object_or_404(Person, pk=blog_id)
    return render(request, 'blogPersonDetail.html', {'blogPerson_detail' : blogPerson_detail})





def blogDetail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogDetail.html', {'blog_detail': blog_detail})


@login_required(login_url='/login/')
def createBlog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('blogList')
        else:
            return redirect('blogList')

    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})

# @login_required(login_url='/login/')
# ef createBanner(request):
#    if request.method == 'POST':
#        form = CreateBanner(request.POST, request.FILES)

#        if form.is_valid():
 #           form.save()
  #          return redirect('blogList')
   #     else:
    #        return redirect('home')

  #  else:
   #     form = CreateBanner()




class LoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    def form_invalid(self, form):
        messages.error(self.request, '???????????? ?????????????????????.', extra_tags='danger')
        return super().form_invalid(form)

    # form = CreateBlog()
    # return render(request, 'createBlog.html', {'form': form})







