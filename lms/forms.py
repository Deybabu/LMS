from django import forms
from django.contrib.auth.models import User

 
from lms.models import user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    Email=forms.EmailField()

    class Meta():
        model=User
        fields=('Username','First_Name','Last_Name','Email','Password_1','Password_2')
        labels={
            'Password_1':'Password',
            'Password_2':'Confirm Pasword'
        }

class user_profile(forms.ModelForm):
    bio=forms.CharField(required=False)
    teacher='teacher'
    student='student'
    user_types=[
        (teacher,'teacher'),
        (student,'student'),
    ]
    user_type=forms.CharField(required=True,choices=user_types)

    class Meta():
        model=user_profile
        fields=('bio','profile_pic','user_type')
