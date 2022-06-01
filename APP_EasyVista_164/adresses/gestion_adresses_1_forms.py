"""
    Fichier : gestion_categories_1_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormAjouterAdresse(FlaskForm):
    """
        Dans le formulaire "adresses_ajouter_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_categorie_regexp = ""
    nom_adresse_1 = StringField("Clavioter l'adresse ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_categorie_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Enregistrer adresse")


class FormUpdateAdresse(FlaskForm):
    """
        Dans le formulaire "adresse_update_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_categorie_update_regexp = ""
    nom_adresse_update_1 = StringField("Clavioter l'adresse ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_categorie_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    NPA_adresse_1 = IntegerField("NPA")
    ville_adresse_1 = StringField("Clavioter la ville", widget=TextArea())

    submit = SubmitField("Update adresse")


class FormDeleteAdresse(FlaskForm):
    """
        Dans le formulaire "adresse_delete_1.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_adresse_delete_1 = StringField("Effacer cette adresse")
    submit_btn_del = SubmitField("Effacer adresse")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
