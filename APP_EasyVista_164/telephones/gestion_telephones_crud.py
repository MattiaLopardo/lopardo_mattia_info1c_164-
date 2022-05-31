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
from APP_EasyVista_164.telephones.gestion_telephones_1_forms import FormAjouterTelephone
from APP_EasyVista_164.telephones.gestion_telephones_1_forms import FormDeleteTelephone
from APP_EasyVista_164.telephones.gestion_telephones_1_forms import FormUpdateTelephone

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /telephones_afficher
    
    Test : ex : http://127.0.0.1:5005/telephones_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les categories.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/telephones_afficher/<string:order_by>/<int:id_telephone_sel>", methods=['GET', 'POST'])
def telephones_afficher(order_by, id_telephone_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_telephone_sel == 0:
                    strsql_telephone_afficher = """SELECT * FROM t_telephone ORDER BY id_telephone ASC"""
                    mc_afficher.execute(strsql_telephone_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_telephone_selected_dictionnaire = {"value_id_telephone_selected": id_telephone_sel}
                    strsql_telephone_afficher = """SELECT id_telephone, num_telephone FROM t_telephone WHERE id_telephone 
                    = %(value_id_telephone_selected)s"""

                    mc_afficher.execute(strsql_telephone_afficher, valeur_id_telephone_selected_dictionnaire)
                else:
                    strsql_telephone_afficher = """SELECT id_telephone, num_telephone FROM t_telephone ORDER BY 
                    id_telephone DESC"""

                    mc_afficher.execute(strsql_telephone_afficher)

                data_telephone = mc_afficher.fetchall()

                print("data_telephone ", data_telephone, " Type : ", type(data_telephone))

                # Différencier les messages si la table est vide.
                if not data_telephone and id_telephone_sel == 0:
                    flash("""La table "t_telephone" est vide. !!""", "warning")
                elif not data_telephone and id_telephone_sel > 0:
                    # Si l'utilisateur change l'id_telephone dans l'URL et que le genre n'existe pas,
                    flash(f"Le telephone demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données telephones affichées !!", "success")

        except Exception as Exception_telephone_afficher:
            raise ExceptionTelephoneAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{telephones_afficher.__name__} ; "
                                          f"{Exception_telephone_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("telephones/telephones_afficher.html", data=data_telephone)


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


@app.route("/telephones_ajouter", methods=['GET', 'POST'])
def telephones_ajouter_1():
    form = FormAjouterTelephone()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                num_telephone_1 = form.number_telephone_1.data
                num_telephone = num_telephone_1.lower()
                valeurs_insertion_dictionnaire = {"value_num_telephone": num_telephone}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_telephone = """INSERT INTO t_telephone (id_telephone,num_telephone) VALUES 
                (NULL,%(value_num_telephone)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_telephone, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('telephones_afficher', order_by='DESC', id_telephone_sel=0))

        except Exception as Exception_telephones_ajouter_1:
            raise strsql_insert_telephone(f"fichier : {Path(__file__).name}  ;  "
                                          f"{telephones_ajouter_1.__name__} ; "
                                          f"{Exception_telephones_ajouter_1}")

    return render_template("telephones/telephones_ajouter_1.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "categories" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "telephones_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "categories/telephone_update_1.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/telephone_update", methods=['GET', 'POST'])
def telephone_update_1():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    Exception_telephones_ajouter_1 = request.values['id_telephone_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormUpdateTelephone()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "telephone_update_1.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            number_telephone_update = form_update.num_telephone_update_1.data
            number_telephone_update = number_telephone_update.lower()


            valeur_update_dictionnaire = {"value_id_telephone": Exception_telephones_ajouter_1,
                                          "value_num_telephone": number_telephone_update,

                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_NomTelephone = """UPDATE t_telephone SET num_telephone = %(value_num_telephone)s 
            WHERE id_telephone = %(value_id_telephone)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_NomTelephone, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('telephones_afficher', order_by="ASC", id_telephone_sel=Exception_telephones_ajouter_1))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
            str_sql_id_telephone = "SELECT id_telephone, num_telephone FROM t_telephone " \
                               "WHERE id_telephone = %(value_id_telephone)s"
            valeur_select_dictionnaire = {"value_id_telephone": Exception_telephones_ajouter_1}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_telephone, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_num_telephone = mybd_conn.fetchone()
            print("data_num_telephone ", data_num_telephone, " type ", type(data_num_telephone), " telephone ",
                  data_num_telephone["num_telephone"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "telephone_update_1.html"
            form_update.num_telephone_update_1.data = data_num_telephone["num_telephone"]


    except Exception as Exception_telephone_update:
        raise ExceptionTelephoneUpdate(f"fichier : {Path(__file__).name}  ;  "
                                      f"{telephone_update_1.__name__} ; "
                                      f"{Exception_telephone_update}")

    return render_template("telephones/telephone_update_1.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "categories" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "telephones_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "categories/telephone_delete_1.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/telephone_delete", methods=['GET', 'POST'])
def telephone_delete_1():
    data_personne_attribue_telephone_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_telephone_delete = request.values['id_telephone_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormDeleteTelephone()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("telephones_afficher", order_by="ASC", id_telephone_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "categories/telephone_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_personne_attribue_telephone_delete = session['data_personne_attribue_telephone_delete']
                print("data_personne_attribue_telephone_delete ", data_personne_attribue_telephone_delete)

                flash(f"Effacer le telephone de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_telephone": id_telephone_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_personnes_telephones = """DELETE FROM t_personne WHERE FK_telephone = %(value_id_telephone)s"""
                str_sql_delete_idtelephone = """DELETE FROM t_telephone WHERE id_telephone = %(value_id_telephone)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_genre_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_personnes_telephones, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idtelephone, valeur_delete_dictionnaire)

                flash(f"telephone définitivement effacé !!", "success")
                print(f"telephone définitivement effacé !!")

                # afficher les données
                return redirect(url_for('telephones_afficher', order_by="ASC", id_telephone_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_telephone": id_telephone_delete}
            print(id_telephone_delete, type(id_telephone_delete))

            # Requête qui affiche tous les personnes_categories qui ont le genre que l'utilisateur veut effacer
            str_sql_telephones_personnes_delete = """SELECT id_personne, nom_personne, id_telephone, num_telephone FROM t_personne
                                            INNER JOIN t_telephone ON t_personne.FK_telephone = t_telephone.id_telephone
                                            WHERE FK_telephone = %(value_id_telephone)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_telephones_personnes_delete, valeur_select_dictionnaire)
                data_personne_attribue_telephone_delete = mydb_conn.fetchall()
                print("data_personne_attribue_telephone_delete...", data_personne_attribue_telephone_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "categories/telephone_delete_1.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_personne_attribue_telephone_delete'] = data_personne_attribue_telephone_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
                str_sql_id_telephone = "SELECT id_telephone, num_telephone FROM t_telephone WHERE id_telephone = %(value_id_telephone)s"

                mydb_conn.execute(str_sql_id_telephone, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_num_telephone = mydb_conn.fetchone()
                print("data_num_telephone ", data_num_telephone, " type ", type(data_num_telephone), " telephone ",
                      data_num_telephone["id_telephone"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "telephone_delete_1.html"
            form_delete.num_telephone_delete_1.data = data_num_telephone["id_telephone"]

            # Le bouton pour l'action "DELETE" dans le form. "telephone_delete_1.html" est caché.
            btn_submit_del = False

    except Exception as Exception_telephone_delete_1:
        raise ExceptionTelephoneDelete(f"fichier : {Path(__file__).name}  ;  "
                                      f"{telephone_delete_1.__name__} ; "
                                      f"{Exception_telephone_delete_1}")

    return render_template("telephones/telephone_delete_1.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_personnes_associes=data_personne_attribue_telephone_delete)


