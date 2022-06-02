"""Gestion des "routes" FLASK et des données pour les adresses.
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
from APP_EasyVista_164.adresses.gestion_adresses_1_forms import FormAjouterAdresse
from APP_EasyVista_164.adresses.gestion_adresses_1_forms import FormDeleteAdresse
from APP_EasyVista_164.adresses.gestion_adresses_1_forms import FormUpdateAdresse

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /adresses_afficher
    
    Test : ex : http://127.0.0.1:5005/adresses_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les adresses.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/adresses_afficher/<string:order_by>/<int:id_adresse_sel>", methods=['GET', 'POST'])
def adresses_afficher(order_by, id_adresse_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_adresse_sel == 0:
                    strsql_adresse_afficher = """SELECT id_adresse, nom_adresse, NPA_adresse, ville_adresse FROM t_adresse ORDER BY id_adresse ASC"""
                    mc_afficher.execute(strsql_adresse_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_adresse_selected_dictionnaire = {"value_id_adresse_selected": id_adresse_sel}
                    strsql_adresse_afficher = """SELECT id_adresse, nom_adresse, NPA_adresse, ville_adresse FROM t_adresse WHERE id_adresse 
                    = %(value_id_adresse_selected)s"""

                    mc_afficher.execute(strsql_adresse_afficher, valeur_id_adresse_selected_dictionnaire)
                else:
                    strsql_adresse_afficher = """SELECT id_adresse, nom_adresse, NPA_adresse, ville_adresse FROM t_adresse ORDER BY 
                    id_adresse DESC"""

                    mc_afficher.execute(strsql_adresse_afficher)

                data_adresse = mc_afficher.fetchall()

                print("data_adresse ", data_adresse, " Type : ", type(data_adresse))

                # Différencier les messages si la table est vide.
                if not data_adresse and id_adresse_sel == 0:
                    flash("""La table "t_adresse" est vide. !!""", "warning")
                elif not data_adresse and id_adresse_sel > 0:
                    # Si l'utilisateur change l'id_adresse dans l'URL et que le genre n'existe pas,
                    flash(f"L'adresse demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données adresses affichées !!", "success")

        except Exception as Exception_adresse_afficher:
            raise ExceptionAdresseAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{adresses_afficher.__name__} ; "
                                          f"{Exception_adresse_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("adresses/adresses_afficher.html", data=data_adresse)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5005/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "adresses/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/adresses_ajouter", methods=['GET', 'POST'])
def adresses_ajouter_1():
    form = FormAjouterAdresse()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_adresse_1 = form.nom_adresse_1.data
                name_adresse = name_adresse_1.lower()
                valeurs_insertion_dictionnaire = {"value_nom_adresse": name_adresse}

                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_adresse = """INSERT INTO t_adresse (id_adresse, nom_adresse, NPA_adresse, ville_adresse) VALUES 
                (NULL,%(value_nom_adresse)s,%(value_NPA_adresse)s,%(value_ville_adresse)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_adresse, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('adresses_afficher', order_by='DESC', id_adresse_sel=0))

        except Exception as Exception_adresse_ajouter_1:
            raise strsql_insert_adresse(f"fichier : {Path(__file__).name}  ;  "
                                          f"{adresses_ajouter_1.__name__} ; "
                                          f"{Exception_adresse_ajouter_1}")

    return render_template("adresses/adresses_ajouter_1.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "adresses" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "adresses_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "adresses/adresse_update_1.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/adresse_update", methods=['GET', 'POST'])
