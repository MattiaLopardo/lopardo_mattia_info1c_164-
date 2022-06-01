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


class FormAddDemande(FlaskForm):
    """
        Dans le formulaire "categories_ajouter_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_personne_regexp = ""
    nom_demande_add_1 = StringField("nom de la demande ", widget=TextArea())

    submit = SubmitField("Enregistrer la demande")


class FormUpdateDemande(FlaskForm):
    """
        Dans le formulaire "demande_update_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_demande_update = StringField("Clavioter le nom", widget=TextArea())
    numero_demande_update = StringField("Clavioter le numero", widget=TextArea())
    description_demande_update = StringField("Clavioter la description", widget=TextArea())


    submit = SubmitField("Update demande")


class FormDeleteDemande(FlaskForm):
    """
        Dans le formulaire "demande_delete_1.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_personne_delete_1 = StringField("Effacer cette demande")
    submit_btn_del_demande = SubmitField("Effacer demande")
    submit_btn_conf_del_demande = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
