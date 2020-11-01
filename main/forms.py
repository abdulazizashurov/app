from django.forms import ModelForm
from .models import Pupils

class PupilsForm(ModelForm):
    class Meta:
        model = Pupils
        fields = '__all__'