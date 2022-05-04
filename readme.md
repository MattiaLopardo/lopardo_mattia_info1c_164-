Module 164 Exercice du 2022.04.13
---


# Faire fonctionner cette démo :
##### BUT : CRUD (Create Read Update Delete) complet sur les 3 tables de la base film : Soit "t_film"; "t_genre" et la table intermédiaire "t_genre_film"
* Démarrer le serveur MySql (uwamp ou xamp ou mamp, etc)
* Dans PyCharm, importer la BD à partir du fichier DUMP
  * Ouvrir le fichier "database/1_ImportationDumpSql.py"
  * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10)
  * En cas d'erreurs : ouvrir le fichier ".env" à la racine du projet, contrôler les indications de connexion pour la bd.
* Test simple de la connexion à la BD 
  * Ouvrir le fichier "database/2_test_connection_bd.py"
  * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10)
* Démarrer le microframework FLASK
  * Dans le répertoire racine du projet, ouvrir le fichier "run_mon_app.py"
  * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10)

