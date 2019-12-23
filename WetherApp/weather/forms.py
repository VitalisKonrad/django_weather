from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["name"]
        #Для добаления атрибутов используем TextInput
        widgets = {'name' : TextInput(attrs={'class' : 'form-control',
                                             'name' : 'city',
                                             'id' : 'city',
                                             'placeholder' : 'Введите город'})} #Указываем поле с которым будем работать и его атрибуты
