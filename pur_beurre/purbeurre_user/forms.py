from django import forms

# connexion form


class ConnectionForm(forms.Form):
    username = forms.EmailField(label="Identifiant : e-mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class AccountForm(ConnectionForm):

    # pwd_confirm = forms.CharField(label="Confirmation mot de passe", widget=forms.PasswordInput)

    # if ConnectionForm.password != pwd_confirm:
    #     raise forms.ValidationError(
    #         "Le mot de passe et la confirmation du mot de passe ne correspondent pas."
    #     )
    first_name = forms.CharField(label="Prénom", max_length=30)
