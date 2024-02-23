from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required':'champ obligatoire'}, label="Entrer votre pseudo", max_length=200,widget=forms.TextInput(attrs={'class':'form-control email forms-ctr'}))
    password = forms.CharField(error_messages={'required':'champ obligatoire'}, label="Mot de passe", max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control pawword forms-ctr' }))

class SubscribForm(forms.Form):
    username = forms.CharField(error_messages={'required':'champ obligatoire'},label="Entrer votre pseudo", max_length=200,widget=forms.TextInput(attrs={'class':'form-control email forms-ctr'}))
    email = forms.CharField(error_messages={'required':'champ obligatoire'},label="Entrer votre email", max_length=200,widget=forms.TextInput(attrs={'class':'form-control email forms-ctr'}))
    first_name = forms.CharField(error_messages={'required':'champ obligatoire'},label="Entrer votre Nom", max_length=200,widget=forms.TextInput(attrs={'class':'form-control email forms-ctr'}))
    last_name = forms.CharField(error_messages={'required':'champ obligatoire'},label="Entrer votre Prenom", max_length=200,widget=forms.TextInput(attrs={'class':'form-control email forms-ctr'}))    
    password = forms.CharField(error_messages={'required':'champ obligatoire'},label="Entrer votre mot de passe", max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control pawword forms-ctr' }))
    passwordc = forms.CharField(error_messages={'required':'champ obligatoire'},label="Entrer votre mot de passe de confirmation", max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control pawword forms-ctr' }))
