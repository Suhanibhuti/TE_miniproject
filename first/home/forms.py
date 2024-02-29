from django import forms
from .models import adM
# from .models import cocuM

class AcademicDetailsForm(forms.ModelForm):
    class Meta:
        model = adM
        fields = ['adSem', 'at1', 'at2', 'ia1', 'ia2', 'prelim', 'endsem', 'perf']


# class CoCurricularForm(forms.ModelForm):
#     class Meta:
#         model = cocuM
#         fields = ['semester', 'professional_society', 'internship', 'paper_published']