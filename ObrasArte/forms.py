from django import forms
from .models import Artista, Pintura

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ('nombre', 'edad', 'pinturas')

        def __init__(self, *args, **kwargs):
            super(ArtistaFrom, self).__init__(*args, **kwargs)

            self.fields["pinturas"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["pinturas"].queryset = Pintura.objects.all()

class PinturaForm(forms.ModelForm):
    class Meta:
        model = Pintura
        fields = ('nombre_pintura', 'estilo')
