"""
    Fichier : gestion_personnes_categories_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les personnes et les categories.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_EasyVista_164.database.database_tools import DBconnection
from APP_EasyVista_164.erreurs.exceptions import *

"""
    Nom : films_genres_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /films_genres_afficher
    
    But : Afficher les personnes avec les categories associés pour chaque film.
    
    Paramètres : id_genre_sel = 0 >> tous les personnes.
                 id_genre_sel = "n" affiche le film dont l'id est "n"
                 
"""


@app.route("/personnes_categories_afficher/<int:id_personne_sel>", methods=['GET', 'POST'])
def personnes_categories_afficher(id_personne_sel):
    print(" personnes_categories_afficher id_personne_sel ", id_personne_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_categories_personnes_afficher_data = """SELECT id_personne, nom_personne, prenom_personne, date_naiss_personne,
                                                            FK_mail, FK_adresse, FK_telephone,
                                                            GROUP_CONCAT(nom_categorie) as PersCategorie FROM t_pers_categorie
                                                            RIGHT JOIN t_personne ON t_personne.id_personne = t_pers_categorie.FK_personne
                                                            LEFT JOIN t_categorie ON t_categorie.id_categorie = t_pers_categorie.FK_categorie
                                                            GROUP BY id_personne"""
                if id_personne_sel == 0:
                    # le paramètre 0 permet d'afficher tous les personnes
                    # Sinon le paramètre représente la valeur de l'id du film
                    mc_afficher.execute(strsql_categories_personnes_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    valeur_id_personne_selected_dictionnaire = {"value_id_personne_selected": id_personne_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_categories_personnes_afficher_data += """ HAVING id_personne= %(value_id_personne_selected)s"""

                    mc_afficher.execute(strsql_categories_personnes_afficher_data, valeur_id_personne_selected_dictionnaire)

                # Récupère les données de la requête.
                data_categories_personnes_afficher = mc_afficher.fetchall()
                print("data_categorie ", data_categories_personnes_afficher, " Type : ", type(data_categories_personnes_afficher))

                # Différencier les messages.
                if not data_categories_personnes_afficher and id_personne_sel == 0:
                    flash("""La table "t_personne" est vide. !""", "warning")
                elif not data_categories_personnes_afficher and id_personne_sel > 0:
                    # Si l'utilisateur change l'id_film dans l'URL et qu'il ne correspond à aucun film
                    flash(f"La personne {id_personne_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données personnes et categories affichées !!", "success")

        except Exception as Exception_personnes_categories_afficher:
            raise ExceptionPersonnesCategoriesAfficher(f"fichier : {Path(__file__).name}  ;  {personnes_categories_afficher.__name__} ;"
                                               f"{Exception_personnes_categories_afficher}")

    print("personnes_categories_afficher  ", data_categories_personnes_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("personnes_categories/personnes_categories_afficher.html", data=data_categories_personnes_afficher)


"""
    nom: edit_genre_film_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les categories du film sélectionné par le bouton "MODIFIER" de "personnes_categories_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les categories contenus dans la "t_genre".
    2) Les categories attribués au film selectionné.
    3) Les categories non-attribués au film sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_categorie_personne_selected", methods=['GET', 'POST'])
