from django.urls import path
from tandegna.views import *
from conversation.views import *
from . import views

handler404 = views.handler404
#handler500 = views.handler500

urlpatterns = [
    path('montuple/', montuple,name="montuple"),
    path('', home, name="home"),
    path('existePhoto/<int:lastId>',existePhoto,name="existePhoto"),
    path('mailTandegna/',mailTandegna, name="mailTandegna"),
    path('conversation/', conversation, name="conversation"),
    #path('<str:slug><int:id>', details_tandegna, name="details_tandegna"),
    path('login_tandegna/', login_tandegna, name="login_tandegna"),
    path('inscription_tandegna/', inscription_tandegna, name="inscription_tandegna"),
    path('deconnexion/', logout_tandegna , name="logout_tandegna"),
    path('mon_compte/<str:slug><int:id>', mon_compte, name="mon_compte"),
    path('insertion_du_produit/Produits/', insertion_du_produit , name="insertion_du_produit"),
    path('insertion_du_produit/ArticlePhotoView/<int:lastId>', ArticlePhotoView , name="ArticlePhotoView"),
    path('insertion_du_produit/ArticlePhotoViewEdit/<id>', ArticlePhotoViewEdit , name="ArticlePhotoViewEdit"),
    path('insertion_du_produit/insertion_du_produit_edit/', insertion_du_produit_edit , name="insertion_du_produit_edit"),
    path('filtreTandegna/',filtreTandegna, name="filtreTandegna"),
    path('insertion_du_produit/Stock/<int:lastId>', stockArticle , name="stockArticle"),
    path('myAdmin/', myAdmin, name="myAdmin"),
    path('listeAdmin/', listeAdmin, name="listeAdmin"),
    path('OffreTandegna/', OffreTandegna, name="OffreTandegna"),
    path('DemandeTandegna/', DemandeTandegna,  name="DemandeTandegna"),
    path('details_tandegna/<str:slug><int:id>', details_tandegna, name="details_tandegna"),
    path('mode_Tandegna/', mode_Tandegna , name='mode_Tandegna'),
    path('detailsAdmin', detailsAdmin, name="detailsAdmin"),
    path('home/recherche', rechercheTandegna, name="rechercheTandegna"),
    path('home/details_tandegna/<str:slug><int:id>', details_tandegna, name="rechercheTandegna"),
    ]