def adresse_update_1():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    Exception_adresse_ajouter_1 = request.values['id_adresse_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormUpdateAdresse()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "adresse_update_1.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            nom_adresse_update = form_update.nom_adresse_update_1.data
            nom_adresse_update = nom_adresse_update.lower()
            NPA_adresse_1 = form_update.NPA_adresse_1.data
            ville_adresse_1 = form_update.ville_adresse_1.data

            valeur_update_dictionnaire = {"value_id_adresse": Exception_adresse_ajouter_1,
                                          "value_nom_adresse": nom_adresse_update,
                                          "value_NPA_adresse": NPA_adresse_1,
                                          "value_ville_adresse": ville_adresse_1
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_NomAdresse = """UPDATE t_adresse SET nom_adresse = %(value_nom_adresse)s, 
            NPA_adresse = %(value_NPA_adresse)s WHERE id_adresse = %(value_id_adresse)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_NomAdresse, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('adresses_afficher', order_by="ASC", id_adresse_sel=Exception_adresse_ajouter_1))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
            str_sql_id_adresse = "SELECT id_adresse, nom_adresse, NPA_adresse, ville_adresse FROM t_adresse " \
                               "WHERE id_adresse = %(value_id_adresse)s"
            valeur_select_dictionnaire = {"value_id_adresse": Exception_adresse_ajouter_1}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_adresse, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_adresse = mybd_conn.fetchone()
            print("data_nom_adresse ", data_nom_adresse, " type ", type(data_nom_adresse), " adresse ",
                  data_nom_adresse["nom_adresse"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "adresse_update_1.html"
            form_update.nom_adresse_update_1.data = data_nom_adresse["nom_adresse"]
            form_update.NPA_adresse_1.data = data_nom_adresse["NPA_adresse"]
            form_update.ville_adresse_1.data = data_nom_adresse["ville_adresse"]

    except Exception as Exception_adresse_update:
        raise ExceptionAdresseUpdate(f"fichier : {Path(__file__).name}  ;  "
                                      f"{adresse_update_1.__name__} ; "
                                      f"{Exception_adresse_update}")

    return render_template("adresses/adresse_update_1.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "adresses" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "adresses_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "adresses/adresse_delete_1.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/adresse_delete", methods=['GET', 'POST'])
def adresse_delete_1():
    data_personne_attribue_adresse_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_adresse_delete = request.values['id_adresse_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormDeleteAdresse()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("adresses_afficher", order_by="ASC", id_adresse_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "adresses/adresse_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_personne_attribue_adresse_delete = session['data_personne_attribue_adresse_delete']
                print("data_personne_attribue_adresse_delete ", data_personne_attribue_adresse_delete)

                flash(f"Effacer l'  adresse de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_adresse": id_adresse_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_personnes_adresses = """DELETE FROM t_personne WHERE FK_adresse = %(value_id_adresse)s"""
                str_sql_delete_idadresse = """DELETE FROM t_adresse WHERE id_adresse = %(value_id_adresse)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_genre_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_personnes_adresses, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idadresse, valeur_delete_dictionnaire)

                flash(f"  adresse définitivement effacé !!", "success")
                print(f"  adresse définitivement effacé !!")

                # afficher les données
                return redirect(url_for('adresses_afficher', order_by="ASC", id_adresse_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_adresse": id_adresse_delete}
            print(id_adresse_delete, type(id_adresse_delete))

            # Requête qui affiche tous les personnes_categories qui ont le genre que l'utilisateur veut effacer
            str_sql_adresses_personnes_delete = """SELECT id_personne, 	nom_personne, 	id_adresse, nom_adresse FROM t_personne
                                            INNER JOIN t_adresse ON t_personne.FK_adresse = t_adresse.id_adresse
                                            WHERE FK_adresse = %(value_id_adresse)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_adresses_personnes_delete, valeur_select_dictionnaire)
                data_personne_attribue_adresse_delete = mydb_conn.fetchall()
                print("data_personne_attribue_adresse_delete...", data_personne_attribue_adresse_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "adresses/adresse_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_personne_attribue_adresse_delete'] = data_personne_attribue_adresse_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
                str_sql_id_adresse = "SELECT id_adresse, nom_adresse FROM t_adresse WHERE id_adresse = %(value_id_adresse)s"

                mydb_conn.execute(str_sql_id_adresse, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_nom_adresse = mydb_conn.fetchone()
                print("data_nom_adresse ", data_nom_adresse, " type ", type(data_nom_adresse), " adresse ",
                      data_nom_adresse["nom_adresse"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "adresse_delete_1.html"
            form_delete.nom_adresse_delete_1.data = data_nom_adresse["nom_adresse"]

            # Le bouton pour l'action "DELETE" dans le form. "adresse_delete_1.html" est caché.
            btn_submit_del = False

    except Exception as Exception_adresse_delete_1:
        raise ExceptionAdresseDelete(f"fichier : {Path(__file__).name}  ;  "
                                      f"{adresse_delete_1.__name__} ; "
                                      f"{Exception_adresse_delete_1}")

    return render_template("adresses/adresse_delete_1.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_personnes_associes=data_personne_attribue_adresse_delete)
