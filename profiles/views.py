from django.shortcuts import render, render_to_response, RequestContext, Http404
from django.contrib.auth.models import User

from forms import JobForm, AddressForm, UserPictureForm
from .models import Job, Address, UserPicture

def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def all_users(request):
    users = User.objects.filter(is_active=True)
    return render_to_response('profiles/all.html', locals(), context_instance=RequestContext(request))


def single_user(request, username):
    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404

    return render_to_response('profiles/single_user.html', locals(), context_instance=RequestContext(request))


def edit_profile(request):
    user = request.user

    address = Address.objects.get(user=user)
    job = Job.objects.get(user=user)
    user_picture = UserPicture.objects.get(user=user)

    address_form = AddressForm(request.POST or None, prefix="address", instance=address)
    job_form = JobForm(request.POST or None, prefix="job", instance=job)
    user_picture_form = UserPictureForm(request.POST or None, prefix="pic", instance=user_picture)

    if address_form.is_valid() and job_form.is_valid() and user_picture_form.is_valid():
        form1 = address_form.save(commit=False)
        form1.save()

        form2 = job_form.save(commit=False)
        form2.save()

        form3 = user_picture_form.save(commit=False)
        form3.save()

    return render_to_response('profiles/edit_profile.html', locals(), context_instance=RequestContext(request))