from django import forms
from app1.models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email','image', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)  # Don't commit yet to avoid saving twice
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user