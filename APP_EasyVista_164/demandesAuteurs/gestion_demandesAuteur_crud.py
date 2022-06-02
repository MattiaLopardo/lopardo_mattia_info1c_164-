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
from APP_EasyVista_164.demandesAuteurs.gestion_demandesAuteurs_1_forms import FormUpdateDemandeAuteur, FormAddDemandeAuteur, FormDeleteDemandeAuteur

"""Ajouter un film grâce au formulaire "demandeAuteur_add_1.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "personnes/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/demandeAuteur_add_1", methods=['GET', 'POST'])
def demandeAuteur_add_1():
    # Objet formulaire pour AJOUTER un film
    form_add_demandeAuteur = FormAddDemandeAuteur()
    if request.method == "POST":
        try:
            if form_add_demandeAuteur.validate_on_submit():
                nom_demandeAuteur_add = form_add_demandeAuteur.nom_demandeAuteur_add_1.data

                valeurs_insertion_dictionnaire = {"value_nom_demandeAuteur": nom_demandeAuteur_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_demandeA = """INSERT INTO t_demande (id_demande,nom_demande) VALUES (NULL,%(value_nom_demandeAuteur)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_demandeA, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau film (id_film_sel=0 => afficher tous les personnes)
                return redirect(url_for('demandes_auteurs_personnes_afficher', id_demandeAuteur_sel=0))

        except Exception as Exception_personneAuteur_ajouter_1:
            raise strsql_insert_personneAuteur(f"fichier : {Path(__file__).name}  ;  "
                                            f"{demandeAuteur_add_1.__name__} ; "
                                            f"{Exception_personneAuteur_ajouter_1}")

    return render_template("demandesAuteurs/demandeAuteur_add_1.html", form_add_demandeAuteur=form_add_demandeAuteur)


"""Editer(update) un film qui a été sélectionné dans le formulaire "demandes_auteurs_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "categories_afficher.html"

Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "personnes/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/demandeAuteur_update", methods=['GET', 'POST'])
def demandeAuteur_update_1():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_film"
    id_demandeAuteur_update = request.values['id_demandeAuteur_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_demandeAuteur = FormUpdateDemandeAuteur()
    try:
        print(" on submit ", form_update_demandeAuteur.validate_on_submit(), "  ", form_update_demandeAuteur.validate())
        if form_update_demandeAuteur.validate_on_submit():
            # Récupèrer la valeur du champ depuis "categorie_update_1.html" après avoir cliqué sur "SUBMIT".
            nom_demandeAuteur_update = form_update_demandeAuteur.nom_demandeAuteur_update.data
            numero_demandeAuteur_update = form_update_demandeAuteur.numero_demandeAuteur_update.data
            description_demandeAuteur_update = form_update_demandeAuteur.description_demandeAuteur_update.data
            

            valeur_update_dictionnaire = {"value_id_demandeAuteur": id_demandeAuteur_update,
                                          "value_nom_demandeAuteur": nom_demandeAuteur_update,
                                          "value_numero_demandeAuteur": numero_demandeAuteur_update,
                                          "value_description_demande_update": description_demandeAuteur_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_demandeAuteur = """UPDATE t_demande SET nom_demande = %(value_nom_demandeAuteur)s,
                                                            numero_demande = %(value_numero_demandeAuteur)s,
                                                            description_demande = %(value_description_demande_update)s
                                                            WHERE id_demande = %(value_id_demandeAuteur)s
                                                            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_demandeAuteur, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_film_update"
            return redirect(url_for('demandes_auteurs_personnes_afficher', id_demandeAuteur_sel=id_demandeAuteur_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_film" et "intitule_genre" de la "t_genre"
            str_sql_id_personneAuteur = "SELECT * FROM t_demande WHERE id_demande = %(value_id_demandeAuteur)s"
            valeur_select_dictionnaire = {"value_id_demandeAuteur": id_demandeAuteur_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_personneAuteur, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_demandeAuteur = mybd_conn.fetchone()
            print("data_demandeAuteur ", data_demandeAuteur, " type ", type(data_demandeAuteur), " personneAuteur ",
                  data_demandeAuteur["nom_demande"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "demandeAuteur_update_1.html"
            form_update_demandeAuteur.numero_demandeAuteur_update.data = data_demandeAuteur["nom_demande"]
            print(f" dta personne  ", data_demandeAuteur["nom_demande"])
            form_update_demandeAuteur.numero_demandeAuteur_update.data = data_demandeAuteur["numero_demande"]
            print(f" date de naiss personne  ", data_demandeAuteur["numero_demande"], "  type ", type(data_demandeAuteur["numero_demande"]))


    except Exception as Exception_demandeAuteur_update_1:
        raise ExceptionDemandeAuteurUpdate(f"fichier : {Path(__file__).name}  ;  "
                                     f"{demandeAuteur_update_1.__name__} ; "
                                     f"{Exception_demandeAuteur_update_1}")

    return render_template("demandesAuteurs/demandeAuteur_update_1.html", form_update_demandeAuteur=form_update_demandeAuteur)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "demandes_auteurs_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "personnes/demandeAuteur_delete_1.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/demandeAuteur_delete", methods=['GET', 'POST'])
def demandeAuteur_delete_1():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_demandeAuteur_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_film"
    id_demandeAuteur_delete = request.values['id_demandeAuteur_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_demandeAuteur = FormDeleteDemandeAuteur()
    try:
        # Si on clique sur "ANNULER", afficher tous les personnes.
        if form_delete_demandeAuteur.submit_btn_annuler.data:
            return redirect(url_for("demandes_auteurs_personnes_afficher", id_demandeAuteur_sel=0))

        if form_delete_demandeAuteur.submit_btn_conf_del_demande.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "personnes/demandeAuteur_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_demandeAuteur_delete = session['data_demandeAuteur_delete']
            print("data_demandeAuteur_delete ", data_demandeAuteur_delete)

            flash(f"Effacer la demande de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_demandeAuteur.submit_btn_del_demande.data:
            valeur_delete_dictionnaire = {"value_id_demandeAuteur": id_demandeAuteur_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_demande_auteur_personne = """DELETE FROM t_pers_auteur_dem WHERE FK_demande = %(value_id_demandeAuteur)s"""
            str_sql_delete_demandeAuteur = """DELETE FROM t_demande WHERE id_demande = %(value_id_demandeAuteur)s"""
            # Manière brutale d'effacer d'abord la "fk_film", même si elle n'existe pas dans la "t_genre_film"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_demande_auteur_personne, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_demandeAuteur, valeur_delete_dictionnaire)

            flash(f"demande définitivement effacé !!", "success")
            print(f"demande définitivement effacé !!")

            # afficher les données
            return redirect(url_for('demandes_auteurs_personnes_afficher', id_demandeAuteur_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_demandeAuteur": id_demandeAuteur_delete}
            print(id_demandeAuteur_delete, type(id_demandeAuteur_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_personne_auteur_demande_delete = """SELECT * FROM t_demande WHERE id_demande = %(value_id_demandeAuteur)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute( str_sql_personne_auteur_demande_delete, valeur_select_dictionnaire)
                data_demandeAuteur_delete = mydb_conn.fetchall()
                print("data_demandeAuteur_delete...", data_demandeAuteur_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "personnes/demandeAuteur_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_demandeAuteur_delete'] = data_demandeAuteur_delete

            # Le bouton pour l'action "DELETE" dans le form. "demandeAuteur_delete_1.html" est caché.
            btn_submit_del = False

    except Exception as Exception_demandeAuteur_delete_1:
        raise ExceptionDemandeAuteurDelete(f"fichier : {Path(__file__).name}  ;  "
                                     f"{demandeAuteur_delete_1.__name__} ; "
                                     f"{Exception_demandeAuteur_delete_1}")

    return render_template("demandesAuteurs/demandeAuteur_delete_1.html",
                           form_delete_demandeAuteur=form_delete_demandeAuteur,
                           btn_submit_del=btn_submit_del,
                           data_demande_del=data_demandeAuteur_delete
                            )
