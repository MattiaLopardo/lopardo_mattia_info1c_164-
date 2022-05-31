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


class FormAddPersonne(FlaskForm):
    """
        Dans le formulaire "categories_ajouter_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_personne_regexp = ""
    nom_personne_add_1 = StringField("Nom de la Personne ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                               Regexp(nom_personne_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])

    submit = SubmitField("Enregistrer la Personne")


class FormUpdatePersonne(FlaskForm):
    """
        Dans le formulaire "personne_update_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_personne_update_1 = StringField("Clavioter le nom", widget=TextArea())
    prenom_personne_update_1 = StringField("Clavioter le prenom", widget=TextArea())
    date_naiss_personne_update_1 = DateField("Date de naissance", validators=[InputRequired("Date obligatoire"),
                                                                                 DataRequired("Date non valide")])
    FK_mail_personne_update_1 = IntegerField("FK_mail")
    FK_adresse_personne_update = IntegerField("FK_adresse")
    FK_telephone_personne_update = IntegerField("FK_telephone")
    submit = SubmitField("Update Personne")


class FormDeletePersonne(FlaskForm):
    """
        Dans le formulaire "personne_delete_1.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_personne_delete_1 = StringField("Effacer cette personne")
    submit_btn_del_personne = SubmitField("Effacer personne")
    submit_btn_conf_del_personne = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
