from django import forms
from .models import University, Class, Topic

class FlashcardForm(forms.Form):
    university = forms.CharField(max_length=255, label="University Name")
    class_field = forms.CharField(max_length=255, label="Class Name")
    topic = forms.CharField(max_length=255, required=False, label="Topic (Optional)")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['class_field'].queryset = Class.objects.filter(university_id=university_id).order_by('name')
            except (ValueError, TypeError):
                pass
        if 'class_field' in self.data:
            try:
                class_id = int(self.data.get('class_field'))
                self.fields['topic'].queryset = Topic.objects.filter(class_field_id=class_id).order_by('name')
            except (ValueError, TypeError):
                pass