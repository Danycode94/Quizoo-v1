""" La clase Utilisateur possedent tous les attributs pour un utilisateur. """

class Utilisateur:
    
    def __init__(self,nom:str,prenom:str,sexe:str,pseudo:str,mdp:str,etat:str):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.pseudo = pseudo
        self.mdp = mdp
        self.etat = etat
        