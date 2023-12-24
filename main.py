""" La classe MainActivity regroupent l'ensembles des classes, methodes du programme. """

import os

from datetime import datetime
from app.messages import Messages
from model.utilisateur import Utilisateur
from dao.utilisateurDao import UtilisateurDao
from model.quiz import Quiz
from dao.quizDao import QuizDao

tableauQuiz = []

class MainActivity:

    def menu_principal(self):
        os.system("cls")
        test_menu = True
        
        while test_menu:
            Messages.txt_entete(self)
            Messages.txt_menu_principal(self)
            
            choix = input("\nPresser le chiffre qui correspond a votre choix :").strip()
            while choix != "0" and choix != "1" and choix != "2":
                choix = input("Presser le chiffre qui correspond a votre choix :").strip()
            
            choix = int(choix)
            match(choix):
                case 0:
                    os.system("cls")
                    print("\nMerci d'avoir utiliser le programme Quizoo.\n")
                    exit(1)
                case 1:
                    os.system("cls")
                    MainActivity.enregistrer_quiz(self)
                case 2:
                    os.system("cls")
                    MainActivity.jouer_un_quiz(self)
    
    def enregistrer_quiz(self):
        os.system("cls")
        test_menu = True
        
        while test_menu:
            Messages.txt_entete(self)
            Messages.txt_enregistrer_quiz(self)
            
            choix = input("\nPresser le chiffre qui correspond a votre choix :").strip()
            while choix != "0" and choix != "1" and choix != "2":
                choix = input("Presser le chiffre qui correspond a votre choix :").strip()
            
            choix = int(choix)
            match(choix):
                case 0:
                    test_menu = False
                case 1:
                    os.system("cls")
                    Messages.txt_creerCompte(self)
                    
                    nom = input("\nEntrer votre nom :").strip()
                    while not nom or len(nom) < 3:
                        nom = input("Entrer un nom valide et contient au minimum 3 caracteres :").strip()
                    
                    prenom = input("\nEntrer votre prenom :").strip()
                    while not prenom or len(prenom) < 3:
                        prenom = input("Entrer un prenom valide et contient au minimum 3 caracteres :").strip()
                    
                    print(f"\n1.-Masculin \t 2.-Feminin")
                    sexe = input("faite votre choix du sexe :").strip()
                    while not sexe or sexe != "1" and sexe != "2":
                        sexe = input("faite votre choix du sexe :").strip()
                    if sexe == "1":
                        sexe = "Masculin"
                    else:
                        sexe = "Feminin"
                        
                    pseudo = input("\nEntrer votre pseudo :").strip()
                    while not pseudo or len(pseudo) < 3 or UtilisateurDao.rechercherCompteParPseudo(self, pseudo) != -1:
                        if UtilisateurDao.rechercherCompteParPseudo(self, pseudo) == -1:
                            pseudo = input("Entrer un pseudo valide et contient au minimum 3 caracteres :").strip()
                        else:
                            pseudo = input("Cette pseudo exite deja dans notre liste d'utilisateur :").strip()
                    
                    mdp = input("\nEntrer votre mot de passe :").strip()
                    while not mdp or len(mdp) < 4 or UtilisateurDao.rechercherCompteParMdp(self, mdp) != -1:
                        if UtilisateurDao.rechercherCompteParPseudo(self, mdp) == -1:
                            mdp = input("Entrer un mot de passe valide et contient au minimum 4 caracteres :").strip()
                        else:
                            mdp = input("Cette mot de passe exite deja dans notre liste d'utilisateur :").strip()
                    
                    compte = Utilisateur(nom.upper(),prenom.title(),sexe,pseudo,mdp,"Donner quiz")
                    if UtilisateurDao.creerUnCompte(self, compte):
                        print("Votre compte a ete creer avec succes !")
                    else:
                        print("La creation de votre compte a echouer !")
                    
                    input("\nPresser la toucher enter pour continuer...")
                case 2:
                    os.system("cls")
                    Messages.txt_creerQuiz(self)
                    
                    pseudo = input("\nVeuillez entrer votre pseudo :")
                    if UtilisateurDao.rechercherCompteParPseudo(self, pseudo) != -1:
                        mdp = input("\nVeuillez entrer votre mot de passe :")
                        if UtilisateurDao.rechercherCompteParMdp(self, mdp) != -1:
                            os.system("cls")
                            print("\nVous avez bien ete connecter !")
                            
                            sujet = input("\nEntrer le sujet de votre quiz - (ex: Geograpie,fisik) :")
                            while not sujet or len(sujet) < 3:
                                sujet = input("Entrer sujet de quiz valide et contient au minimum 3 caracteres :").strip()
                            
                            i = 1
                            testQuestionReponse = True
                            lesQuestions = []
                            lesChoixDesReponses = []
                            lesReponses = []
                            relaisLesRep = []
                            LesNonbres = []
                            
                            while testQuestionReponse:
                                nbrRep = True
                                os.system("cls")
                                print("\nTaper 'ok' lorsque vous avez fini de mettre toutes vos questions")
                                question = input(f"Entrer la question #{i} de votre quiz :")
                                while not question or len(question) < 2:
                                    question = input("Entrer un question de quiz valide et contient au minimum 3 caracteres :").strip()
                                if question == "ok" or question == "OK" or question == "Ok" or question == "oK":
                                    testQuestionReponse = False
                                else:
                                    lesQuestions.append(question)
                                
                                if testQuestionReponse:
                                    os.system("cls")
                                    i1 = 1
                                    print("\nTaper 'ok' lorsque vous avez fini de mettre les responses")
                                    print(f"\nPour la question | {question} | entrer les choix de reponse")
                                    while nbrRep:
                                        reponseDonner = input(f"Entrer le/la {i1} choix de reponse pour la question :").strip()
                                        while not reponseDonner:
                                            reponseDonner = input(f"Entrer le/la {i1} choix de reponse pour la question valide :").strip()
                                        if reponseDonner == "ok" or reponseDonner == "OK" or reponseDonner == "Ok" or reponseDonner == "oK":
                                            LesNonbres.append((i1 - 1))
                                            nbrRep = False
                                        else:
                                            lesChoixDesReponses.append(reponseDonner)
                                            relaisLesRep.append(reponseDonner)
                                        i1 += 1
                                    i += 1
                                    
                                    os.system("cls")
                                    reponsAlaQuestion = input(f"\nPour la question | {question}|\nVoici ce que vous avez remplit{relaisLesRep}\nEntrer la bonne reponse  :").strip()
                                    while reponsAlaQuestion not in relaisLesRep:
                                        os.system("cls")
                                        reponsAlaQuestion = input(f"\nPour la question | {question}|\nVoici ce que vous avez remplit{relaisLesRep}  :").strip()
                                    lesReponses.append(reponsAlaQuestion)
                                    relaisLesRep.clear()
                                else:
                                    os.system("cls")
                                    if len(lesQuestions) == 0 and len(lesReponses) == 0:
                                        print("Vous n'avez creer aucun quiz")
                                    else:
                                        quiz = Quiz(sujet,lesQuestions,lesChoixDesReponses,lesReponses,str(datetime.now()),mdp,LesNonbres)
                                        QuizDao.creerUnQuiz(self, quiz)
                                        print("Vous avez terminer le remplissage de quiz")
                        else:
                            print("\nCette mot de passe n'existe pas ou elle est incorrect")
                    else:
                        print("\nCette pseudo n'existe pas ou elle est incorrect")
                    input("\nPresser la toucher enter pour continuer...")
                
    def jouer_un_quiz(self):
        os.system("cls")
        test_menu = True
        test = []
        
        while test_menu:
            Messages.txt_entete(self)
            Messages.txt_jouer_quiz(self)
            
            choix = input("\nPresser le chiffre qui correspond a votre choix :").strip()
            while choix != "0" and choix != "1":
                choix = input("Presser le chiffre qui correspond a votre choix :").strip()
            
            choix = int(choix)
            match(choix):
                case 0:
                    test_menu = False
                case 1:
                    os.system("cls")
                    Messages.txt_sujetsQuiz(self)
                    sujets = QuizDao.rechercherLesSujets(self)
                    if len(sujets) == 0:
                        print("\nAuncun quiz n'est disponible pour l'intant...")
                    else:
                        for i, sujet in enumerate(sujets):
                            print(f"{i+1}.-{sujet}")
                            test.append(f"{i+1}")
                            
                        print("Un quiz va etre choisie de facon aleatoire selon le choix de votre sujet.")
                
                        choix1 = input("\nPresser le chiffre qui correspond a votre sujet :").strip()
                        while choix1 not in test:
                            choix1 = input("Presser le chiffre qui correspond a votre choix :").strip()
                        
                        choix1 = int(choix1)
                        for i, sujet in enumerate(sujets):
                            if i+1 == choix1:
                                t = QuizDao.rechercherQuizParSujet(self, sujet)
                                choixQuiz = [t]

                        pp = []
                        tp = 0
                        if choixQuiz != -1:  
                            os.system("cls")
                            nbresDeQuestion = 0
                            nbresReponseParQuestion = 0
                            
                            for i in range(len(choixQuiz)):
                                nbresDeQuestion = len(choixQuiz[i].question)
                            print(f"\nCette quiz comptes {nbresDeQuestion} questions\n")
                            
                            connaitreChoixReponse = [] 
                            reponseDonner = ""
                            reponseVerifier = ""
                            scoreTotal = 0
                            for i in range(nbresDeQuestion):
                                os.system("cls")
                                for k in range(len(choixQuiz)):
                                    question = choixQuiz[k].question[i]
                                    print(f"La question #{(i + 1)}     :{question}")
                                    nbresReponseParQuestion = 0
                                    nbresReponseParQuestion = choixQuiz[k].nombres[i]
                                    tp += nbresReponseParQuestion
                                    for i1 in range(nbresReponseParQuestion if (i < 1) else tp):
                                        if i >= 1:
                                            if choixQuiz[k].lesReponses[i1] not in pp:
                                                pp.append(choixQuiz[k].lesReponses[i1])
                                                connaitreChoixReponse.append(choixQuiz[k].lesReponses[i1])
                                                print(f"Reponse #{(len(connaitreChoixReponse))} :{(choixQuiz[k].lesReponses[i1])}")
                                        else:
                                            pp.append(choixQuiz[k].lesReponses[i1])
                                            connaitreChoixReponse.append(choixQuiz[k].lesReponses[i1])
                                            print(f"Reponse #{(i1 + 1)} :{(choixQuiz[k].lesReponses[i1])}")
                                            
                                    rep = input("\nPresser le chiffre qui correspond a votre reponse :").strip()
                                    repCorrect = []
                                    for e in range(1, nbresReponseParQuestion+1):
                                        repCorrect.append(f"{e}")
                                    while rep not in repCorrect:
                                        rep = input("Presser le chiffre qui correspond a votre reponse :").strip()                               
                                    
                                    
                                    for e, val in enumerate(connaitreChoixReponse):
                                        if (e) == int(rep)-1:
                                            reponseDonner = val
                                    reponseVerifier = str(choixQuiz[k].laReponse[i])
                                    
                                    if reponseDonner.casefold() == reponseVerifier.casefold():
                                        os.system("cls")
                                        pointParQuestion = (100 / nbresDeQuestion)
                                        scoreTotal += 1
                                        print(f"\nVous avez trouver la reponse...")
                                    else:
                                        os.system("cls")
                                        print(f"\nLa reponse n'est pas correct...")
                                    
                                    connaitreChoixReponse.clear()
                                    input("\nPresser la toucher enter pour continuer...")
                                    
                            print(f"\nVotre score total de reponse est :{scoreTotal} / {nbresDeQuestion} questions...")
                    input("\nPresser la toucher enter pour continuer...")
    
        
MainActivity().menu_principal()
