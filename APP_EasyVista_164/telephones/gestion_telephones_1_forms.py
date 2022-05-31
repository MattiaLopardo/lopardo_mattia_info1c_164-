"""
    Fichier : gestion_categories_1_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp


class FormAjouterTelephone(FlaskForm):
    """
        Dans le formulaire "telephones_ajouter_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_telephone_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    number_telephone_1 = StringField("Clavioter le numero ")

    submit = SubmitField("Enregistrer telephone")


class FormUpdateTelephone(FlaskForm):
    """
        Dans le formulaire "telephone_update_1.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_mail_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    num_telephone_update_1 = StringField("Clavioter le numero ")

    submit = SubmitField("Update telephone")


class FormDeleteTelephone(FlaskForm):
    """
        Dans le formulaire "telephone_delete_1.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    num_telephone_delete_1 = StringField("Effacer ce numero")
    submit_btn_del = SubmitField("Effacer numero")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
