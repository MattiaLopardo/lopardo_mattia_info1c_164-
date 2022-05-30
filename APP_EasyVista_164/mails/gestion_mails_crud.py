"""Gestion des "routes" FLASK et des données pour les categories.
Fichier : gestion_categories_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_EasyVista_164 import app
from APP_EasyVista_164.database.database_tools import DBconnection
from APP_EasyVista_164.erreurs.exceptions import *
from APP_EasyVista_164.mails.gestion_mails_1_forms import FormAjouterMail
from APP_EasyVista_164.mails.gestion_mails_1_forms import FormDeleteMail
from APP_EasyVista_164.mails.gestion_mails_1_forms import FormUpdateMail

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /mails_afficher
    
    Test : ex : http://127.0.0.1:5005/mails_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les categories.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/mails_afficher/<string:order_by>/<int:id_mail_sel>", methods=['GET', 'POST'])
def mails_afficher(order_by, id_mail_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_mail_sel == 0:
                    strsql_mail_afficher = """SELECT * FROM t_mail ORDER BY id_mail ASC"""
                    mc_afficher.execute(strsql_mail_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_mail_selected_dictionnaire = {"value_id_mail_selected": id_mail_sel}
                    strsql_mail_afficher = """SELECT id_mail, nom_mail FROM t_mail WHERE id_mail 
                    = %(value_id_mail_selected)s"""

                    mc_afficher.execute(strsql_mail_afficher, valeur_id_mail_selected_dictionnaire)
                else:
                    strsql_mail_afficher = """SELECT id_mail, nom_mail FROM t_mail ORDER BY 
                    id_mail DESC"""

                    mc_afficher.execute(strsql_mail_afficher)

                data_mail = mc_afficher.fetchall()

                print("data_mail ", data_mail, " Type : ", type(data_mail))

                # Différencier les messages si la table est vide.
                if not data_mail and id_mail_sel == 0:
                    flash("""La table "t_mail" est vide. !!""", "warning")
                elif not data_mail and id_mail_sel > 0:
                    # Si l'utilisateur change l'id_mail dans l'URL et que le genre n'existe pas,
                    flash(f"Le mail demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données mails affichées !!", "success")

        except Exception as Exception_mail_afficher:
            raise ExceptionMailsAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{mails_afficher.__name__} ; "
                                          f"{Exception_mail_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("mails/mails_afficher.html", data=data_mail)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5005/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "categories/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/mails_ajouter", methods=['GET', 'POST'])
def mails_ajouter_1():
    form = FormAjouterMail()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_mail_1 = form.nom_mail_1.data
                name_mail = name_mail_1.lower()
                valeurs_insertion_dictionnaire = {"value_nom_mail": name_mail}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_mail = """INSERT INTO t_mail (id_mail,nom_mail) VALUES 
                (NULL,%(value_nom_mail)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_mail, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('mails_afficher', order_by='DESC', id_mail_sel=0))

        except Exception as Exception_mails_ajouter_1:
            raise strsql_insert_mail(f"fichier : {Path(__file__).name}  ;  "
                                          f"{mails_ajouter_1.__name__} ; "
                                          f"{Exception_mails_ajouter_1}")

    return render_template("mails/mails_ajouter_1.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "categories" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "mails_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "categories/mail_update_1.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/mail_update", methods=['GET', 'POST'])
