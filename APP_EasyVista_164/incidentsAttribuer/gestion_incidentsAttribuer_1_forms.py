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


class FormAddIncidentAttribuer(FlaskForm):
    """
        Dans le formulaire "categories_ajouter_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_personne_regexp = ""
    nom_incidentAttribuer_add_1 = StringField("nom de l'incident ", widget=TextArea())

    submit = SubmitField("Enregistrer l'incident")


class FormUpdateIncidentAttribuer(FlaskForm):
    """
        Dans le formulaire "incidentAttribuer_update_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_incidentAttribuer_update = StringField("Clavioter le nom", widget=TextArea())
    numero_incidentAttribuer_update = IntegerField("clavioter le numero")
    description_incidentAttribuer_update = StringField("Clavioter la description", widget=TextArea())


    submit = SubmitField("Update incident")


class FormDeleteIncidentAttribuer(FlaskForm):
    """
        Dans le formulaire "incidentAttribuer_delete_1.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_personne_delete_1 = StringField("Effacer cet incident")
    submit_btn_del_incidentAtt = SubmitField("Effacer incident")
    submit_btn_conf_del_incidentAtt = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
