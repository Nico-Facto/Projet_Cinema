import mysql.connector
import requests
import argparse
from datetime import datetime
from bs4 import BeautifulSoup
import locale
from pandas import read_csv
from sec import secureLog as SL
# import isodate


locale.setlocale(locale.LC_ALL, 'en_US') # Anglais 'en_GB' ou 'en_US'


goToDataBase = True
idee = SL.sqlLogMovie


def conectToDatabase():
    return mysql.connector.connect(user=f'{idee}', password=f'{idee}', host='database', database=f'{idee}')

conectToDatabase()

def disconectToDatabase(cnx):
    cnx.close()

def createCursor(cnx):
    return cnx.cursor(named_tuple=True) 

def closeCursor(cursor):
    cursor.close

def sendTodataBase() :
    conectToDatabase()

def autoscrap():
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    
    df = read_csv("DataPip/filteredDB.csv")
    print("Scrap vers Base")

    for newID in df["id"] :
        budl = 0
        boxoffice = ""
        vactors = ""

        imdb_id = str(newID)

        try :
            r = requests.get(f"https://www.imdb.com/title/{newID}", headers={"Accept-language" : "fr-fr"})
            print(r) # doit retourné rep 200 pour ok
            print(f"{newID}")
            soup = BeautifulSoup(r.text, "html.parser")

            titleO = soup.find(class_='title_wrapper').find('h1').get_text().split("(")[0] # id est unique sur la page
            titleUn = titleO.replace("\xa0","")

            duration = soup.find(class_="subtext").find('time').get_text().strip()
            vartime = datetime.strptime(duration,'%Hh %Mmin')
            durtime = vartime.hour*60 + vartime.minute
            # duration = isodate.parse_duration("PT155M")
            # print(int(duration.total_seconds()/60))

            release = soup.find(class_="subtext").find(attrs={'title':"See more release dates"}).get_text().split("(")[0]
            release_dates_as_string = release.strip()# 9 octobre 2019
            release_date_object = datetime.strptime(release_dates_as_string,'%d %B %Y')
            rdo_sql = release_date_object.strftime('%Y-%m-%d')

            try :
                for content in soup.findAll("h4"):
                    if content.text == "Certificate:":
                        rating = content.find_next("span").text
                        if "public" in rating :
                            rating = 'TP'
                        elif "PG" in rating :
                            rating = "-12"
                        else :
                            rating = f'-{rating}' 
            except :
                print("ratingfailed")
                rating = "TP"                          
                        
            try :        
                for content in soup.findAll("h4"):
                    if content.text == "Budget:":
                        frt = (content.parent.contents[2].strip().split("$")[1])#parent.contents me donne toute la ligne, je prend le 2 eme.strip().split(valeur qui defini la separation,valeur que je scrap)
                        bud = frt.replace(",","")
                        budl = int(bud)
            except :
                budl = 0
                print("budgetfailed")
                              
                              
            # director = soup.find(class_="plot_summary").find("a").get_text()

            token = SL.token
            url2 = f"http://www.omdbapi.com/?i={newID}&apikey={token}&imdbID={newID}"
            response= requests.get(url2)
            print(response)
            response_json = response.json() 

            vactors = response_json['Actors']
            vplots = response_json['Plot']
            vprod = response_json['Production']
            vgenre = response_json['Genre']
            director = response_json['Director']
            vcontry = response_json['Country']
            vwriter = response_json['Writer']

            note = soup.find(class_="ratingValue").find_next("span").text
            note = note.replace(",",".")

            for content in soup.findAll("h4"):
                if content.text == "Cumulative Worldwide Gross:":
                    frt = (content.parent.contents[2].strip().split("$")[1])#parent.contents me donne toute la ligne, je prend le 2 eme.strip().split(valeur qui defini la separation,valeur que je scrap)
                    box = frt.replace(",","")
                    boxoffice = int(box)

            vals = imdb_id,titleUn,durtime,vplots,vgenre,rdo_sql,rating,budl,director,vactors,vprod,vwriter,vcontry,note,boxoffice

            if goToDataBase :
                try :
                    cursor.execute(f"INSERT INTO movies (imdb_id,title,duration,synopsis,genre,release_date,rating,prod_budget,director,people,produceur,writer,country,target,box_office) VALUES {vals}")
                    cnx.commit()
                    print(vals)
                    print("Import dans la BD ok")
                except :
                    print("import failed")    
            else :
                print(vals) 
        except :
            print("requête failed")
    closeCursor(cnx)
    disconectToDatabase(cnx)        

