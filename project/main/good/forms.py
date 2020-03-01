from django.forms import ModelForm

from good.models import good


class GoodForm(ModelForm):
    class Meta:
        model = good
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GoodForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
