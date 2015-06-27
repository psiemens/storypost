from django.forms import Form, ModelForm, PasswordInput, CharField, EmailField
from django.contrib.auth.models import User as AuthUser

from codexapp.main.models import User, List, Prompt


class RegistrationForm(ModelForm):

    username = CharField(max_length=50)
    email = EmailField()

    password1 = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password confirmation', widget=PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):

        auth_user = AuthUser(username=self.cleaned_data["username"], email=self.cleaned_data["email"])
        auth_user.set_password(self.cleaned_data["password1"])
        auth_user.save()

        user = super(RegistrationForm, self).save(commit=False)
        user.auth_user = auth_user

        return user.save()

    class Meta:
        model = User
        exclude = ('auth_user',)


class ListForm(ModelForm):
    class Meta:
        model = List
        exclude = ('mc_list_id', 'user')

class PromptForm(ModelForm):
    class Meta:
        model = Prompt
        exclude = ('mc_campaign_id', 'user', 'list')