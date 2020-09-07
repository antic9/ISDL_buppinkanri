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

class NewForm(forms.Form):
  TYPE_CHOICES = (
    (1, '書籍'),
    (2, 'デバイス'),
    (3, 'コンピュータ'),
  )
  name = forms.CharField(
    label = '名称',
    max_length = 50,
    required = True,
    widget = forms.TextInput(),
  )
  # eqtype = forms.ChoiceField(
  #   label = '種別',
  #   widget = forms.RadioSelect,
  #   choices = TYPE_CHOICES,
  #   required = True,
  # )
  remark = forms.CharField(
    label = '備考',
    widget = forms.Textarea(),
    required = False,
  )



class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
