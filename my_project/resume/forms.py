from django import forms
from .models import Form


class ContactMe(forms.ModelForm):
    class Meta : 
        model = Form

        feilds = "__all__"

