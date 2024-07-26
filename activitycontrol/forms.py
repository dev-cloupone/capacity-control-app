from django import forms

class ActivityControlForm(forms.ModelForm):
    date = forms.DateField()
    dateStart = forms.TimeField()
    dateEnd = forms.TimeField()
    activity = forms.CharField(max_length=100)
    description = forms.CharField(max_length=255)
    total = forms.FloatField()