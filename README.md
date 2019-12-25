Objectif du projet :

    Agreger des données liées aux films sortis au cinéma, afin de generer un dataframe 
    qu'on va soumettre à une IA dans le but de prédire la note donnée par les spectateurs
    sur le site imdb.com une référence mondiale.


Pour les logs crée un fichier sec.py à la racine du projet
avec le contenu suivant :

    class secureLog():
        token="your_token"
        sqlLogMovie="your_logs"

        # Pour BIGML
        pjt_id ="project/your_id"
        bigUseur = 'your_useur name'
        bigApiKey = 'Api key'


Se connecter à la base de donées : http://localhost:8080/
importer dans la base de donée le fichier : TheMoviesPredicator_mysql_create.sql


Exécuter docker-compose up -d depuis le dossier themoviepredicator


docker-compose exec app bash depuis le dossier themoviepredicator

python facto.py

fonction import de csv dans la base de donée ouverte à toutes les tables :

    ###### Supprimer la colonne ID si présente sur le CSV à importer, dans le cas d'un auto incré,
    sinon c'est elle la premiére colonne a renseigner######

    ######  cmd = app.py context import firsCol firstcase --file xxxx.csv
    ######  exemple = app.py people import firstname Alain new_people.csv
    ######  Cette fonction, est ok uniquement si on autorise les valeurs NULL depuis adminer
    ######  sur TOUTES les col sauf la premiére qu'on renseigne + la col ID si auto increment                
       
-----   v0.02a :

ajout d'une fonction de scrap pour le suivi de la note pour suivre la tendance
de nos predictions.

-----   v0.03a :

Creation d'un modéle sklearn, notbook = 3-sic