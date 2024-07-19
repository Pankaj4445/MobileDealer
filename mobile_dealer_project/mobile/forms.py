from django import forms
from .models import Mobile

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['name', 'brand', 'price', 'RAM', 'ROM', 'battery', 'OS', 'network', 'primary_cam', 'secondary_cam', 'processor', 'quantity']
class BuyMobileForm(forms.Form):
    brand = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    quantity = forms.IntegerField()
