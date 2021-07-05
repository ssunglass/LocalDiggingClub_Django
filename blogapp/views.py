from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog, User
from bootstrap_modal_forms.generic import BSModalLoginView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm


# Create your views here.


def blogList(request):
    blogs = Blog.objects.all()
    # banners = Banner.objects.all()
    return render(request, 'blogList.html', {'blogs': blogs})




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
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)

    # form = CreateBlog()
    # return render(request, 'createBlog.html', {'form': form})
