from django.forms import ModelForm
from .models import djangoClasses

class infoForm(ModelForm):
    class Meta:
        model = djangoClasses
        fields = '__all__'
