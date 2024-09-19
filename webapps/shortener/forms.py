# shortener/forms.py
from django import forms
from .models import URL

class URLForm(forms.ModelForm):
    custom_url = forms.CharField(max_length=10, required=False, label="Custom Short URL") 
    expiry_date = forms.DateTimeField(required=False, label="Expiry Date", widget=forms.SelectDateWidget)  

    class Meta:
        model = URL
        fields = ['original_url', 'custom_url', 'expiry_date'] 
