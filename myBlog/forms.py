from django import forms
from tandegna.models import *
from django.forms import ModelForm

#from django.core.exceptions import ValidationError
#from tandegna.models import ArticlePhoto
#from django.core import validators

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))

class InscriptionForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    passwordC = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs ={'class':'form-control '}))
    #validators=[validators.RegexValidator(message='invalid email')],
    typecompte = (('client','client'),('prestateur','prestateur'))
    typeCompte = forms.ChoiceField(widget=forms.Select(attrs={'class':"form-control"}), choices=typecompte)
    telephone = forms.CharField(min_length=10, max_length=10, widget=forms.NumberInput(attrs={'class':"form-control"}))
    check = forms.CharField(widget=forms.CheckboxInput(attrs={'check':True}))


class EmailForm(forms.Form):
     recipient = forms.EmailField()
     message = forms.CharField(widget=forms.Textarea)


class StockForm(forms.Form):
     nombre = forms.CharField(widget=forms.NumberInput(attrs={"id":"inputStock", "class":"form-control","min":"1","max":"1000"}))
     choicesUnites = (('kg','kg'),('nombre','nombre',),('mètre','mètre'),('litre','litre',))
     unites = forms.CharField(widget=forms.Select(attrs={"id":"inputStock", 'class':'form-control'}, choices=choicesUnites))

class ArticlePhotoViewEdit(forms.ModelForm):
    class Meta:
        model = ArticlePhoto
        fields = ['image1','image2','image3','image4']
     
   


    # , widget=forms.NumberInput(attrs={'class':"form-control"})) 
    

