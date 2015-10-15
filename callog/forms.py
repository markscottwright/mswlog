from django import forms
from django.core.exceptions import ValidationError
from bootstrap3_datetime.widgets import DateTimePicker
from callog.models import WeighIn


class WeighInForm(forms.models.ModelForm):

    class Meta:
        model = WeighIn
        fields = ('date', 'pounds')
        widgets = {
            'date': DateTimePicker(
                options={
                    'format': 'YYYY-MM-DD',
                    'picktime': False})
        }

    def clean_pounds(self):
        pounds = self.cleaned_data.get('pounds', None)
        self.validate_positive(pounds)
        return pounds

    def validate_positive(self, value):
        if value <= 0.0:
            raise ValidationError("Please enter a weight greater than 0")