def mail_update_1():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    Exception_mails_ajouter_1 = request.values['id_mail_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormUpdateMail()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "mail_update_1.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_mail_update = form_update.nom_mail_update_1.data
            name_mail_update = name_mail_update.lower()


            valeur_update_dictionnaire = {"value_id_mail": Exception_mails_ajouter_1,
                                          "value_name_mail": name_mail_update,

                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_NomMail = """UPDATE t_mail SET nom_mail = %(value_name_mail)s 
            WHERE id_mail = %(value_id_mail)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_NomMail, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('mails_afficher', order_by="ASC", id_mail_sel=Exception_mails_ajouter_1))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
            str_sql_id_mail = "SELECT id_mail, nom_mail FROM t_mail " \
                               "WHERE id_mail = %(value_id_mail)s"
            valeur_select_dictionnaire = {"value_id_mail": Exception_mails_ajouter_1}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_mail, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_mail = mybd_conn.fetchone()
            print("data_nom_mail ", data_nom_mail, " type ", type(data_nom_mail), " mail ",
                  data_nom_mail["nom_mail"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "mail_update_1.html"
            form_update.nom_mail_update_1.data = data_nom_mail["nom_mail"]


    except Exception as Exception_mail_update:
        raise ExceptionMailUpdate(f"fichier : {Path(__file__).name}  ;  "
                                      f"{mail_update_1.__name__} ; "
                                      f"{Exception_mail_update}")

    return render_template("mails/mail_update_1.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "categories" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "mails_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "categories/mail_delete_1.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/mail_delete", methods=['GET', 'POST'])
def mail_delete_1():
    data_personne_attribue_mail_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_mail_delete = request.values['id_mail_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormDeleteMail()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("mails_afficher", order_by="ASC", id_mail_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "categories/mail_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_personne_attribue_mail_delete = session['data_personne_attribue_mail_delete']
                print("data_personne_attribue_mail_delete ", data_personne_attribue_mail_delete)

                flash(f"Effacer le mail de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_mail": id_mail_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_personnes_mails = """DELETE FROM t_pers_avoir_mail WHERE FK_mail = %(value_id_mail)s"""
                str_sql_delete_idmail = """DELETE FROM t_mail WHERE id_mail = %(value_id_mail)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_genre_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_personnes_mails, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idmail, valeur_delete_dictionnaire)

                flash(f"mail définitivement effacé !!", "success")
                print(f"mail définitivement effacé !!")

                # afficher les données
                return redirect(url_for('mails_afficher', order_by="ASC", id_mail_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_mail": id_mail_delete}
            print(id_mail_delete, type(id_mail_delete))

            # Requête qui affiche tous les personnes_categories qui ont le genre que l'utilisateur veut effacer
            str_sql_mails_personnes_delete = """SELECT t_pers_avoir_mail, 	nom_personne, 	id_mail, nom_mail FROM t_pers_categorie
                                            INNER JOIN t_personne ON t_pers_categorie.FK_personne = t_personne.id_personne
                                            INNER JOIN t_mail ON t_pers_avoir_mail.FK_mail = t_mail.id_mail
                                            WHERE FK_mail = %(value_id_mail)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_mails_personnes_delete, valeur_select_dictionnaire)
                data_personne_attribue_mail_delete = mydb_conn.fetchall()
                print("data_personne_attribue_mail_delete...", data_personne_attribue_mail_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "categories/mail_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_personne_attribue_mail_delete'] = data_personne_attribue_mail_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
                str_sql_id_mail = "SELECT id_mail, nom_mail FROM t_mail WHERE id_mail = %(value_id_mail)s"

                mydb_conn.execute(str_sql_id_mail, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_nom_mail = mydb_conn.fetchone()
                print("data_nom_mail ", data_nom_mail, " type ", type(data_nom_mail), " mail ",
                      data_nom_mail["id_mail"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "mail_delete_1.html"
            form_delete.nom_mail_delete_1.data = data_nom_mail["id_mail"]

            # Le bouton pour l'action "DELETE" dans le form. "mail_delete_1.html" est caché.
            btn_submit_del = False

    except Exception as Exception_mail_delete_1:
        raise ExceptionMailDelete(f"fichier : {Path(__file__).name}  ;  "
                                      f"{mail_delete_1.__name__} ; "
                                      f"{Exception_mail_delete_1}")

    return render_template("mails/mail_delete_1.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_personnes_associes=data_personne_attribue_mail_delete)


