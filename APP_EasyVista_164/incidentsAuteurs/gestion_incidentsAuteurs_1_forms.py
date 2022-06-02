"""Gestion des formulaires avec WTF pour les personnes
Fichier : gestion_personnes_1_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormAddDemandeAuteur(FlaskForm):
    """
        Dans le formulaire "categories_ajouter_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_personne_regexp = ""
    nom_demandeAuteur_add_1 = StringField("nom de la demande ", widget=TextArea())

    submit = SubmitField("Enregistrer la demande")


class FormUpdateDemandeAuteur(FlaskForm):
    """
        Dans le formulaire "demandeAuteur_update_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_demandeAuteur_update = StringField("Clavioter le nom", widget=TextArea())
    numero_demandeAuteur_update = IntegerField("clavioter le numero")
    description_demandeAuteur_update = StringField("Clavioter la description", widget=TextArea())


    submit = SubmitField("Update demande")


class FormDeleteDemandeAuteur(FlaskForm):
    """
        Dans le formulaire "demandeAuteur_delete_1.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_personne_delete_1 = StringField("Effacer cette demande")
    submit_btn_del_demande = SubmitField("Effacer demande")
    submit_btn_conf_del_demande = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
