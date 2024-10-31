from django import forms

class PartnerForm(forms.ModelForm):
    partnerCode = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    partnerType = models.CharField(max_length=2)
    nationalId = models.CharField(max_length=20)
    address = models.CharField(max_length=255)