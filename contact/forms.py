# flake8: noqa

from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(
        attrs={'accept': 'image/*'}), help_text='Put a image here', required=False)

    # self.fields['first_name'].widget.attrs.update({
    #     'class': 'classe-a classe-b',
    #     'placeholder': 'Aqui veio do init',
    # })

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category', 'picture',)

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                "The first name can't be equal last name",
                code='Invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error('first_name',
                           ValidationError(
                               message='Came from add',
                               code='Invalid')
                           )
        return first_name
