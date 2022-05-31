"""Gestion des "routes" FLASK et des données pour les personnes.
Fichier : gestion_personnes_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import flash, render_template, session
from flask import redirect
from flask import request
from flask import url_for

from APP_EasyVista_164 import app
from APP_EasyVista_164.database.database_tools import DBconnection
from APP_EasyVista_164.erreurs.exceptions import *
from APP_EasyVista_164.personnes.gestion_personnes_1_forms import FormUpdatePersonne, FormAddPersonne, FormDeletePersonne

"""Ajouter un film grâce au formulaire "personne_add_1.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "personnes/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/personne_add_1", methods=['GET', 'POST'])
def personne_add_1():
    # Objet formulaire pour AJOUTER un film
    form_add_personne = FormAddPersonne()
    if request.method == "POST":
        try:
            if form_add_personne.validate_on_submit():
                nom_personne_add = form_add_personne.nom_personne_add_1.data

                valeurs_insertion_dictionnaire = {"value_nom_personne": nom_personne_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_personne = """INSERT INTO t_personne (id_personne,nom_personne) VALUES (NULL,%(value_nom_personne)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_personne, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau film (id_film_sel=0 => afficher tous les personnes)
                return redirect(url_for('personnes_categories_afficher', id_personne_sel=0))

        except Exception as Exception_categorie_ajouter_wtf:
            raise strsql_insert_categorie(f"fichier : {Path(__file__).name}  ;  "
                                            f"{personne_add_1.__name__} ; "
                                            f"{Exception_categorie_ajouter_wtf}")

    return render_template("personnes/personne_add_1.html", form_add_personne=form_add_personne)


"""Editer(update) un film qui a été sélectionné dans le formulaire "personnes_categories_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "categories_afficher.html"

Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "personnes/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/personne_update", methods=['GET', 'POST'])
def personne_update_1():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_film"
    id_personne_update = request.values['id_personne_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_personne = FormUpdatePersonne()
    try:
        print(" on submit ", form_update_personne.validate_on_submit(), "  ", form_update_personne.validate())
        if form_update_personne.validate_on_submit():
            # Récupèrer la valeur du champ depuis "categorie_update_1.html" après avoir cliqué sur "SUBMIT".
            nom_personne_update = form_update_personne.nom_personne_update_1.data
            prenom_personne_update = form_update_personne.prenom_personne_update_1.data
            date_naiss_personne_update = form_update_personne.date_naiss_personne_update_1.data
            FK_mail_personne_update = form_update_personne.FK_mail_personne_update_1.data
            FK_adresse_personne_update = form_update_personne.FK_adresse_personne_update.data
            FK_telephone_personne_update = form_update_personne.FK_telephone_personne_update.data

            valeur_update_dictionnaire = {"value_id_personne": id_personne_update,
                                          "value_nom_personne": nom_personne_update,
                                          "value_prenom_personne": prenom_personne_update,
                                          "value_date_naiss_personne": date_naiss_personne_update,
                                          "value_FK_mail_personne": FK_mail_personne_update,
                                          "value_FK_adresse_personne": FK_adresse_personne_update,
                                          "value_FK_telephone_personne": FK_telephone_personne_update,
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_personne = """UPDATE t_personne SET nom_personne = %(value_nom_personne)s,
                                                            prenom_personne = %(value_prenom_personne)s,
                                                            date_naiss_personne = %(value_date_naiss_personne)s,
                                                            FK_mail = %(value_FK_mail_personne)s,
                                                            FK_adresse = %(value_FK_adresse_personne)s,
                                                            FK_telephone = %(value_FK_telephone_personne)s
                                                            WHERE id_personne = %(value_id_personne)s
                                                            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_personne, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_film_update"
            return redirect(url_for('personnes_categories_afficher', id_personne_sel=id_personne_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_film" et "intitule_genre" de la "t_genre"
            str_sql_id_personne = "SELECT * FROM t_personne WHERE id_personne = %(value_id_personne)s"
            valeur_select_dictionnaire = {"value_id_personne": id_personne_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_personne, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_personne = mybd_conn.fetchone()
            print("data_personne ", data_personne, " type ", type(data_personne), " categorie ",
                  data_personne["nom_personne"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "personne_update_1.html"
            form_update_personne.nom_personne_update_1.data = data_personne["nom_personne"]
            print(f" dta personne  ", data_personne["nom_personne"])
            form_update_personne.prenom_personne_update_1.data = data_personne["prenom_personne"]
            print(f" date de naiss personne  ", data_personne["prenom_personne"], "  type ", type(data_personne["prenom_personne"]))


    except Exception as Exception_personne_update_1:
        raise ExceptionPersonneUpdate(f"fichier : {Path(__file__).name}  ;  "
                                     f"{personne_update_1.__name__} ; "
                                     f"{Exception_personne_update_1}")

    return render_template("personnes/personne_update_1.html", form_update_personne=form_update_personne)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "personnes_categories_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "personnes/personne_delete_1.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/personne_delete", methods=['GET', 'POST'])
def personne_delete_1():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_personne_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_film"
    id_personne_delete = request.values['id_personne_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_personne = FormDeletePersonne()
    try:
        # Si on clique sur "ANNULER", afficher tous les personnes.
        if form_delete_personne.submit_btn_annuler.data:
            return redirect(url_for("personnes_categories_afficher", id_personne_sel=0))

        if form_delete_personne.submit_btn_conf_del_personne.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "personnes/personne_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_personne_delete = session['data_personne_delete']
            print("data_personne_delete ", data_personne_delete)

            flash(f"Effacer la personne de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_personne.submit_btn_del_personne.data:
            valeur_delete_dictionnaire = {"value_id_personne": id_personne_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_personne_categorie = """DELETE FROM t_pers_categorie WHERE FK_personne = %(value_id_personne)s"""
            str_sql_delete_personne = """DELETE FROM t_personne WHERE id_personne = %(value_id_personne)s"""
            # Manière brutale d'effacer d'abord la "fk_film", même si elle n'existe pas dans la "t_genre_film"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_personne_categorie, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_personne, valeur_delete_dictionnaire)

            flash(f"Personne définitivement effacé !!", "success")
            print(f"Personne définitivement effacé !!")

            # afficher les données
            return redirect(url_for('personnes_categories_afficher', id_personne_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_personne": id_personne_delete}
            print(id_personne_delete, type(id_personne_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_categorie_personne_delete = """SELECT * FROM t_personne WHERE id_personne = %(value_id_personne)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute( str_sql_categorie_personne_delete, valeur_select_dictionnaire)
                data_personne_delete = mydb_conn.fetchall()
                print("data_personne_delete...", data_personne_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "personnes/personne_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_personne_delete'] = data_personne_delete

            # Le bouton pour l'action "DELETE" dans le form. "personne_delete_1.html" est caché.
            btn_submit_del = False

    except Exception as Exception_personne_delete_1:
        raise ExceptionPersonneDelete(f"fichier : {Path(__file__).name}  ;  "
                                     f"{personne_delete_1.__name__} ; "
                                     f"{Exception_personne_delete_1}")

    return render_template("personnes/personne_delete_1.html",
                           form_delete_personne=form_delete_personne,
                           btn_submit_del=btn_submit_del,
                           data_personne_del=data_personne_delete
                            )
