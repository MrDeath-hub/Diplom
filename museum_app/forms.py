from django import forms
from .models import ExcursionRequest

class ExcursionForm(forms.ModelForm):
    class Meta:
        model = ExcursionRequest
        fields = ['full_name', 'email', 'phone', 'desired_date', 'desired_time']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ivan@example.ru'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (123) 456-78-90'}),
            'desired_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'desired_time': forms.Select(attrs={'class': 'form-select'}, choices=[('10:00','10:00'),('12:00','12:00'),('14:00','14:00'),('16:00','16:00')]),
        }

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label='Сообщение')