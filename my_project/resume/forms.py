from django import forms

class ContactMe(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 col-md-4'}),required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'col-12 col-md-4'}),required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 col-md-4'}),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'col-12'}) , required=True)
