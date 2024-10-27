# forms.py
from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    EXAM_TIME_CHOICES = [
        ('09:00:00', 'Forenoon (9 AM)'),
        ('13:00:00', 'Afternoon (1 PM)'),
    ]

    exam_time = forms.ChoiceField(choices=EXAM_TIME_CHOICES)

    class Meta:
        model = Exam
        fields = ['subject_name', 'subject_code', 'exam_date', 'exam_time', 'semester', 'exam_slot']
