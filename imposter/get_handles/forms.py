from django import forms
from .models import BaseHandle
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class BaseHandleForm(forms.ModelForm):
    class Meta:
        model = BaseHandle
        fields = ['handle']
        
    def clean_handle(self):
        data = self.cleaned_data['handle']
        twitter_alph = "abcdefghijklmnopqrstuvwxyz0123456789_"
        # Check handle contains only allowed characters
        if not set(data.lower()).issubset(set(twitter_alph)):
            raise ValidationError(_("Sorry, that's an invalid handle, please only use characters that Twitter allows in handles, namely " + twitter_alph))
        return data