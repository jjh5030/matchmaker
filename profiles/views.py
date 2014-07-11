from django.shortcuts import render, render_to_response, RequestContext, Http404
from django.contrib.auth.models import User

from forms import JobForm, AddressForm, UserPictureForm
from .models import Job, Address, UserPicture

from django.forms.models import modelformset_factory

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
    user_picture = UserPicture.objects.get(user=user)

    user_picture_form = UserPictureForm(request.POST or None, prefix="pic", instance=user_picture)

    if user_picture_form.is_valid():
        form3 = user_picture_form.save(commit=False)
        form3.save()

    return render_to_response('profiles/edit_profile.html', locals(), context_instance=RequestContext(request))


def edit_address(request):
    user = request.user
    addresses = Address.objects.filter(user=user)

    address_formset = modelformset_factory(Address, form=AddressForm, extra=1, max_num=5)
    formset_a = address_formset(request.POST or None, queryset=addresses)

    if formset_a.is_valid():
        pass
    return render_to_response('profiles/edit_address.html', locals(), context_instance=RequestContext(request))


def edit_job(request):
    user = request.user
    jobs = Job.objects.filter(user=user)

    job_formset = modelformset_factory(Job, form=JobForm, extra=1, max_num=5)
    formset_j = job_formset(request.POST or None, queryset=jobs)

    if formset_j.is_valid():
        pass

    return render_to_response('profiles/edit_job.html', locals(), context_instance=RequestContext(request))