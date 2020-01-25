Objectif du projet :

    Agreger des données liées aux films sortis au cinéma, afin de generer un dataframe 
    qu'on va soumettre à une IA dans le but de prédire la note donnée par les spectateurs
    sur le site imdb.com une référence mondiale.


Pour les logs crée un fichier sec.py à la racine du projet
avec le contenu suivant :

    class secureLog():
        token="your_token_Api_omdb"
        sqlLogMovie="your_logs_sql"

        # Pour BIGML
        pjt_id ="project/your_id"
        bigUseur = 'your_useur name'
        bigApiKey = 'Api key'

Exécuter docker-compose build // depuis le dossier themoviepredicator
Exécuter docker-compose up -d // depuis le dossier themoviepredicator

Se connecter à la base de donées : http://localhost:8080/
importer dans la base de donée le fichier : MoviesPredictorV2.sql

python facto.py depuis le projet


Utiliser le menu scraping pour agréer des données, il faut préparer une liste d' imdb ID dans un csv pour que le script de scraping y accede.
utiliser le menu bdd pour intéragir avec elle. Vous pouvez rajouter des fonctionnalités au menus, voir le code source, il dispose de nombreuses fonctions.
Les menus 1 / 2 / 3 permette d'intéragir avec BigMl, se documenter auprés du site ci nécessaire.

-----   v0.02a :

ajout d'une fonction de scrap pour le suivi de la note pour suivre la tendance
de nos predictions.

-----   v0.03a :

Creation d'un modéle sklearn, notebook = 3-sic

-----   v0.10a :

Ajout d'un logiciel pour demander une prédiction 
Exécuter python facto.py et selectionner l'option 3 Demander une prediction

-----   v0.15a :

Ajout fontionalitée prediction multiple
Upgrade de l'interface de l'app

---------------------------------------------------------------------------------------------------------------
fonction import de csv dans la base de donée ouverte à toutes les bdd :

    ###### Supprimer la colonne ID si présente sur le CSV à importer, dans le cas d'un auto incré,
    sinon c'est elle la premiére colonne a renseigner######

    ######  cmd = app.py context import firsCol firstcase --file xxxx.csv
    ######  exemple = app.py people import firstname Alain new_people.csv
    ######  Cette fonction, est ok uniquement si on autorise les valeurs NULL depuis adminer
    ######  sur TOUTES les col sauf la premiére qu'on renseigne + la col ID si auto increment           
---------------------------------------------------------------------------------------------------------------