def scrapOnPred() :

    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    
    df = read_csv("DataPip/id_movies_ic.csv")
    print("Scrap vers Pred")
    for newID in df["id"] :
        budl = 0
        vactors = ""
    
        imdb_id = str(newID)

        r = requests.get(f"https://www.imdb.com/title/{newID}", headers={"Accept-language" : "fr-fr"})
        print(r) # doit retourné rep 200 pour ok
        print(f"{newID}")
        soup = BeautifulSoup(r.text, "html.parser")

        try : 
            titleO = soup.find(class_='title_wrapper').find('h1').get_text().split("(")[0] # id est unique sur la page
            titleUn = titleO.replace("\xa0","")

            duration = soup.find(class_="subtext").find('time').get_text().strip()
            vartime = datetime.strptime(duration,'%Hh %Mmin')
            durtime = vartime.hour*60 + vartime.minute
            # duration = isodate.parse_duration("PT155M")
            # print(int(duration.total_seconds()/60))

            release = soup.find(class_="subtext").find(attrs={'title':"See more release dates"}).get_text().split("(")[0]
            release_dates_as_string = release.strip()# 9 octobre 2019
            release_date_object = datetime.strptime(release_dates_as_string,'%d %B %Y')
            rdo_sql = release_date_object.strftime('%Y-%m-%d')

            # try :
            #     for content in soup.findAll("h4"):
            #         if content.text == "Certificate:":
            #             rating = content.find_next("span").text
            #             if "public" in rating :
            #                 rating = 'TP'
            #             elif "PG" in rating :
            #                 rating = "-12"
            #             else :
            #                 rating = f'-{rating}' 
            # except :
            #     print("ratingfailed")
            rating = "TP"                          
                        
            try :        
                for content in soup.findAll("h4"):
                    if content.text == "Budget:":
                        frt = (content.parent.contents[2].strip().split("$")[1])#parent.contents me donne toute la ligne, je prend le 2 eme.strip().split(valeur qui defini la separation,valeur que je scrap)
                        bud = frt.replace(",","")
                        budl = int(bud)
            except :
                print("budgetfailed")
                                
            token = SL.token
            url2 = f"http://www.omdbapi.com/?i={newID}&apikey={token}&imdbID={newID}"
            response= requests.get(url2)
            print(response)
            response_json = response.json() 

            vactors = response_json['Actors']
            vplots = response_json['Plot']
            vprod = response_json['Production']
            vgenre = response_json['Genre']
            director = response_json['Director']
            vcontry = response_json['Country']
            vwriter = response_json['Writer']

            vals = imdb_id,titleUn,durtime,vplots,vgenre,rdo_sql,rating,budl,director,vactors,vprod,vcontry,vwriter

            if goToDataBase :
            
                cursor.execute(f"INSERT INTO inc_movies (imdb_id,title,duration,synopsis,genre,release_date,rating,prod_budget,director,people,produceur,country,writer) VALUES {vals}")
                cnx.commit()
                print(vals)
                print("Import dans la BD ok")
            else :
                print(vals) 
        except :
            print("requête failed")
    closeCursor(cnx)
    disconectToDatabase(cnx)

def scrapOnTarget():
    cnx=conectToDatabase()
    cursor =createCursor(cnx)
    
    df = read_csv("Pred_Files/suivi_mod_janv.csv")
    print("Scrap vers Target")
    for newID in df["imdb_id"] :
    
        imdb_id = str(newID)

        
        r = requests.get(f"https://www.imdb.com/title/{newID}", headers={"Accept-language" : "fr-fr"})
        print(r) # doit retourné rep 200 pour ok
        print(f"{newID}")
        soup = BeautifulSoup(r.text, "html.parser")

        try :
            target = soup.find(class_="ratingValue").find_next("span").text
            target = target.replace(",",".")
            print(target)
        except :
            target = 0
            print(target)    

        cursor.execute(f"UPDATE inc_movies SET target = {target} WHERE imdb_id = ('{imdb_id}')")
        cnx.commit()
        print("Import dans la BD ok")    
    closeCursor(cnx)
    disconectToDatabase(cnx)
  
mod = (int(input("0 pour Scrap base, 1 pour Scrap pred, 2 Scrap target : ")))
if mod == 0:
    autoscrap()
elif mod == 1 :
    scrapOnPred()
elif mod == 2 :
    scrapOnTarget()
       

print("Programme terminé !! ")
