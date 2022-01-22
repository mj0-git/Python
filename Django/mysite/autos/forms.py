from django.db.models import fields
from django.forms import ModelForm
from autos.models import Make

class MakeForm(ModelForm):
    class Meta: 
        model = Make
        fields = '__all__'
