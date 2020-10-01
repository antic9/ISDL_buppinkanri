from django.contrib.auth.forms import AuthenticationForm 


class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form'
            field.widget.attrs={'style':'height:35px'}
            field.widget.attrs['placeholder'] = field.label