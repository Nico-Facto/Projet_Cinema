Objectif du projet :

    Agreger des données liées aux films sortis au cinéma, afin de generer un dataframe 
    qu'on va soumettre à une IA dans le but de prédire le C.A mondiale d'un film
    ainsi que la note donnée par les spectateurs sur le site imdb.com une référence mondiale.

Exécuter docker-compose up -d depuis le dossier themoviepredicator

Se connecter à la base de donées : http://localhost:8080/
importer dans la base de donée le fichier : TheMoviesPredicator_mysql_create.sql

Pour les logs crée un fichier sec.py à la racine du projet
avec le contenu suivant :

    class secureLog():
        token="your_token"
        sqlLogMovie="your_logs"
Creer un fichier auth.env, avec vos logs mysql        

Pour ajouter un film à la BD :
    docker-compose exec app bash
    python scrap.py movies scrap yes


Pour automatiser la tâche, vous pouvez utiliser la class Pending présente dans le script class_sql.py

app.py

Executer sans commande lancera le script
avec un choix à faire au début :
0 = mode automatique avec requête comme vu en formation 
1 = mode manuel, possibilité de saisir une requête sql 
    a tapé sans ""

fonction import ouverte à toutes les tables :

    ###### Supprimer la colonne ID si présente sur le CSV à importer, dans le cas d'un auto incré,
    sinon c'est elle la premiére colonne a renseigner, je rajouterai du code qui gerera ça afin de ne 
    plus avoir à s'en occuper

    ######  cmd = app.py context import firsCol firstcase --file xxxx.csv
    ######  exemple = app.py people import firstname Alain new_people.csv
    ######  Cette fonction, est ok uniquement si on autorise les valeurs NULL depuis adminer
    ######  sur TOUTES les col sauf la premiére qu'on renseigne + la col ID si auto increment                
       
