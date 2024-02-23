from django import forms

class contactForm(forms.Form):
   email = forms.CharField(label="Entrer votre email pour que nous puissions de vous appelez ou Numero téléphone", max_length=200,widget=forms.TextInput(attrs={'class':'form-control email forms-ctr'}))
   objet = forms.CharField(label="Objet", max_length=200,widget=forms.TextInput(attrs={'class':'form-control email forms-ctr'}))
   message = forms.CharField(label="Messages:", max_length=200,widget=forms.Textarea(attrs={'class':'form-control email forms-ctr'}))