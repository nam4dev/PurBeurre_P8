from django import forms

# connexion form


class ConnectionForm(forms.Form):
    username = forms.EmailField(label="Identifiant : e-mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class AccountForm(ConnectionForm):
    first_name = forms.CharField(label="Prénom", max_length=30)
    pwd_confirm = forms.CharField(label="pseudo", max_length=30)
