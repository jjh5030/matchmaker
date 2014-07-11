from django import forms
from .models import Job, Address, UserPicture


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address


class JobForm(forms.ModelForm):
    class Meta:
        model = Job


class UserPictureForm(forms.ModelForm):
    class Meta:
        model = UserPicture