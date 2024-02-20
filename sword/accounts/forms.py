from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from django.forms import ModelForm

User = get_user_model()  # Get the current user model (CustomUser)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('first_name', 'email','username', 'password1', 'password2')
        labels={
            'first_name':('Name'),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(request=self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid username or password")
        return self.cleaned_data
    
class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields = ['username','email', 'birth_date', 'facebook', 'twitter', 'github', 'bio']  # Exclude the 'user' field