""" La classe UtilisateurDao comportants toutes les methodes de la classe. """

import pickle
from model.utilisateur import Utilisateur

T = []
nomFichierUtilisateur = "Utilisateur.txt"

class UtilisateurDao:
    
    """ Enregistrer un compte d'utilisateur dans le fichier utilisateur."""
    def creerUnCompte(self, utilisateur: Utilisateur):
        UtilisateurDao.miseAjourFichierVersTableau(self)
        T.append(utilisateur)
        UtilisateurDao.miseAjourTableauVersFichier(self)
        if UtilisateurDao.rechercherCompteParMdp(self,utilisateur.mdp) != -1:
            return True
        return False
        
    """ Rechercher un compte d'utilisateur par mot de passe dans le fichier utilisateur."""
    def rechercherCompteParMdp(self, mdpAverifier:str):
        UtilisateurDao.miseAjourFichierVersTableau(self)
        for i in range(len(T)):
            if T[i].mdp == mdpAverifier:
                return i
        
        return -1
    
    """ Rechercher un compte d'utilisateur par pseudo dans le fichier utilisateur."""
    def rechercherCompteParPseudo(self, pseudoAverifier:str):
        UtilisateurDao.miseAjourFichierVersTableau(self)
        for i in range(len(T)):
            if T[i].pseudo.casefold() == pseudoAverifier.casefold():
                return i
        
        return -1
    
    """ Afficher toutes les comptes d'utilisateur dans le fichier utilisateur."""
    def afficherComptes(self):
        UtilisateurDao.miseAjourFichierVersTableau(self)
        for i in range(len(T)):
            print(f"Nom       :{T[i].nom}")
            print(f"Prenom    :{T[i].prenom}")
            print(f"Sexe      :{T[i].sexe}")
            print(f"Pseudo    :{T[i].pseudo}")
            print(f"----------------------------------------")
        
    """ Mise a jour des donnees d'utilisateur dans le tableau vers le fichier utilisateur."""
    def miseAjourTableauVersFichier(self):
        with open(nomFichierUtilisateur,"wb") as fichier:
            pickle.dump(T, fichier)
            
    """ Mise a jour des donnees du fichier d'utilisateur vers le tableau utilisateurs."""
    def miseAjourFichierVersTableau(self):
        T.clear()
        try:
            with open(nomFichierUtilisateur,"rb") as fichier:
                voirDonnees = pickle.load(fichier)
                
                for i in range(len(voirDonnees)):
                    T.append(voirDonnees[i])
        except EOFError:
            pass
        except FileNotFoundError:
            with open(nomFichierUtilisateur,"wb") as fichier:
                pass
        except IOError:
            print("Vous avez une erreur d'entrer et de sortie sur Le fichier !")