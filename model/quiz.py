""" La clase Quiz possedent tous les attributs pour un quiz. """

class Quiz:
    
    def __init__(self,sujet:str, question:[str], lesReponses:[str], laReponse:[str], dateHeure:str, mdp:str,nombres:[int]):
        self.sujet = sujet
        self.question = question
        self.lesReponses = lesReponses
        self.laReponse = laReponse
        self.dateHeure = dateHeure
        self.mdp = mdp
        self.nombres = nombres
        