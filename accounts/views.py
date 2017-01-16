from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from datetime import datetime


def index(request):
    return render(request, 'index.html', {}
                  # , content_type='application/xhtml+xml'
    )


# def profile(request):
#     return render(request, 'profile.html', {}, content_type='application/xhtml+xml')


def register(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        t = datetime.now()
        t = (t - datetime(1970,1,1)).total_seconds()
        instance.user_id = int(t)
        # t = datetime.datetime.now().date()
        # instance.id = datetime.datetime.strftime(t)
        print instance.user_id
        instance.save()
    context = {
        "form": form,
    }
    return render(request, 'login_form.html', context)