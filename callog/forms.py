from django import forms
from callog.models import WeighIn


class WeighInForm(forms.models.ModelForm):

    class Meta:
        model = WeighIn
        fields = ('date', 'pounds')
