from django import forms

class SubscribComplete(forms.Form):
    typecompte = (('client','client'),('prestateur','prestateur'))
    type = forms.CharField(label="chosir votre compte...", max_length=200,widget=forms.Select(attrs={'class':'form-control email forms-ctr'},choices=typecompte),error_messages={'required':'champ obligatoire'})
    pack = forms.CharField(label="votre pack", widget=forms.TextInput(attrs={'class':'form-control email forms-ctr'}))
    phone = forms.CharField(label="phone", widget=forms.NumberInput(attrs={'class':'form-control email forms-ctr'}),error_messages={'required':'champ obligatoire'})

class produitsForm(forms.Form):
    titre = forms.CharField(label="Titre du produit:", max_length=500, widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'champ obligatoire'})
    description = forms.CharField(label="Description du produit:", max_length=500, widget=forms.Textarea(attrs={'class':'form-control'}),error_messages={'required':'champ obligatoire'})
    prix = forms.CharField(label="Prix du produit:", max_length=500, widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'champ obligatoire'})