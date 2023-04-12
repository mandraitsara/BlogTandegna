from django.urls import path
from tandegna.views import *
from conversation.views import *
from . import views

urlpatterns = [
    path('', home, name="home"),  
    path('<str:user_id>', conversation, name="conversation"),
    path('<int:id>', details_tandegna, name="details_tandegna"),
    path('login_tandegna/', login_tandegna, name="login_tandegna"),
    path('inscription_tandegna/', inscription_tandegna, name="inscription_tandegna"),
    path('deconnexion/', logout_tandegna , name="logout_tandegna"),
    path('insertion_du_produit/', insertion_du_produit , name="insertion_du_produit"),
    path('insertion_du_produit/stock', stockArticle , name="stockArticle"),
    path('myAdmin/', myAdmin, name="myAdmin"),
    path('insertion_du_produit/<int:lastId>', ArticlePhotoP, name="ArticlePhotoP"),
    path('listeAdmin/', listeAdmin, name="listeAdmin"),
    path('ArticlePhoto/', ArticlePhotoP, name="ArticlePhotoP"),
    path('OffreTandegna/', OffreTandegna, name="OffreTandegna"),
    path('DemandeTandegna/', DemandeTandegna,  name="DemandeTandegna"),
    path('details_tandegna/<int:id>',details_tandegna, name="details_tandegna"),
    path('mode_Tandegna/', mode_Tandegna , name='mode_Tandegna'),    
    path('detailsAdmin', detailsAdmin, name="detailsAdmin")   
    ]