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
from APP_EasyVista_164.demandes.gestion_demandes_1_forms import FormUpdateDemande, FormAddDemande, FormDeleteDemande

"""Ajouter un film grâce au formulaire "demande_add_1.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "personnes/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/demande_add_1", methods=['GET', 'POST'])
def demande_add_1():
    # Objet formulaire pour AJOUTER un film
    form_add_demande = FormAddDemande()
    if request.method == "POST":
        try:
            if form_add_demande.validate_on_submit():
                nom_demande_add = form_add_demande.nom_demande_add_1.data

                valeurs_insertion_dictionnaire = {"value_nom_demande": nom_demande_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_demande = """INSERT INTO t_demande (id_demande,nom_demande) VALUES (NULL,%(value_nom_demande)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_demande, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau film (id_film_sel=0 => afficher tous les personnes)
                return redirect(url_for('demandes_attribuer_personnes_afficher', id_demande_sel=0))

        except Exception as Exception_personne_ajouter_1:
            raise strsql_insert_personne(f"fichier : {Path(__file__).name}  ;  "
                                            f"{demande_add_1.__name__} ; "
                                            f"{Exception_personne_ajouter_1}")

    return render_template("demandes/demande_add_1.html", form_add_demande=form_add_demande)


"""Editer(update) un film qui a été sélectionné dans le formulaire "demandes_attribuer_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "categories_afficher.html"

Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "personnes/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/demande_update", methods=['GET', 'POST'])
def demande_update_1():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_film"
    id_demande_update = request.values['id_demande_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_demande = FormUpdateDemande()
    try:
        print(" on submit ", form_update_demande.validate_on_submit(), "  ", form_update_demande.validate())
        if form_update_demande.validate_on_submit():
            # Récupèrer la valeur du champ depuis "categorie_update_1.html" après avoir cliqué sur "SUBMIT".
            nom_demande_update = form_update_demande.nom_demande_update.data
            numero_demande_update = form_update_demande.numero_demande_update.data
            description_demande_update = form_update_demande.description_demande_update.data
            

            valeur_update_dictionnaire = {"value_id_demande": id_demande_update,
                                          "value_nom_demande": nom_demande_update,
                                          "value_numero_demande": numero_demande_update,
                                          "value_description_demande_update": description_demande_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_demande = """UPDATE t_demande SET nom_demande = %(value_nom_demande)s,
                                                            numero_demande = %(value_numero_demande)s,
                                                            description_demande = %(value_description_demande_update)s
                                                            WHERE id_demande = %(value_id_demande)s
                                                            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_demande, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_film_update"
            return redirect(url_for('demandes_attribuer_personnes_afficher', id_demande_sel=id_demande_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_film" et "intitule_genre" de la "t_genre"
            str_sql_id_personne = "SELECT * FROM t_demande WHERE id_demande = %(value_id_demande)s"
            valeur_select_dictionnaire = {"value_id_demande": id_demande_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_personne, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_demande = mybd_conn.fetchone()
            print("data_demande ", data_demande, " type ", type(data_demande), " personne ",
                  data_demande["nom_demande"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "demande_update_1.html"
            form_update_demande.numero_demande_update.data = data_demande["nom_demande"]
            print(f" dta personne  ", data_demande["nom_demande"])
            form_update_demande.numero_demande_update.data = data_demande["numero_demande"]
            print(f" date de naiss personne  ", data_demande["numero_demande"], "  type ", type(data_demande["numero_demande"]))


    except Exception as Exception_demande_update_1:
        raise ExceptionDemandeUpdate(f"fichier : {Path(__file__).name}  ;  "
                                     f"{demande_update_1.__name__} ; "
                                     f"{Exception_demande_update_1}")

    return render_template("demandes/demande_update_1.html", form_update_demande=form_update_demande)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "demandes_attribuer_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "personnes/demande_delete_1.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/demande_delete", methods=['GET', 'POST'])
def demande_delete_1():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_demande_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_film"
    id_demande_delete = request.values['id_demande_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_demande = FormDeleteDemande()
    try:
        # Si on clique sur "ANNULER", afficher tous les personnes.
        if form_delete_demande.submit_btn_annuler.data:
            return redirect(url_for("demandes_attribuer_personnes_afficher", id_demande_sel=0))

        if form_delete_demande.submit_btn_conf_del_demande.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "personnes/demande_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_demande_delete = session['data_demande_delete']
            print("data_demande_delete ", data_demande_delete)

            flash(f"Effacer la demande de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_demande.submit_btn_del_demande.data:
            valeur_delete_dictionnaire = {"value_id_demande": id_demande_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_demande_attribuer_personne = """DELETE FROM t_pers_attribuer_dem WHERE FK_demande = %(value_id_demande)s"""
            str_sql_delete_demande = """DELETE FROM t_demande WHERE id_demande = %(value_id_demande)s"""
            # Manière brutale d'effacer d'abord la "fk_film", même si elle n'existe pas dans la "t_genre_film"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_demande_attribuer_personne, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_demande, valeur_delete_dictionnaire)

            flash(f"demande définitivement effacé !!", "success")
            print(f"demande définitivement effacé !!")

            # afficher les données
            return redirect(url_for('demandes_attribuer_personnes_afficher', id_demande_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_demande": id_demande_delete}
            print(id_demande_delete, type(id_demande_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_personne_attribuer_demande_delete = """SELECT * FROM t_demande WHERE id_demande = %(value_id_demande)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute( str_sql_personne_attribuer_demande_delete, valeur_select_dictionnaire)
                data_demande_delete = mydb_conn.fetchall()
                print("data_demande_delete...", data_demande_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "personnes/demande_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_demande_delete'] = data_demande_delete

            # Le bouton pour l'action "DELETE" dans le form. "demande_delete_1.html" est caché.
            btn_submit_del = False

    except Exception as Exception_demande_delete_1:
        raise ExceptionDemandeDelete(f"fichier : {Path(__file__).name}  ;  "
                                     f"{demande_delete_1.__name__} ; "
                                     f"{Exception_demande_delete_1}")

    return render_template("demandes/demande_delete_1.html",
                           form_delete_demande=form_delete_demande,
                           btn_submit_del=btn_submit_del,
                           data_demande_del=data_demande_delete
                            )
