from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class user_loginForm(ModelForm):
    pass

class cutomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(cutomUserForm, self).__init__(*args, **kwargs)

        # for labels, fieldname in zip(['Name','Email Adress','Username','Password','Confirm-password'],['first_name', 'email', 'username', 'password1', 'password2']):
        #     self.fields[fieldname].help_text = None
        #     self.fields[fieldname].label = labels

        self.fields['first_name'].widget.attrs.update(
            {
                
                'type':'text',
                'name':'first_name',
                'placeholder':'First Name'

            }
        )

        self.fields['last_name'].widget.attrs.update(
            {
                'type':'text',
                'name':'last_name',
                'placeholder':'Last Name'

            }
        )

        self.fields['username'].widget.attrs.update(
            {
                'type':'text',
                'name':'username',
                'placeholder':'username'

            }
        )

        self.fields['email'].widget.attrs.update(
            {
               
                'type':'email',
                'name':'email',
                'placeholder':'Email Address'

            }
        )

        self.fields['password1'].widget.attrs.update(
            {
                
                'type':'password',
                'name':'password1',
                'placeholder':'Password'

            }
        )

        self.fields['password2'].widget.attrs.update(
            {
                
                'type':'password',
                'name':'password2',
                'placeholder':'Confirm Password'

            }
        )

 