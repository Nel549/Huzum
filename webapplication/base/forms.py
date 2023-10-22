from .models import Message
from django import forms

class main_form(forms.ModelForm):
    msg = forms.CharField(max_length=300, widget=forms.TextInput(
                              attrs={
                                'class': "msger-inputarea",
                                'placeholder': 'Type something..',
                                'id': 'input_msg',
                                'name': 'input_msg'
                                }))

    class Meta:
        model = Message
        fields = '__all__'
