from django import forms



def validate_long_value(value):
    if len(value) >= 50:
        raise forms.ValidationError(
            'Слишком много символов.',
            params={'value': value},
        )