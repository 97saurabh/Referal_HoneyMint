from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from . import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('myapp:login')
    template_name = 'accounts/signup.html'

def signin(request):

    return render(request,'accounts/sign.html',{})

def refer_fun(request):

    form=forms.FormName()
    da=False
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            code=form.cleaned_data['Referal_Code']

            try:
                go = User.objects.get(username=code)
            except:
                go=False
            if go:
                return HttpResponseRedirect(reverse('myapp:register',kwargs={'refer_code':go}))
            da="Referal Code Does Not Match"




    return render(request,"accounts/form.html",{"form":form,"da":da})
def register(request,refer_code):

    registered = False
    if request.method == "POST":
        user_form = forms.UserCreateForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            refer_used=user_form.cleaned_data['username']
            user.set_password(user.password)
            user.save()
            ob1=User.objects.get(username=refer_code)
            try:
                a1=ob1.result
                a1.point=a1.point+100
                a1.save()
            except:
                a=models.UserResult(refer_by=ob1,point=100)
                a.save()


            return HttpResponseRedirect(reverse('myapp:sendmail'))

        else:
            print(user_form.errors)
    else:

        user_form =forms.UserCreateForm()

    return render(request,'accounts/signup.html',{
                                    'form':user_form,
                                    'registered':registered,
    })
def ranklist(request):
    data=models.UserResult.objects.all().order_by('-point')

    return render(request,'ranklist.html',{'data':data,})
def sendmail(request):
    ob=User.objects.latest('pk')
    subject = 'Welcome to HoneyMint'
    #message="Hi"
    message = 'Welcome'+ob.first_name+"\n"+'Your Referal Code is '+str(ob.username)+"\n"+"Share this link amoung your friend "+str("http://127.0.0.1:8000/myapp/signup/")+str(ob.username)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [str(ob.email),]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponseRedirect(reverse('myapp:login'))
