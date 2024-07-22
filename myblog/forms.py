from django import forms
from django.contrib.auth.models import User


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

#     def send_email(self):
#         print(f"Sending email from {self.cleaned_data['email']} with message: {self.cleaned_data['message']}")

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm_password")

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')

            # check if matches password
            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("passwords do not match")
            return cleaned_data