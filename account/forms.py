from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


def send_activation_mail(email, activation_code):
    message = f'http://localhost:2000/accounts/activation/?u={activation_code}'
    send_mail('Активация аккаунта', message, 'test@gmail.com', [email])


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(min_length=8,
                               widget=forms.PasswordInput,
                               required=True)
    password_confirm = forms.CharField(min_length=8,
                                       widget=forms.PasswordInput,
                                       required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('уже зареган')
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.pop('password_confirm')
        if password !=password_confirm:
            raise forms.ValidationError('не совподябт пароли')
        return self.cleaned_data

    def save(self):
        user = User.objects.create(**self.cleaned_data)
        user.create_activation_code()
        send_activation_mail(user.email, user.activation_code)
        return user


class ChangePasswordForm:
    pass


class ForgotPasswordForm:
    pass
