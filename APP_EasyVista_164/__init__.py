"""Initialisation des variables d'environnement
    Auteur : OM 2021.03.03 Indispensable pour définir les variables indispensables dans tout le projet.
"""
import sys
from flask import Flask
from environs import Env

try:
    try:
        obj_env = Env()
        obj_env.read_env()
        HOST_MYSQL = obj_env("HOST_MYSQL")
        USER_MYSQL = obj_env("USER_MYSQL")
        PASS_MYSQL = obj_env("PASS_MYSQL")
        PORT_MYSQL = int(obj_env("PORT_MYSQL"))
        NAME_BD_MYSQL = obj_env("NAME_BD_MYSQL")
        NAME_FILE_DUMP_SQL_BD = obj_env("NAME_FILE_DUMP_SQL_BD")

        ADRESSE_SRV_FLASK = obj_env("ADRESSE_SRV_FLASK")
        DEBUG_FLASK = obj_env("DEBUG_FLASK")
        PORT_FLASK = obj_env("PORT_FLASK")
        SECRET_KEY_FLASK = obj_env("SECRET_KEY_FLASK")

        app = Flask(__name__, template_folder="templates")
        print("app.url_map ____> ", app.url_map)

    except Exception as erreur:
        # print(f"45677564530 Erreur {type(erreur)} init application variables d'environnement {erreur.args}")
        print(f"45677564530 init application variables d'environnement\n"
              f"{__name__}, "
              f"{erreur.args[0]}, "
              f"{repr(erreur)}, "
              f"{type(erreur)}")
        sys.exit()

    """
        Tout commence ici. Il faut "indiquer" les routes de l'applicationn.    
        Dans l'application les lignes ci-dessous doivent se trouver ici... soit après l'instanciation de la classe "Flask"
    """
    from APP_EasyVista_164.database import database_tools
    from APP_EasyVista_164.essais_wtf_forms import gestion_essai_wtf
    from APP_EasyVista_164.essais_wtf_forms import gestion_wtf_forms_demo_select
    from APP_EasyVista_164.categories import gestion_categories_crud
    from APP_EasyVista_164.categories import gestion_categories_1_forms
    from APP_EasyVista_164.demos_om_164 import routes_demos
    from APP_EasyVista_164.mails import gestion_mails_crud
    from APP_EasyVista_164.mails import gestion_mails_1_forms

    from APP_EasyVista_164.personnes_categories import gestion_personnes_categories_crud
    from APP_EasyVista_164.erreurs import msg_avertissements

    from APP_EasyVista_164.personnes import gestion_personnes_crud
    from APP_EasyVista_164.personnes import gestion_personnes_1_forms

except Exception as e:
    print(f"Un erreur est survenue {type(e)} dans {__name__}.__init__ {e.args}")
    sys.exit()
