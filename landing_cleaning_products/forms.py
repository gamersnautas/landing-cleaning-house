from django import forms

class ZipCodeForm(forms.Form):
    zipcode = forms.CharField(
        required=True,
        min_length=4,
        max_length=5,
        label="Type your zip code",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id': 'zipcode',
            }
        )
    )