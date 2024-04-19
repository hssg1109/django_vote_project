from django import forms
from .models import Poll,Choice

class ChocieCreateForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ['choiceText',]

class PollCreateForm(forms.ModelForm):
    questionText = forms.CharField(required="required", max_length=200)  # Field name made lowercase.
    pollImage = forms.ImageField(max_length=50)  # Field name made lowercase.
    expireDate = forms.DateField(required="required")  # Field name made lowercase.
    secretPoll = forms.BooleanField(required="required")  # Field name made lowercase.

    class Meta:
        model=Poll
        fields = ['questionText','pollImage','expireDate','secretPoll',]




