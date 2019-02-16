from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.decorators import login_required


def logout_view(request):
    """用户注销"""
    logout(request)
    return HttpResponseRedirect(reverse('learn_blogs:index'))

def register(request):
    if request.method!="POST":
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learn_blogs:index'))
    context={'form':form}
    return render(request,'users/register.html',context)


# Create your views here.
