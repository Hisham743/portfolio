from django import forms


class Mail(forms.Form):
    name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'name': 'name',
                'id': 'name',
                'class': 'col-xs-12 col-sm-12 col-md-12 col-lg-12',
                'placeholder': 'Your name...'
            }
        ),
    )
    email = forms.EmailField(
        max_length=150,
        widget=forms.EmailInput(
            attrs={
                'name': 'email',
                'id': 'email',
                'class': ' col-xs-12 col-sm-12 col-md-12 col-lg-12 noMarr',
                'placeholder': 'Email Address...'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'name': 'comments',
                'id': 'comments',
                'class': 'col-xs-12 col-sm-12 col-md-12 col-lg-12',
                'placeholder': 'Message...'
            }
        )
    )
