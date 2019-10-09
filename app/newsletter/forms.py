from django import forms
from .models import Subscriber

class NewSubscriberFrom(forms.Modelform):
    class meta:
        model = Subscriber
        fields = ['name', 'email']


