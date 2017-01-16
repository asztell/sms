from .models import Profile
from django import forms
from django.utils.translation import ugettext_lazy as _



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # course = forms.ChoiceField(widget=forms.RadioSelect, choices=COURSE)
        labels = {
            'username': _('Phone #')
        }
        fields = [
            'username',
            'password',
            'course',
        ]