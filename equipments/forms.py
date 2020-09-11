from django import forms
from django.contrib.auth.forms import AuthenticationForm 


class BorrowForm(forms.Form):
  ACTION_CHOICES = (
    ('borrowing', '貸出'),
    ('returning', '返却'),
    # ('extension', 'Extend'),
  )
  action = forms.ChoiceField(
    label = 'Action',
    widget = forms.RadioSelect,
    choices = ACTION_CHOICES,
    required = True,
  )
  name = forms.CharField(
    label = '備考',
    max_length = 50,
    required = False,
    widget = forms.TextInput(),
    #widget = request.user,
  )

class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
