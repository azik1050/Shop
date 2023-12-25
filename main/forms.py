from django import forms
from .models import ProductCartItem, Product


class ProductCartItemForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter quantity'
    }))
    class Meta:
        model = ProductCartItem
        fields = ('quantity',)



class ProductUpdateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter title'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'massage-bt',
        'placeholder': 'Enter description'
    }))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter price'
    }))
    total = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter total number'
    }))
    color = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter color'
    }))
    material = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email-bt',
        'placeholder': 'Enter material'
    }))
    class Meta:
        model = Product
        fields = ('title', 'description', 'text', 'price', 'total', 'image', 'is_active', 'color', 'material')



