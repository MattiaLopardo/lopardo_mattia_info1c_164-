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
from APP_EasyVista_164.incidentsAttribuer.gestion_incidentsAttribuer_1_forms import FormUpdateIncidentAttribuer, FormAddIncidentAttribuer, FormDeleteIncidentAttribuer

"""Ajouter un film grâce au formulaire "incidentAttribuer_add_1.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "personnes/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/incidentAttribuer_add_1", methods=['GET', 'POST'])
def incidentAttribuer_add_1():
    # Objet formulaire pour AJOUTER un film
    form_add_incidentAttribuer = FormAddIncidentAttribuer()
    if request.method == "POST":
        try:
            if form_add_incidentAttribuer.validate_on_submit():
                nom_incidentAttribuer_add = form_add_incidentAttribuer.nom_incidentAttribuer_add_1.data

                valeurs_insertion_dictionnaire = {"value_nom_incidentAttribuer": nom_incidentAttribuer_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_incidentAtt = """INSERT INTO t_incident (id_incident,nom_incident) VALUES (NULL,%(value_nom_incidentAttribuer)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_incidentAtt, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau film (id_film_sel=0 => afficher tous les personnes)
                return redirect(url_for('incidents_attribuer_personnes_afficher', id_incidentAttribuer_sel=0))

        except Exception as Exception_personneIncAttribuer_ajouter_1:
            raise strsql_insert_personneIncAttribuer(f"fichier : {Path(__file__).name}  ;  "
                                            f"{incidentAttribuer_add_1.__name__} ; "
                                            f"{Exception_personneIncAttribuer_ajouter_1}")

    return render_template("incidentsAttribuer/incidentAttribuer_add_1.html", form_add_incidentAttribuer=form_add_incidentAttribuer)


"""Editer(update) un film qui a été sélectionné dans le formulaire "incidents_attribuer_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "categories_afficher.html"

Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "personnes/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/incidentAttribuer_update", methods=['GET', 'POST'])
def incidentAttribuer_update_1():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_film"
    id_incidentAttribuer_update = request.values['id_incidentAttribuer_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_incidentAttribuer = FormUpdateIncidentAttribuer()
    try:
        print(" on submit ", form_update_incidentAttribuer.validate_on_submit(), "  ", form_update_incidentAttribuer.validate())
        if form_update_incidentAttribuer.validate_on_submit():
            # Récupèrer la valeur du champ depuis "categorie_update_1.html" après avoir cliqué sur "SUBMIT".
            nom_incidentAttribuer_update = form_update_incidentAttribuer.nom_incidentAttribuer_update.data
            numero_incidentAttribuer_update = form_update_incidentAttribuer.numero_incidentAttribuer_update.data
            description_incidentAttribuer_update = form_update_incidentAttribuer.description_incidentAttribuer_update.data
            

            valeur_update_dictionnaire = {"value_id_incidentAttribuer": id_incidentAttribuer_update,
                                          "value_nom_incidentAttribuer": nom_incidentAttribuer_update,
                                          "value_numero_incidentAttribuer": numero_incidentAttribuer_update,
                                          "value_description_incidentAttribuer_update": description_incidentAttribuer_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_incidentAttribuer = """UPDATE t_incident SET nom_incident = %(value_nom_incidentAttribuer)s,
                                                            numero_incident = %(value_numero_incidentAttribuer)s,
                                                            description_incident = %(value_description_incidentAttribuer_update)s
                                                            WHERE id_incident = %(value_id_incidentAttribuer)s
                                                            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_incidentAttribuer, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_film_update"
            return redirect(url_for('incidents_attribuer_personnes_afficher', id_incidentAttribuer_sel=id_incidentAttribuer_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_film" et "intitule_genre" de la "t_genre"
            str_sql_id_personneIncAttribuer = "SELECT * FROM t_incident WHERE id_incident = %(value_id_incidentAttribuer)s"
            valeur_select_dictionnaire = {"value_id_incidentAttribuer": id_incidentAttribuer_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_personneIncAttribuer, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_incidentAttribuer = mybd_conn.fetchone()
            print("data_incidentAttribuer ", data_incidentAttribuer, " type ", type(data_incidentAttribuer), " personneIncAttribuer ",
                  data_incidentAttribuer["nom_incident"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "incidentAttribuer_update_1.html"
            form_update_incidentAttribuer.numero_incidentAttribuer_update.data = data_incidentAttribuer["nom_incident"]
            print(f" dta personne  ", data_incidentAttribuer["nom_incident"])
            form_update_incidentAttribuer.numero_incidentAttribuer_update.data = data_incidentAttribuer["numero_incident"]
            print(f" date de naiss personne  ", data_incidentAttribuer["numero_incident"], "  type ", type(data_incidentAttribuer["numero_incident"]))


    except Exception as Exception_incidentAttribuer_update_1:
        raise ExceptionIncidentAttribuerUpdate(f"fichier : {Path(__file__).name}  ;  "
                                     f"{incidentAttribuer_update_1.__name__} ; "
                                     f"{Exception_incidentAttribuer_update_1}")

    return render_template("incidentsAttribuer/incidentAttribuer_update_1.html", form_update_incidentAttribuer=form_update_incidentAttribuer)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "incidents_attribuer_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "personnes/incidentAttribuer_delete_1.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/incidentAttribuer_delete", methods=['GET', 'POST'])
def incidentAttribuer_delete_1():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_incidentAttribuer_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_film"
    id_incidentAttribuer_delete = request.values['id_incidentAttribuer_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_incidentAttribuer = FormDeleteIncidentAttribuer()
    try:
        # Si on clique sur "ANNULER", afficher tous les personnes.
        if form_delete_incidentAttribuer.submit_btn_annuler.data:
            return redirect(url_for("incidents_attribuer_personnes_afficher", id_incidentAttribuer_sel=0))

        if form_delete_incidentAttribuer.submit_btn_conf_del_incidentAtt.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "personnes/incidentAttribuer_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_incidentAttribuer_delete = session['data_incidentAttribuer_delete']
            print("data_incidentAttribuer_delete ", data_incidentAttribuer_delete)

            flash(f"Effacer l'incident de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_incidentAttribuer.submit_btn_del_incidentAtt.data:
            valeur_delete_dictionnaire = {"value_id_incidentAttribuer": id_incidentAttribuer_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_incident_attribuer_personne = """DELETE FROM t_pers_attribuer_inc WHERE FK_incident = %(value_id_incidentAttribuer)s"""
            str_sql_delete_incidentAttribuer = """DELETE FROM t_incident WHERE id_incident = %(value_id_incidentAttribuer)s"""
            # Manière brutale d'effacer d'abord la "fk_film", même si elle n'existe pas dans la "t_genre_film"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_incident_attribuer_personne, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_incidentAttribuer, valeur_delete_dictionnaire)

            flash(f"incident définitivement effacé !!", "success")
            print(f"incident définitivement effacé !!")

            # afficher les données
            return redirect(url_for('incidents_attribuer_personnes_afficher', id_incidentAttribuer_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_incidentAttribuer": id_incidentAttribuer_delete}
            print(id_incidentAttribuer_delete, type(id_incidentAttribuer_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_personne_attribuer_incident_delete = """SELECT * FROM t_incident WHERE id_incident = %(value_id_incidentAttribuer)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute( str_sql_personne_attribuer_incident_delete, valeur_select_dictionnaire)
                data_incidentAttribuer_delete = mydb_conn.fetchall()
                print("data_incidentAttribuer_delete...", data_incidentAttribuer_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "personnes/incidentAttribuer_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_incidentAttribuer_delete'] = data_incidentAttribuer_delete

            # Le bouton pour l'action "DELETE" dans le form. "incidentAttribuer_delete_1.html" est caché.
            btn_submit_del = False

    except Exception as Exception_incidentAttribuer_delete_1:
        raise ExceptionIncidentAttribuerDelete(f"fichier : {Path(__file__).name}  ;  "
                                     f"{incidentAttribuer_delete_1.__name__} ; "
                                     f"{Exception_incidentAttribuer_delete_1}")

    return render_template("incidentsAttribuer/incidentAttribuer_delete_1.html",
                           form_delete_incidentAttribuer=form_delete_incidentAttribuer,
                           btn_submit_del=btn_submit_del,
                           data_incidentAtt_del=data_incidentAttribuer_delete
                            )
