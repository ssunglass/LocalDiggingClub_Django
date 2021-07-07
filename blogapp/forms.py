from django import forms
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import AuthenticationForm
from django.forms import EmailField




class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ['brand', 'location', 'instagram', 'image', 'title', 'head', 'body']

        widgets = {

            'brand': forms.TextInput(
                             attrs={'class': 'form-control', 'style': 'width: 20%', 'placeholder': '브랜드를 입력하세요.'}
            )
            ,
            'location': forms.TextInput(
                          attrs={'class': 'form-control', 'style': 'width: 30%', 'placeholder': '위치를 입력하세요.'}
            ),
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 30%', 'placeholder': '제목을 입력하세요.'}
            ),
            'head': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 50%', 'placeholder': '표제를 입력하세요.'}

            ),

            'body': forms.CharField(widget=CKEditorUploadingWidget()),

        }

# class CreateBanner(forms.ModelForm):
 #   class Meta:
  #      model = Banner

#        fields = ['title', 'location', 'image']

 #       widgets = {
  #          'title': forms.TextInput(
   #             attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
    #        ),

     #       'location': forms.TextInput(
      #          attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '위치를 입력하세요.'}
       #     ),

      #  }

class LoginForm(AuthenticationForm):
    username = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))









