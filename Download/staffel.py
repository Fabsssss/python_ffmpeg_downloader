from bs4 import BeautifulSoup
from Download.episode import Episode
import os
from Download.functions import get_html
import time

class Staffel:

    def __init__(self, url,serie):
        self.serie = serie
        self.path = serie.get_path()
        self.url = url
        self.episodenListe = []
        self.html = get_html(self.url)        
        self.staffelName = self.get_staffel()
        self.createDir() 

        self.vorhandeneEpisoden = {}
        self.get_mp4_file_paths(self.path)

        #for key, value in self.vorhandeneEpisoden.items():
        #    print(key, value)

        self.list_of_not_downloaded_animes ={}
        self.suche_noch_downloadbare_epsioden()

        for key, value in self.list_of_not_downloaded_animes.items():
            if "film" in self.url[self.url.rfind('/')+1:]:
                Episode(self,self.url+"/film-"+key, value, key)
            else:
                Episode(self,self.url+"/episode-"+key, value, key)


        return 
        
        #self.delete_double_episodes()
        

        

        if len(self.list_of_not_downloaded_animes) >= 1:
            self.downloaded()
        else:
            return
        return
        self.get_episode()



    def get_staffel(self):
        active_links = self.html.find_all('a', class_='active')
        for link in active_links:
            return link.text
        
    
    def createDir(self):
        sta = self.staffelName
        if "Film" not in sta:
            sta = "Staffel "+sta
        self.path = self.path+"\\"+sta
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def get_mp4_file_paths(self,directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".mp4"):
                    try:
                        sp = file.split("_")
                        if sp[4] == "German.mp4":
                            self.vorhandeneEpisoden[sp[2]] = "True"
                        else:
                            self.vorhandeneEpisoden[sp[2]] = "False"
                    except Exception as e:
                        print(f"Unexpected error: {e}")
    

    def delete_double_episodes(self):
        for f in self.vorhandeneEpisoden:
            for s in self.vorhandeneEpisoden:
                if f.split(",")[0] == s.split(",")[0]:
                    if f.split(",")[1] == s.split(",")[1]:
                        if f.split(",")[2] != s.split(",")[2]:
                            print(f)
                            print(s)

#if nicht deutsch aber deutsch vorhanden oder gar nicht vorhanden
    def suche_noch_downloadbare_epsioden(self):
        elements = self.html.find_all(attrs={'data-episode-season-id': True})
        for element in elements:
            if element['data-episode-season-id'] in self.vorhandeneEpisoden:
                if self.vorhandeneEpisoden[element['data-episode-season-id']] == False and 'title="Deutsch/German"' in str(element):
                    self.list_of_not_downloaded_animes[element['data-episode-season-id']] = "True"
            else:
                if 'title="Deutsch/German"' in str(element):
                    self.list_of_not_downloaded_animes[element['data-episode-season-id']] = "True"
                else:
                    self.list_of_not_downloaded_animes[element['data-episode-season-id']] = "False"
            continue



            if element['data-episode-season-id'] != "none":
                for episo in self.vorhandeneEpisoden:
                    if episo == str(element['data-episode-season-id']):
                        if "/german.svg" in str(element) and episo.split(",")[2] == "False": # not episo.get_german():
                            i = 0
                            #self.list_of_not_downloaded_animes.append(element)
                            #print("Deutsch Vorhanden "+ self.serie.get_title()+" "+self.staffelName+" "+str(element['data-episode-season-id']))
                        gefunden = True
                        break
                if not gefunden:
                    i = 0
                    #self.list_of_not_downloaded_animes.append(element)
                    #print("Noch nicht Gedownloadet "+ self.serie.get_title()+" "+self.staffelName+" "+str(element['data-episode-season-id']))


          





































    


  

    def downloaded(self):
        all_a_tags = [element.find('a') for element in self.list_of_not_downloaded_animes]
        filtered_a_tags = list(filter(None, all_a_tags))
        for a_tag in filtered_a_tags:
            #epidode = Episode("https://aniworld.to"+a_tag['href'],self.path,self.serie.get_title() +"_"+self.staffelName)
            #self.episodenListe.append(epidode)
            i = 0


    def get_episode(self):
        alreadyList = []
        a_elements = self.html.select('.seasonEpisodesList a')
        for a_element in a_elements:
            if str(a_element.get('href')) not in alreadyList:
                try:
                    #epidode = Episode("https://aniworld.to"+a_element.get('href'),self.path,self.serie.get_title()+"_"+self.staffelName)
                    #self.episodenListe.append(epidode)
                    alreadyList.append(str(a_element.get('href')))
                except Exception as e:
                    print(f"Unexpected error: {e}")
