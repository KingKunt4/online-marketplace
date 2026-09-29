from django import forms
from .models import Item

class newItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'input-area'
        }),

            'name': forms.TextInput(attrs={
                        'class': 'input-area'
                }),

            'description': forms.Textarea(attrs={
                        'class': 'input-area'
                }),

            'price': forms.TextInput(attrs={
                        'class': 'input-area'
                }),

            'image': forms.FileInput(attrs={
                        'class': 'input-area'
                }),
        }