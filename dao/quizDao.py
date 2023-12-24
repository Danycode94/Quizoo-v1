""" La classe QuizDao comportants toutes les methodes de la classe. """

from random import choice
from pickle import load,dump
from model.quiz import Quiz

T = []
nomFichierUtilisateur = "Quiz.txt"

class QuizDao:
    
    """ Enregistrer un quiz dans le fichier Quiz."""
    def creerUnQuiz(self, quiz: Quiz):
        QuizDao.miseAjourFichierVersTableau(self)
        T.append(quiz)
        QuizDao.miseAjourTableauVersFichier(self)
    
    
    """ Rechercher toutes les sujets dans le fichier Quiz."""
    def rechercherLesSujets(self):
        QuizDao.miseAjourFichierVersTableau(self)
        setSujet = set()
        for i in range(len(T)):
           setSujet.add(T[i].sujet) 
        
        return setSujet
    
    
    """ Rechercher les quiz par sujet dans le fichier Quiz."""
    def rechercherQuizParSujet(self, sujetDuQuiz:str):
        QuizDao.miseAjourFichierVersTableau(self)
        tableauDeRetour = []
        for i in range(len(T)):
            if T[i].sujet.casefold() == sujetDuQuiz.casefold():
                quiz = Quiz(T[i].sujet,T[i].question,T[i].lesReponses,T[i].laReponse,T[i].dateHeure,T[i].mdp,T[i].nombres)
                tableauDeRetour.append(quiz)
        if len(tableauDeRetour) != 0:
            t = choice(range(len(tableauDeRetour))) 
            return tableauDeRetour[t]
        
        return -1

    
    """ Afficher toutes les quiz dans le fichier Quiz."""
    def afficherQuiz(self):
        QuizDao.miseAjourFichierVersTableau(self)
        for i in range(len(T)):
            print(f"Sujet             :{T[i].sujet}")
            print(f"Question          :{T[i].question}")
            print(f"Les reponses      :{T[i].lesReponses}")
            print(f"La reponse        :{T[i].laReponse}")
            print(f"La date           :{T[i].dateHeure}")
            print(f"Mot de passe      :{T[i].mdp}")
            print(f"Nombres          :{T[i].nombres}")
            print(f"----------------------------------------")
        
    """ Mise a jour des donnees quiz dans le tableau vers le fichier Quiz."""
    def miseAjourTableauVersFichier(self):
        with open(nomFichierUtilisateur,"wb") as fichier:
            dump(T, fichier)
            
    """ Mise a jour des donnees du fichier Quiz vers le tableau quiz."""
    def miseAjourFichierVersTableau(self):
        T.clear()
        try:
            with open(nomFichierUtilisateur,"rb") as fichier:
                voirDonnees = load(fichier)
                
                for i in range(len(voirDonnees)):
                    T.append(voirDonnees[i])
        except EOFError:
            pass
        except FileNotFoundError:
            with open(nomFichierUtilisateur,"wb") as fichier:
                pass
        except IOError:
            print("Vous avez une erreur d'entrer et de sortie sur Le fichier !")