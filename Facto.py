import sys
import os
from pandas import read_csv
from biglearn import createNewPred as CP 
from alys import regression as AR   
# import ui
   
    

############## void start ##########################


############## void update ##########################
def voidUpdate() :

        affichage = """
    Choisissez une option:

    \t1: Creation du modèle             \t2: Entrainement Modèle

    \t3: Demander prediction             \t4: Analyse statistique 
    
    \t5: Scrap             \t6: Interagir avec la base de données

                    \t9: Terminer
                        """
        option_choisie = 0
        leave_values = 9

        while option_choisie != leave_values :
            
            print(affichage)
            option_choisie = input("Choisir option : ")
            option_choisie = int(option_choisie)
        
            if option_choisie == 1 :
                creatMod()
            elif option_choisie == 2:
                askTrain()
            elif option_choisie == 3:
                askPred()
            elif option_choisie == 4:
                askAnalyse()
            elif option_choisie == 5:
                askScrap() 
            elif option_choisie == 6:
                print("Travail en cours")                            
            elif option_choisie == leave_values :
                endsParty()  
                    
        
############### fonction ###############################

def endsParty():
    print("Main programme terminé !")
    exit()

def creatMod():
    CP.newDataSet()

def askTrain():
    CP.loaddDataSet()

def askPred():
    CP.predOnProdSet() 

def askAnalyse():
    df = input(str("Nom du fichier pred + .csv : "))
    df = read_csv(f'{df}')
    AR.regr(df)

def askScrap():
    import scrap
  
voidUpdate()    



