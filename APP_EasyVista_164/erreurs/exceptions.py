"""
    Fichier : exceptions.py
    Auteur : OM 2021.03.07
    Classes pour définir des erreurs particulières (personnalisées), qui n'existent que dans mon projet à moi.
    Quand il y a une erreur on doit définir des messages "clairs" sur un affichage à destination des "personnes".
    On ne doit pas les laisser devant des erreurs incompréhensibles.
    Dérivation des classes standard des "except" dans les blocs "try...except"
"""
import sys

from flask import flash, render_template
from pymysql import IntegrityError
from APP_EasyVista_164 import app


class Base(Exception):
    """
    Handled in Base Handler, will result of an error page display.
    Display an base error flash message
    """

    def __init__(self, message):
        self.message = message


class ErreurFichierSqlDump(Exception):
    """Erreur qui doit être affichée lorsque le fichier DUMP à un problème"""
    pass


class ErreurFichierEnvironnement(Exception):
    """Erreur qui doit être affichée lorsque le fichier des variables d'environnement pose un problème"""
    pass


class ErreurConnectionBD(Exception):
    """Erreur qui doit être affichée lorsque la connection à la bd pose un problème"""
    pass


class ErreurExtractNameBD(Exception):
    """Erreur qui doit être affichée lorsque c'est impossible d'extraire le nom de la BD depuis le fichier DUMP """
    pass


class MaBdErreurDoublon(IntegrityError):
    """Erreur qui doit être affichée lorsqu'une valeur en "double" (doublon) veut être insérée dans une table"""
    pass


class MonErreur(Exception):
    """Erreur qui doit être affichée lors d'une expérience avec du code à OM de la 707"""
    pass


class MaBdErreurConnexion(Exception):
    """Erreur qui doit être affichée lorsque la connection à la BD à des problèmes"""
    pass


class DatabaseException(Base):
    pass


class SqlException(DatabaseException):
    pass


class SqlSyntaxError(SqlException):
    pass


class DatabaseException(Base):
    pass


class ExceptionGenresAfficher(Base):
    pass


class ExceptionCategorieDelete(Base):
    pass


class ExceptionCategorieUpdate(Base):
    pass


class strsql_insert_categorie(Base):
    pass


class ExceptionPersonnesCategoriesAfficher(Base):
    pass


class ExceptionEditCategoriePersonneSelected(Base):
    pass


class ExceptionUpdateCategoriePersonneSelected(Base):
    pass


class ExceptionCategoriesPersonnesAfficherData(Base):
    pass


class ExceptionPersonneUpdate(Base):
    pass


class ExceptionPersonneDelete(Base):
    pass


class ExceptionMailsAfficher(Base):
    pass


class ExceptionMailUpdate(Base):
    pass


class ExceptionMailDelete(Base):
    pass


class ExceptionTelephoneAfficher(Base):
    pass


class ExceptionTelephoneUpdate(Base):
    pass


class ExceptionTelephoneDelete(Base):
    pass


class strsql_insert_personne(Base):
    pass


class ExceptionDemandeUpdate(Base):
    pass


class ExceptionDemandeDelete(Base):
    pass


class ExceptionDemandesAttribuerAfficher(Base):
    pass


class ExceptionEditDemandeAttribuerPersonneSelected(Base):
    pass


class ExceptionUpdateDemandeAttribuerPersonneSelected(Base):
    pass


class ExceptionDemandesAttribuerPersonnesAfficherData(Base):
    pass


class ExceptionAdresseAfficher(Base):
    pass


class strsql_insert_adresse(Base):
    pass

class ExceptionAdresseUpdate(Base):
    pass


class ExceptionAdresseDelete(Base):
    pass


class strsql_insert_personneAuteur(Base):
    pass


class ExceptionDemandeAuteurUpdate(Base):
    pass


class ExceptionDemandeAuteurDelete(Base):
    pass


class ExceptionDemandesAuteursAfficher(Base):
    pass


class ExceptionEditDemandeAuteurPersonneSelected(Base):
    pass


class ExceptionUpdateDemandeAuteurPersonneSelected(Base):
    pass


class ExceptionDemandesAuteursPersonnesAfficherData(Base):
    pass


class strsql_insert_personneIncAuteur(Base):
    pass


class ExceptionIncidentAuteurUpdate(Base):
    pass


class ExceptionIncidentAuteurDelete(Base):
    pass


class ExceptionIncidentsAuteursAfficher(Base):
    pass


class ExceptionEditIncidentAuteurPersonneSelected(Base):
    pass


class ExceptionUpdateIncidentAuteurPersonneSelected(Base):
    pass


class ExceptionIncidentsAuteursPersonnesAfficherData(Base):
    pass


class strsql_insert_personneIncAttribuer(Base):
    pass


class ExceptionIncidentAttribuerUpdate(Base):
    pass


class ExceptionIncidentAttribuerDelete(Base):
    pass


class ExceptionIncidentsAttribuerAfficher(Base):
    pass


class ExceptionEditIncidentAttribuerPersonneSelected(Base):
    pass


class ExceptionUpdateIncidentAttribuerPersonneSelected(Base):
    pass

class ExceptionIncidentsAttribuerPersonnesAfficherData(Base):
    pass


"""
    Grâce à la méthode "flash" cela permet de "raise" (remonter) les erreurs "try...execpt" dans la page "home.html"
"""


@app.errorhandler(Exception)
def om_104_exception_handler(error):
    flash(f"Erreur : {error} {error.args[0]} {sys.exc_info()[0]}", "danger")
    a, b, c = sys.exc_info()
    flash(f"Erreur générale : {a} {b} {c}", "danger")

    return render_template("home.html")


"""
    Pour définir sa propre page d'erreur 404
    Ce code est repris de la documentation FLASK
    https://flask-doc.readthedocs.io/en/latest/patterns/errorpages.html
"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
