from django import forms
from .models import Todo


# class TodoForm(forms.Form):
#   text = forms.CharField(max_length=100,
#                         widget=forms.TextInput(attrs={
#                            'placeholder': 'Enter todo e.g. Delete junk files', 'class': 'form-control',
#                           'aria-label': 'Todo', 'aria-describedby': 'add-btn'
#                      }))


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Enter todo e.g. Delete junk files', 'class': 'form-control',
                'aria-label': 'Todo', 'aria-describedby': 'add-btn'
            })
        }
