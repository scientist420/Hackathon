from django import forms
from .models import Hackathon

class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = [
            'title',
            'description',
            'background_image',
            'hackathon_image',
            'registered_users',
            'Submission_Type',  # Corrected field name
            'start_date',       # Corrected field name
            'end_date',         # Corrected field name
            'reward_prize',
            'created_by',
        ]
class RegistrationForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = Hackathon
        fields = ['title', 'description', 'background_image', 'hackathon_image', 'Submission_Type', 'start_date', 'end_date', 'reward_prize']