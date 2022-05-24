"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormAjouterCategorie
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormDeleteCategorie
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormUpdateCategorie

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5005/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/genres_afficher/<string:order_by>/<int:id_categorie_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_categorie_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_categorie_sel == 0:
                    strsql_categorie_afficher = """SELECT * FROM t_categorie ORDER BY id_categorie ASC"""
                    mc_afficher.execute(strsql_categorie_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_categorie_selected_dictionnaire = {"value_id_categorie_selected": id_categorie_sel}
                    strsql_categorie_afficher = """SELECT id_categorie, nom_categorie FROM t_categorie WHERE id_categorie 
                    = %(value_id_categorie_selected)s"""

                    mc_afficher.execute(strsql_categorie_afficher, valeur_id_categorie_selected_dictionnaire)
                else:
                    strsql_categorie_afficher = """SELECT id_categorie, nom_categorie FROM t_categorie ORDER BY 
                    id_categorie DESC"""

                    mc_afficher.execute(strsql_categorie_afficher)

                data_categorie = mc_afficher.fetchall()

                print("data_categorie ", data_categorie, " Type : ", type(data_categorie))

                # Différencier les messages si la table est vide.
                if not data_categorie and id_categorie_sel == 0:
                    flash("""La table "t_categorie" est vide. !!""", "warning")
                elif not data_categorie and id_categorie_sel > 0:
                    # Si l'utilisateur change l'id_categorie dans l'URL et que le genre n'existe pas,
                    flash(f"La categorie demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données categories affichées !!", "success")

        except Exception as Exception_categorie_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_categorie_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("genres/genres_afficher.html", data=data_categorie)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5005/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormAjouterCategorie()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_categorie_1 = form.nom_categorie_1.data
                name_categorie = name_categorie_1.lower()
                valeurs_insertion_dictionnaire = {"value_nom_categorie": name_categorie}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_categorie = """INSERT INTO t_categorie (id_categorie,nom_categorie) VALUES 
                (NULL,%(value_nom_categorie)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_categorie, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('genres_afficher', order_by='DESC', id_categorie_sel=0))

        except Exception as Exception_categorie_ajouter_wtf:
            raise strsql_insert_categorie(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_ajouter_wtf.__name__} ; "
                                          f"{Exception_categorie_ajouter_wtf}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    Exception_categorie_ajouter_wtf = request.values['id_categorie_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormUpdateCategorie()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_categorie_update = form_update.nom_categorie_update_1.data
            name_categorie_update = name_categorie_update.lower()


            valeur_update_dictionnaire = {"value_id_categorie": Exception_categorie_ajouter_wtf,
                                          "value_name_categorie": name_categorie_update,

                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_NomCategorie = """UPDATE t_categorie SET nom_categorie = %(value_name_categorie)s 
            WHERE id_categorie = %(value_id_categorie)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_NomCategorie, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('genres_afficher', order_by="ASC", id_categorie_sel=Exception_categorie_ajouter_wtf))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
            str_sql_id_categorie = "SELECT id_categorie, nom_categorie FROM t_categorie " \
                               "WHERE id_categorie = %(value_id_categorie)s"
            valeur_select_dictionnaire = {"value_id_categorie": Exception_categorie_ajouter_wtf}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_categorie, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_categorie = mybd_conn.fetchone()
            print("data_nom_categorie ", data_nom_categorie, " type ", type(data_nom_categorie), " categorie ",
                  data_nom_categorie["nom_categorie"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "genre_update_wtf.html"
            form_update.nom_categorie_update_1.data = data_nom_categorie["nom_categorie"]


    except Exception as Exception_categorie_update:
        raise ExceptionCategorieUpdate(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_update_wtf.__name__} ; "
                                      f"{Exception_categorie_update}")

    return render_template("genres/genre_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/genre_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    data_personne_attribue_categorie_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_categorie_delete = request.values['id_categorie_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormDeleteCategorie()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("genres_afficher", order_by="ASC", id_categorie_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "genres/genre_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_personne_attribue_categorie_delete = session['data_personne_attribue_categorie_delete']
                print("data_personne_attribue_categorie_delete ", data_personne_attribue_categorie_delete)

                flash(f"Effacer la categorie de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_categorie": id_categorie_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_personnes_categories = """DELETE FROM t_pers_categorie WHERE FK_categorie = %(value_id_categorie)s"""
                str_sql_delete_idcategorie = """DELETE FROM t_categorie WHERE id_categorie = %(value_id_categorie)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_genre_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_personnes_categories, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idcategorie, valeur_delete_dictionnaire)

                flash(f"categorie définitivement effacé !!", "success")
                print(f"categorie définitivement effacé !!")

                # afficher les données
                return redirect(url_for('genres_afficher', order_by="ASC", id_categorie_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_categorie": id_categorie_delete}
            print(id_categorie_delete, type(id_categorie_delete))

            # Requête qui affiche tous les films_genres qui ont le genre que l'utilisateur veut effacer
            str_sql_categories_personnes_delete = """SELECT id_pers_categorie, 	nom_personne, 	id_categorie, nom_categorie FROM t_pers_categorie
                                            INNER JOIN t_personne ON t_pers_categorie.FK_personne = t_personne.id_personne
                                            INNER JOIN t_categorie ON t_pers_categorie.FK_categorie = t_categorie.id_categorie
                                            WHERE fk_categorie = %(value_id_categorie)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_categories_personnes_delete, valeur_select_dictionnaire)
                data_personne_attribue_categorie_delete = mydb_conn.fetchall()
                print("data_personne_attribue_categorie_delete...", data_personne_attribue_categorie_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "genres/genre_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_personne_attribue_categorie_delete'] = data_personne_attribue_categorie_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
                str_sql_id_categorie = "SELECT id_categorie, nom_categorie FROM t_categorie WHERE id_categorie = %(value_id_categorie)s"

                mydb_conn.execute(str_sql_id_categorie, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_nom_categorie = mydb_conn.fetchone()
                print("data_nom_categorie ", data_nom_categorie, " type ", type(data_nom_categorie), " categorie ",
                      data_nom_categorie["id_categorie"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "genre_delete_wtf.html"
            form_delete.nom_categorie_delete_wtf.data = data_nom_categorie["id_categorie"]

            # Le bouton pour l'action "DELETE" dans le form. "genre_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_categorie_delete_1:
        raise ExceptionCategorieDelete(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_delete_wtf.__name__} ; "
                                      f"{Exception_categorie_delete_1}")

    return render_template("genres/genre_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_personnes_associes=data_personne_attribue_categorie_delete)
