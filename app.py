''' The Movies Predictor Script Sql- Nicolas Autexier '''

import mysql.connector
import sys
import argparse
import csv
from sec import secureLog as SL


modechoice = input("1 pour une execution manuelle, 0 pour une excecution automatique cmd :")
modechoice = int(modechoice)
print(f"Mode selec : {modechoice}")

if modechoice == 0 :
    parser = argparse.ArgumentParser(description="Process movie predictor data")

    parser.add_argument('context', choices=['people','movies','compagnies','movies_companies_roles','movies_origins_country','movies_people_roles','roles'], help='context dans lequel nous allons travailler')
    
    subparsers = parser.add_subparsers(dest='Action',required=True)
    
    parser_list = subparsers.add_parser("list")
    parser_list.add_argument('--export')

    parser_fetch = subparsers.add_parser("fetch")
    parser_fetch.add_argument('id', metavar='id', type=int)
    parser_fetch.add_argument('--export')

    parser_count = subparsers.add_parser("count")
    parser_count.add_argument('var')
    parser_count.add_argument('whereToCount')
    parser_count.add_argument('--export')

    parser_insert = subparsers.add_parser("insert")
    parser_insert.add_argument('col')
    parser_insert.add_argument('vals')
    parser_insert.add_argument('--export')

    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument('condition')
    parser_delete.add_argument('--export')

    parser_ADD_COL = subparsers.add_parser("ADD_COL")
    parser_ADD_COL.add_argument('columnName')
    parser_ADD_COL.add_argument('colType')
    parser_ADD_COL.add_argument('--export')

    parser_DROP_COL = subparsers.add_parser("DROP_COL")
    parser_DROP_COL.add_argument('columnName')
    parser_DROP_COL.add_argument('--export')

    parser_Update = subparsers.add_parser("update")
    parser_Update.add_argument('setVals')
    parser_Update.add_argument('where')
    parser_Update.add_argument('--export')

    parser_import = subparsers.add_parser("import")
    parser_import.add_argument('firstcol', help='le nom de la premiére colone de la table' )
    parser_import.add_argument('firstcase', help='le type de données')
    parser_import.add_argument('--file')
    parser_import.add_argument('--export')

    parser_import = subparsers.add_parser("import_col")
    parser_import.add_argument('typeK', help='le type de données')
    parser_import.add_argument('--file')
    parser_import.add_argument('--export')

    try :
        args = parser.parse_args() 
        print(args)
        if args.export == None :
            extractMode = False
        else :
            extractMode = True  
    except :
        print("erreur dans la selection d'arguments, mode libre activé !")
        modechoice = 1
        # args = None
        extractMode = False  
      
elif modechoice >=1:
    parser2 = argparse.ArgumentParser(description="Process movie predictor data")
    parser2.add_argument('--export')
    args = parser2.parse_args()
    if args.export :
        extractMode = True
    else :
        # args = None
        extractMode = False
        print("pas d'argument export")
            


idee = SL.sqlLogMovie
def conectToDatabase():
    return mysql.connector.connect(user=f'{idee}', password=f'{idee}', host='127.0.0.1', database=f'{idee}')

conectToDatabase()

def disconectToDatabase(cnx):
    cnx.close()

def createCursor(cnx):
    return cnx.cursor(named_tuple=True) 

def closeCursor(cursor):
    cursor.close

def findQuery(table, id):
    return (f"SELECT*FROM {table} WHERE id={id}")

def find(table,id):
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    cursor.execute(findQuery(table,id))
    results = cursor.fetchall()
    closeCursor(cursor)
    disconectToDatabase(cnx)
    return results

def findAllQuery(tableFull):
    return (f"SELECT*FROM {tableFull}")

def findAll(tableFull):
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    cursor.execute(findAllQuery(tableFull))
    results = cursor.fetchall()
    closeCursor(cursor)
    disconectToDatabase(cnx)
    return results    

def CountVar(tableToCount,varToCount,whereToCount) : 
    return (f"SELECT {varToCount} COUNT FROM {tableToCount} WHERE{whereToCount}")