def edit_categorie_personne_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_categorie_afficher = """SELECT id_categorie, nom_categorie FROM t_categorie ORDER BY id_categorie ASC"""
                mc_afficher.execute(strsql_categorie_afficher)
            data_categories_all = mc_afficher.fetchall()
            print("dans edit_categorie_personne_selected ---> data_categories_all", data_categories_all)

            # Récupère la valeur de "id_film" du formulaire html "personnes_categories_afficher.html"
            # l'utilisateur clique sur le bouton "Modifier" et on récupère la valeur de "id_film"
            # grâce à la variable "id_film_genres_edit_html" dans le fichier "personnes_categories_afficher.html"
            # href="{{ url_for('edit_genre_film_selected', id_film_genres_edit_html=row.id_film) }}"
            id_personne_categorie_edit = request.values['id_personne_categorie_edit_html']

            # Mémorise l'id du film dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_personne_categorie_edit'] = id_personne_categorie_edit

            # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
            valeur_id_personne_selected_dictionnaire = {"value_id_personne_selected": id_personne_categorie_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction genres_films_afficher_data
            # 1) Sélection du film choisi
            # 2) Sélection des categories "déjà" attribués pour le film.
            # 3) Sélection des categories "pas encore" attribués pour le film choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "genres_films_afficher_data"
            data_categorie_personne_selected, data_categories_personnes_non_attribues, data_categories_personnes_attribues = \
                categories_personnes_afficher_data(valeur_id_personne_selected_dictionnaire)

            print(data_categorie_personne_selected)
            lst_data_personne_selected = [item['id_personne'] for item in data_categorie_personne_selected]
            print("lst_data_personne_selected  ", lst_data_personne_selected,
                  type(lst_data_personne_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les categories qui ne sont pas encore sélectionnés.
            lst_data_categories_personnes_non_attribues = [item['id_categorie'] for item in data_categories_personnes_non_attribues]
            session['session_lst_data_categories_personnes_non_attribues'] = lst_data_categories_personnes_non_attribues
            print("lst_data_categories_personnes_non_attribues  ", lst_data_categories_personnes_non_attribues,
                  type(lst_data_categories_personnes_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les categories qui sont déjà sélectionnés.
            lst_data_categories_personnes_old_attribues = [item['id_categorie'] for item in data_categories_personnes_attribues]
            session['session_lst_data_categories_personnes_old_attribues'] = lst_data_categories_personnes_old_attribues
            print("lst_data_categories_personnes_old_attribues  ", lst_data_categories_personnes_old_attribues,
                  type(lst_data_categories_personnes_old_attribues))

            print(" data data_categorie_personne_selected", data_categorie_personne_selected, "type ", type(data_categorie_personne_selected))
            print(" data data_categories_personnes_non_attribues ", data_categories_personnes_non_attribues, "type ",
                  type(data_categories_personnes_non_attribues))
            print(" data_categories_personnes_attribues ", data_categories_personnes_attribues, "type ",
                  type(data_categories_personnes_attribues))

            # Extrait les valeurs contenues dans la table "t_genres", colonne "intitule_genre"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_genre
            lst_data_categories_personnes_non_attribues = [item['nom_categorie'] for item in data_categories_personnes_non_attribues]
            print("lst_all_categories gf_edit_categorie_personne_selected ", lst_data_categories_personnes_non_attribues,
                  type(lst_data_categories_personnes_non_attribues))

        except Exception as Exception_edit_categorie_personne_selected:
            raise ExceptionEditCategoriePersonneSelected(f"fichier : {Path(__file__).name}  ;  "
                                                 f"{edit_categorie_personne_selected.__name__} ; "
                                                 f"{Exception_edit_categorie_personne_selected}")

    return render_template("personnes_categories/personnes_categories_modifier_tags_dropbox.html",
                           data_categorie=data_categories_all,
                           data_personne_selected=data_categorie_personne_selected,
                           data_categories_attribues=data_categories_personnes_attribues,
                           data_categories_non_attribues=data_categories_personnes_non_attribues)


"""
    nom: update_genre_film_selected

    Récupère la liste de tous les categories du film sélectionné par le bouton "MODIFIER" de "personnes_categories_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les categories contenus dans la "t_genre".
    2) Les categories attribués au film selectionné.
    3) Les categories non-attribués au film sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_categorie_personne_selected", methods=['GET', 'POST'])
def update_categorie_personne_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du film sélectionné
            id_personne_selected = session['session_id_personne_categorie_edit']
            print("session['session_id_personne_categorie_edit'] ", session['session_id_personne_categorie_edit'])

            # Récupère la liste des categories qui ne sont pas associés au film sélectionné.
            old_lst_data_categroies_personnes_non_attribues = session['session_lst_data_categories_personnes_non_attribues']
            print("old_lst_data_categroies_personnes_non_attribues ", old_lst_data_categroies_personnes_non_attribues)

            # Récupère la liste des categories qui sont associés au film sélectionné.
            old_lst_data_categories_personnes_attribues = session['session_lst_data_categories_personnes_old_attribues']
            print("old_lst_data_categories_personnes_old_attribues ", old_lst_data_categories_personnes_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme categories dans le composant "tags-selector-tagselect"
            # dans le fichier "genres_films_modifier_tags_dropbox.html"
            new_lst_str_categories_personnes = request.form.getlist('name_select_tags')
            print("new_lst_str_categories_personnes ", new_lst_str_categories_personnes)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_categorie_personne_old = list(map(int, new_lst_str_categories_personnes))
            print("new_lst_categorie_personne ", new_lst_int_categorie_personne_old, "type new_lst_categorie_personne ",
                  type(new_lst_int_categorie_personne_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_genre" qui doivent être effacés de la table intermédiaire "t_genre_film".
            lst_diff_categories_delete_b = list(set(old_lst_data_categories_personnes_attribues) -
                                            set(new_lst_int_categorie_personne_old))
            print("lst_diff_categories_delete_b ", lst_diff_categories_delete_b)

            # Une liste de "id_genre" qui doivent être ajoutés à la "t_genre_film"
            lst_diff_categories_insert_a = list(
                set(new_lst_int_categorie_personne_old) - set(old_lst_data_categories_personnes_attribues))
            print("lst_diff_categories_insert_a ", lst_diff_categories_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_film"/"id_film" et "fk_genre"/"id_genre" dans la "t_genre_film"
            strsql_insert_categorie_personne = """INSERT INTO t_pers_categorie (id_pers_categorie, FK_categorie, FK_personne)
                                                    VALUES (NULL, %(value_FK_categorie)s, %(value_FK_personne)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_film" et "id_genre" dans la "t_genre_film"
            strsql_delete_categorie_personne = """DELETE FROM t_pers_categorie WHERE FK_categorie = %(value_FK_categorie)s AND FK_personne = %(value_FK_personne)s"""

            with DBconnection() as mconn_bd:
                # Pour le film sélectionné, parcourir la liste des categories à INSÉRER dans la "t_genre_film".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_categorie_ins in lst_diff_categories_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    # et "id_genre_ins" (l'id du genre dans la liste) associé à une variable.
                    valeurs_personne_sel_categorie_sel_dictionnaire = {"value_FK_personne": id_personne_selected,
                                                               "value_FK_categorie": id_categorie_ins}

                    mconn_bd.execute(strsql_insert_categorie_personne, valeurs_personne_sel_categorie_sel_dictionnaire)

                # Pour le film sélectionné, parcourir la liste des categories à EFFACER dans la "t_genre_film".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_categorie_del in lst_diff_categories_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    # et "id_genre_del" (l'id du genre dans la liste) associé à une variable.
                    valeurs_personne_sel_categorie_sel_dictionnaire = {"value_FK_personne": id_personne_selected,
                                                               "value_FK_categorie": id_categorie_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_categorie_personne, valeurs_personne_sel_categorie_sel_dictionnaire)

        except Exception as Exception_update_categorie_personne_selected:
            raise ExceptionUpdateCategoriePersonneSelected(f"fichier : {Path(__file__).name}  ;  "
                                                   f"{update_categorie_personne_selected.__name__} ; "
                                                   f"{Exception_update_categorie_personne_selected}")

    # Après cette mise à jour de la table intermédiaire "t_genre_film",
    # on affiche les personnes et le(urs) genre(s) associé(s).
    return redirect(url_for('personnes_categories_afficher', id_personne_sel=id_personne_selected))


"""
    nom: genres_films_afficher_data

    Récupère la liste de tous les categories du film sélectionné par le bouton "MODIFIER" de "personnes_categories_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des categories, ainsi l'utilisateur voit les categories à disposition

    On signale les erreurs importantes
"""


def categories_personnes_afficher_data(valeur_id_personne_selected_dict):
    print("valeur_id_personne_selected_dict...", valeur_id_personne_selected_dict)
    try:

        strsql_personne_selected = """SELECT id_personne, nom_personne, prenom_personne, date_naiss_personne,
                                        FK_mail, FK_adresse, FK_telephone
                                        GROUP_CONCAT(id_categorie) as PersCategorie FROM t_pers_categorie
                                        INNER JOIN t_personne ON t_personne.id_personne = t_pers_categorie.FK_personne
                                        INNER JOIN t_categorie ON t_categorie.id_categorie = t_pers_categorie.FK_categorie
                                        WHERE id_personne = %(value_id_personne_selected)s"""

        strsql_categories_personnes_non_attribues = """SELECT id_categorie, nom_categorie FROM t_categorie WHERE id_categorie not in(SELECT id_categorie as idCategoriePers FROM t_pers_categorie
                                                    INNER JOIN t_personne ON t_personne.id_personne = t_pers_categorie.FK_personne
                                                    INNER JOIN t_categorie ON t_categorie.id_categorie = t_pers_categorie.FK_categorie
                                                    WHERE id_personne = %(value_id_personne_selected)s)"""

        strsql_categories_personnes_attribues = """SELECT id_personne, id_categorie, nom_categorie FROM t_pers_categorie
                                            INNER JOIN t_personne ON t_personne.id_personne = t_pers_categorie.FK_personne
                                            INNER JOIN t_categorie ON t_categorie.id_categorie = t_pers_categorie.FK_categorie
                                            WHERE id_personne = %(value_id_personne_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_categories_personnes_non_attribues, valeur_id_personne_selected_dict)
            # Récupère les données de la requête.
            data_categories_personnes_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("categories_personnes_afficher_data ----> data_categories_personnes_non_attribues ", data_categories_personnes_non_attribues,
                  " Type : ",
                  type(data_categories_personnes_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_personne_selected, valeur_id_personne_selected_dict)
            # Récupère les données de la requête.
            data_personne_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_personne_selected  ", data_personne_selected, " Type : ", type(data_personne_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_categories_personnes_attribues, valeur_id_personne_selected_dict)
            # Récupère les données de la requête.
            data_categories_personnes_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_categories_personnes_attribues ", data_categories_personnes_attribues, " Type : ",
                  type(data_categories_personnes_attribues))

            # Retourne les données des "SELECT"
            return data_personne_selected, data_categories_personnes_non_attribues, data_categories_personnes_attribues

    except Exception as Exception_categories_personnes_afficher_data:
        raise ExceptionCategoriesPersonnesAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                               f"{categories_personnes_afficher_data.__name__} ; "
                                               f"{Exception_categories_personnes_afficher_data}")
