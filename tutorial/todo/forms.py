from django import forms

from .models import Tasks

class AddTaskForm(forms.ModelForm):
    task = forms.CharField(max_length = 250,
    widget = forms.TextInput(
    attrs = {
    'class' : 'form-control',
    'placeholder' : 'Что нужно добавить?', 
    }
    )
    )

    class Meta:
        model = Tasks
        fields = '__all__'