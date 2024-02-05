from django import forms
from .models import adM

class AcademicDetailsForm(forms.ModelForm):
    class Meta:
        model = adM
        fields = ['adSem', 'at1', 'at2', 'ia1', 'ia2', 'prelim', 'endsem', 'perf']