class ArticleForm(forms.Form):
    choices = (('',''),('Landrace','Landrace',),('Large-White','Large-White'),('Middle_White','Middle-White',),('Omby_Manga','Omby Manga',),('Omby_Mena','Omby Mena',))
    districtChoices=(("AMBOHIDRATRIMO","AMBOHIDRATRIMO"),("ANDRAMASINA","ANDRAMASINA"),("ANJOZOROBE","ANJOZOROBE"),("ANKAZOBE","ANKAZOBE"),("ANTANANARIVO ATSIMONDRANO","ANTANANARIVO ATSIMONDRANO"),("ANTANANARIVO AVARADRANO","ANTANANARIVO AVARADRANO"),("ANTANANARIVO RENIVOHITRA","ANTANANARIVO RENIVOHITRA"),("13","MANJAKANDRIANA"),("14","FENOARIVOBE"),("15","TSIROANOMANDIDY"),("16","ARIVONIMAMO"),("MIARINARIVO","MIARINARIVO"),("SOAVINANDRIANA","SOAVINANDRIANA"),("AMBATOLAMPY","AMBATOLAMPY"),("ANTANIFOTSY","ANTANIFOTSY"),("ANTSIRABE I","ANTSIRABE I"),("ANTSIRABE II","ANTSIRABE II"),("BETAFO","BETAFO"),("FARATSIHO","FARATSIHO"),("25","MANDOTO"),("AMBANJA","AMBANJA"),("AMBILOBE","AMBILOBE"),("ANTSIRANANA I","ANTSIRANANA I"),("ANTSIRANANA II","ANTSIRANANA II"),("NOSY-BE","NOSY-BE"),("ANDAPA","ANDAPA"),("ANTALAHA","ANTALAHA"),("SAMBAVA","SAMBAVA"),("VOHEMAR","VOHEMAR"),("AMBATOFINANDRAHANA","AMBATOFINANDRAHANA"),("AMBOSITRA","AMBOSITRA"),("FANDRIANA","FANDRIANA"),("MANANDRIANA","MANANDRIANA"),("BEFOTAKA ATSIMO","BEFOTAKA ATSIMO"),("FARAFANGANA","FARAFANGANA"),("MIDONGY SUD","MIDONGY SUD"),("VANGAINDRANO","VANGAINDRANO"),("VONDROZO","VONDROZO"),("AMBALAVAO","AMBALAVAO"),("AMBOHIMAHASOA","AMBOHIMAHASOA"),("FIANARANTSOA","FIANARANTSOA"),("ISANDRA","ISANDRA"),("IKALAMAVONY","IKALAMAVONY"),("VOHIBATO","VOHIBATO"),("LALANGINA","LALANGINA"),("IAKORA","IAKORA"),("IHOSY","IHOSY"),("IVOHIBE","IVOHIBE"),("IFANADIANA","IFANADIANA"),("IKONGO","IKONGO"),("MANAKARA","MANAKARA"),("MANANJARY","MANANJARY"),("NOSY VARIKA","NOSY VARIKA"),("VOHIPENO","VOHIPENO"),("KANDREHO","KANDREHO"),("MAEVATANANA","MAEVATANANA"),("TSARATANANA","TSARATANANA"),("AMBATO BOENI","AMBATO BOENI"),("MAHAJANGA I","MAHAJANGA I"),("MAHAJANGA II","MAHAJANGA II"),("MAROVOAY","MAROVOAY"),("MITSINJO","MITSINJO"),("SOALALA","SOALALA"),("AMBATOMAINTY","AMBATOMAINTY"),("ANTSALOVA","ANTSALOVA"),("BESALAMPY","BESALAMPY"),("MAINTIRANO","MAINTIRANO"),("MORAFENOBE","MORAFENOBE"),("ANALALAVA","ANALALAVA"),("ANTSOHIHY","ANTSOHIHY"),("BEALANANA","BEALANANA"),("BEFANDRIANA NORD","BEFANDRIANA NORD"),("MAMPIKONY","MAMPIKONY"),("MANDRITSARA","MANDRITSARA"),("PORT-BERGE","PORT-BERGE"),("81","AMBATONDRAZAKA"),("82","AMPARAFARAVOLA"),("ANDILAMENA","ANDILAMENA"),("84","ANOSIBE AN'ALA"),("MORAMANGA","MORAMANGA"),("86","FENERIVE EST"),("MANANARA-NORD","MANANARA-NORD"),("MAROANTSETRA","MAROANTSETRA"),("SAINTE MARIE","SAINTE MARIE"),("SOANIERANA IVONGO","SOANIERANA IVONGO"),("VAVATENINA","VAVATENINA"),("ANTANAMBAO MANAMPONTSY","ANTANAMBAO MANAMPONTSY"),("BRICKAVILLE","BRICKAVILLE"),("MAHANORO","MAHANORO"),("MAROLAMBO","MAROLAMBO"),("TOAMASINA I","TOAMASINA I"),("TOAMASINA II","TOAMASINA II"),("VATOMANDRY","VATOMANDRY"),("AMBOVOMBE ANDROY","AMBOVOMBE ANDROY"),("BEKILY","BEKILY"),("BELOHA ANDROY","BELOHA ANDROY"),("TSIHOMBE","TSIHOMBE"),("AMBOASARY SUD","AMBOASARY SUD"),("BETROKA","BETROKA"),("TAOLANARO","TAOLANARO"),("AMPANIHY OUEST","AMPANIHY OUEST"),("ANKAZOABO SUD","ANKAZOABO SUD"),("BENENITRA","BENENITRA"),("BEROROHA","BEROROHA"),("BETIOKY SUD","BETIOKY SUD"),("MOROMBE","MOROMBE"),("SAKARAHA","SAKARAHA"),("TOLIARA I","TOLIARA I"),("TOLIARA II","TOLIARA II"),("BELO SUR TSIRIBIHINA","BELO SUR TSIRIBIHINA"),("MAHABO","MAHABO"),("MANJA","MANJA"),("MIANDRIVAZO","MIANDRIVAZO"),("MORONDAVA","MORONDAVA"))
    regionsChoices = (('Alaotra-Mangoro','Alaotra-Mangoro',),('Amoron’i Mania','Amoron’i Mania'),('Analamanga','Analamanga'),('Analanjirofo','Analanjirofo'),('Androy','Androy'),('Anôsy','Anôsy'),('Atsimo-Andrefana','Atsimo-Andrefana'),('Atsimo-Atsinanana','Atsimo-Atsinanana'),('9','Atsinanana'),('Betsiboka','Betsiboka'),('Boeny','Boeny'),('Bongolava','Bongolava'),('Diana','Diana'),('Fitovinany','Fitovinany'),('Haute Matsiatra','Haute Matsiatra'),('Ihorombe','Ihorombe'),('Itasy','Itasy'),('Melaky','Melaky'),('Menabe','Menabe'),('Sava','Sava'),('Vakinankaratra','Vakinankaratra'),('Vatovavy','Vatovavy'))
    optype = (('Porc','Porc',),('Boeuf','Boeuf',),('Provende','Provende',),('Autres','Autres',))
    titre = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    race = forms.ChoiceField(widget=forms.Select(attrs={'class':"form-control"}), choices=choices)
    ages = forms.CharField(max_length="2",error_messages={'required':'L age ne doit être vide'}, widget=forms.NumberInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control '}))
    poids = forms.CharField(max_length="2",widget=forms.NumberInput(attrs={'class':'form-control numberInput1'}))
    optionsChoices = (('Offre','Offre',),('Demande','Demande',))
    options = forms.ChoiceField(choices=optionsChoices, widget=forms.Select(attrs={'class':'form-control'}))
    categories = forms.ChoiceField(choices=optype, widget=forms.Select(attrs={'class':"form-control"}))
    regions = forms.ChoiceField( choices=regionsChoices, widget=forms.Select(attrs={'class':"form-control","id":"regions"}))    
    district = forms.ChoiceField(choices=districtChoices, widget=forms.Select(attrs={'class':'form-control'}))
    communes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    adresseComplet = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'IIIS 226 AB ter J Namontana Madera'}))
    prix = forms.CharField(widget = forms.NumberInput(attrs={"class":"form-control","placeholder":"20 000Ar"}))
    telephone = forms.CharField(widget = forms.NumberInput(attrs={"class":"form-control", "min":"10","max":"10"}))
    telephoneB = forms.CharField(widget = forms.NumberInput(attrs={"class":"form-control", "min":"10","max":"10"}))

   # user_id= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'IIIS 226 AB ter J Namontana Madera', 'type':'hidden'}))
    #images = forms.CharField(widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': True}))
    #created=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    #created_by=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))



class ArticlePhotoForm(forms.Form):
        image1 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
        image2 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
        image3 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
        image4 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
# class ArticlePhotoForm(forms.ModelForm):
#    class Meta:
#        model = ArticlePhoto
#        fields = ('image1','image2','image3','image4')
#        widgets = {
#            'image1': forms.FileInput(attrs={'class':'form-control','id':'file1','onchange':'return fileValidation()'}),
#            'image2': forms.FileInput(attrs={'class':'form-control','id':'file2','onchange':'return fileValidation_1()'}),
#            'image3': forms.FileInput(attrs={'class':'form-control','id':'file3','onchange':'return fileValidation_2()'}),
#            'image4': forms.FileInput(attrs={'class':'form-control','id':'file4','onchange':'return fileValidation_3()'})
 #       }