def execCountVar(varToCount,tableToCount,whereToCount):
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    cursor.execute(CountVar(varToCount,tableToCount,whereToCount))
    results = cursor.fetchall()
    count = 0
    for results in results :
        count +=1       
    closeCursor(cursor)
    disconectToDatabase(cnx)
    if extractMode :
        return results
    else :
        return count   

def insertTable(table,col,vals) :
    return (f"INSERT INTO {table} {col} VALUES {vals}")

def execInsertTable(table,col,vals) :
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    cursor.execute(insertTable(table,col,vals))
    cnx.commit()
    closeCursor(cnx)
    disconectToDatabase(cnx)
 
def deleteWhere(table,condition) :
    return (f"DELETE FROM {table} WHERE {condition}") 

def execDelete(table, condition) :
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    cursor.execute(deleteWhere(table,condition))
    cnx.commit()
    closeCursor(cnx)
    disconectToDatabase(cnx)

def addColumn(table,columnName,colType) :
    return (f"ALTER TABLE {table} ADD COLUMN {columnName} {colType}")

def execAddColumn(table, columnName, colType) :
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    cursor.execute(addColumn(table,columnName,colType))
    cnx.commit()
    closeCursor(cnx)
    disconectToDatabase(cnx)

def dropColumn(table,columnName,) :
    return (f"ALTER TABLE {table} DROP COLUMN {columnName}")

def execDropColumn(table, columnName) :
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    cursor.execute(dropColumn(table,columnName))
    cnx.commit()
    closeCursor(cnx)
    disconectToDatabase(cnx)

def updateTable(table,setVals,where) :
    return (f"UPDATE {table} SET {setVals} WHERE {where}")

def execUpdateTable(table,setVals,where) :
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    cursor.execute(updateTable(table,setVals,where))
    cnx.commit()
    closeCursor(cnx)
    disconectToDatabase(cnx)
     
def import_csv(args, firstcol,firstcase):
    ######  cmd = app.py context import firsCol firstcase --file xxxx.csv
    ######  exemple = app.py people import firstname Alain  --file new_people.csv
    ######  Cette fonction, est ok uniquement si on autorise les valeurs NULL depuis adminer
    ######  sur TOUTES les col sauf la premiére qu'on renseigne + la col ID si auto increment                
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    with open(args.file, 'r', encoding='utf-8', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        print("Import commencé")
        for row in reader:
            dl= row.keys()
            cursor.execute(f"INSERT INTO {args.context} ({firstcol}) VALUES ('{firstcase}')")
            for i in dl:
                k = f'{i}'
                valsRet = str(row[k])
                cursor.execute(f"UPDATE {args.context} SET {k} = ('{valsRet}') WHERE id=LAST_INSERT_ID()")          
    cnx.commit()            
    closeCursor(cursor)
    disconectToDatabase(cnx)    
    print("Import Terminé")  

def exctraction(nameVarWithData):
    if args.export:
        print("Exportation commencé")
        csvfile = open(args.export, 'w', newline='\n',encoding='utf-8')
        wr = csv.writer(csvfile)
        wr.writerow(nameVarWithData[0]._fields)
        for i in nameVarWithData:
            wr.writerow(i)
        csvfile.close()
        print("Exportation terminé !!")


def cmdExecut(): 

    #Action
    if args.context != None and args.Action == 'fetch':
        results=find(args.context, args.id)
        if args.export:
            exctraction(results)
        else:
            print("Résultat requete :")
            for i in results:
                print(i)
                    
    #Action
    elif args.context != None and args.Action == "list":
        results=findAll(args.context)
        if args.export:
            exctraction(results)
        else:
            print("Résultat requete :")
            for i in results:
                print(i)

     #Action
    elif args.context != None and args.Action == "count":
        if extractMode :
            results = execCountVar(args.context,args.var,args.whereToCount)
            exctraction(results)
        else :
            count =execCountVar(args.context,args.var,args.whereToCount)
            print("Résultat requete :")
            print(f"Résultat = {count}")
    #Action
    elif args.context != None and args.Action == 'insert':
        execInsertTable(args.context,args.col,args.vals)
        if args.export:
            exctraction(results)
        else:
            print("--Opération terminée avec succés--")
          
    #Action           
    elif args.context != None and args.Action == 'delete':
        execDelete(args.context, args.condition)
        if args.export:
            exctraction(results)
        else:
            print("--Opération terminée avec succés--")

    #Action           
    elif args.context != None and args.Action == 'ADD_COL':
        execAddColumn(args.context,args.columnName,args.colType)
        if args.export:
            exctraction(results)
        else:
            print("--Opération terminée avec succés--")

    #Action           
    elif args.context != None and args.Action == 'DROP_COL':
        execDropColumn(args.context,args.columnName)
        if args.export:
            exctraction(results)
        else:
            print("--Opération terminée avec succés--")  

    #Action           
    elif args.context != None and args.Action == 'update':
        execUpdateTable(args.context,args.setVals, args.where)
        if args.export:
            exctraction(results)
        else:
            print("--Opération terminée avec succés--")   
    #Action
    elif args.context != None and args.Action == 'import':
        if args.file :
            import_csv(args.typeK,args.firstcol,args.firstcase)                        
        else :
            print("Impossible d'importer le fichier")

def libreCode():
    print("Mettre du code pour commencer  !! ")
 

def voidUpdate() :

    if modechoice == 1 :

        affichage = """
    Choisissez une option:
    \t1: Saisir requête strict
    \t2: Executer votre fonction code libre et variable
    \t3: Afficher la sélection en mémoire
    \t4: Extraire la sélection en mémoire
    \t5: Terminer
        """
        option_choisie = 0

        while option_choisie != 5 :
            
            print(affichage)
            option_choisie = input("Choisir option : ")
            option_choisie = int(option_choisie)
        
            if option_choisie == 1 :
                requete = input("Requête strict :")
                
                cnx=conectToDatabase()
                cursor =createCursor(cnx)
                cursor.execute(requete)
                try:
                    results = cursor.fetchall()
                    print(results)
                except :
                    print("Pas de selection en mémoire")
                finally:
                    cnx.commit()
                
                if extractMode :
                    if args.export:
                        exctraction(results)
                else:
                    try:
                        print(results)
                    except :
                        print("Pas de selection à retourner")
                    finally:
                        print("--Opération terminée avec succés--") 

                closeCursor(cnx)
                disconectToDatabase(cnx)       

                    
            elif option_choisie == 2 :
                libreCode() 

            elif option_choisie == 3 :
                try : 
                    if results :
                        print ("  ------->  ")
                        print(results)
                        print ("  <-------  ")
                except : 
                    print("Votre selection est vide !") 

            elif option_choisie == 4 :
                    filemane = input("Nom du fichier avec extention :")
                    filemane = str(filemane)
                    try :
                        args.export = filemane
                        exctraction(results)
                        args.export = None
                    except : 
                        print("Extraction Impossible")
            # elif option_choisie == 7 :
            #     filemane = input("Nom du fichier avec extention :")
            #     firstcol = str(input("Nom de la première colonne : "))
            #     firstcase = str(input("Nom de la première case :"))
            #     import_csv(filemane,firstcol,firstcase)                         
    if modechoice == 0 :
         cmdExecut()
           

voidUpdate()

print("Programme terminé !")


# def import_col_csv(args, typeK): 
#     #-import de col avec data-             
#     cnx=conectToDatabase()
#     cursor =createCursor(cnx)
#     with open(args.file, 'r', encoding='utf-8', newline='\n') as csvfile:
#         reader = csv.DictReader(csvfile)
#         print("Import commencé")
#         for row in reader:
#             dl= row.keys()
#             print(row)
#             for i in dl:
#                 k = f'{i}'
#                 cursor.execute(f"ALTER TABLE {args.context} ADD COLUMN {k} {typeK}")
#                 for row in reader:    
#                     print("call")
#                     valsRet = str(row[k])
#                     print(valsRet)
#                     cursor.execute(f"UPDATE {args.context} SET {k} = ('{valsRet}') WHERE {k} IS NULL")
#                     print("call")        
#     cnx.commit()            
#     closeCursor(cursor)
#     disconectToDatabase(cnx)    
#     print("Import Terminé") 
#-----------------------------------------------------------
#Action
# elif args.context != None and args.Action == "import_col":
#     if args.file :
#         import_col_csv(args,args.typeK)                        
#     else :
#         print("Impossible d'importer le fichier")



