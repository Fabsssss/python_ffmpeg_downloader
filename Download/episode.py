from bs4 import BeautifulSoup
import requests
import m3u8_To_MP4
import os
import time
from Download.functions import get_html, correctString

class Episode:
    def __init__(self, staffel,url, german, episodennummer):
        self.staffel = staffel
        self.url = url
        self.german = german
        self.episodenNummer = episodennummer
        self.htmlsoup = get_html(self.url)
        
        self.episodentitel = self.get_titelofEpisode()

        self.dateiname = self.get_dateiname()
        self.downloadLink = self.get_downloadLink()
        self.download()
        return


    def get_titelofEpisode(self):
        h2_tags = self.htmlsoup.find_all('h2')
        for h2_tag in h2_tags:
            if h2_tag.find('span') is not None:
                return(h2_tag.find('span').text)
            else:
                return(h2_tag.find('small').text)
    
    # serientitel_staffel_episodennummer_episodentitel_sprache.mp4
    def get_dateiname(self):
        if self.german == "True":
            filename = self.ueberlange((str(self.staffel.path+"\\"+correctString(self.staffel.serie.titleOfTheSeries)+"_"+self.staffel.staffelName+"_"+correctString(self.episodenNummer)+"_"+correctString(str(self.episodentitel).replace("_"," ")) +"_"+"German.mp4").replace("\n","")))
            #if os.path.exists((str(self.path+"\\"+self.correctString(self.filename)+"_"+self.correctString(self.episodenNummer)+"_"+self.correctString(str(self.episodentitel).replace("_"," ")) +"_"+"GermanSub.mp4").replace("\n",""))):
            #    os.remove((str(self.path+"\\"+self.correctString(self.filename)+"_"+self.correctString(self.episodenNummer)+"_"+self.correctString(str(self.episodentitel).replace("_"," ")) +"_"+"GermanSub.mp4").replace("\n","")))
        else:
            filename = self.ueberlange((str(self.staffel.path+"\\"+correctString(self.staffel.serie.titleOfTheSeries)+"_"+self.staffel.staffelName+"_"+correctString(self.episodenNummer)+"_"+correctString(str(self.episodentitel).replace("_"," ")) +"_"+"GermanSub.mp4").replace("\n","")))
        return filename
    
    def ueberlange(self,s):
        if len(os.path.basename(s)) > 255:
            spl = os.path.basename(s).split("_")
            s = os.path.dirname(s)+"\\"+spl[0]+"_"+spl[1]+"_"+spl[2]+"_"+spl[3][:255-len(spl[4])-len(spl[3])-len(spl[2])-len(spl[1])-len(spl[0])-4]+"_"+spl[4]
            return s
        else:
            return s
        
    def get_downloadLink(self):
        s = str(self.htmlsoup).split("\"")
        for a in s:
            if "/redirect/" in a:
                response = requests.get(("https://aniworld.to"+a))
                if not self.german:
                    response = requests.get(self.getRightDonwloadLink(response)) 
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    res = (str(soup)).split("'")
                    for r in res:
                        if "m3u8" in r:
                            return r.split('"')[3]
                else:
                    print("Failed to retrieve the webpage. Status code:", response.status_code)
                    return

    def getRightDonwloadLink(self,string):
        div_element = self.htmlsoup.find('div', class_='changeLanguageBox')
        if div_element:
            img_count = len(div_element.find_all('img'))
            if img_count == 2:
                sp = str(self.htmlsoup).split("\"")
                list_of_re = []
                for s in sp:
                    if "/redirect/" in s:
                        list_of_re.append("https://aniworld.to"+s)
                return (list_of_re[int(len(list_of_re)/2)])
            else:
                sp = str(self.htmlsoup).split("\"")
                list_of_re = []
                for s in sp:
                    if "/redirect/" in s:
                        return "https://aniworld.to"+s
        return string   

    def download(self):
        try:
            if not os.path.exists(self.dateiname):
                m3u8_To_MP4.multithread_download(self.downloadLink, self.dateiname)
            else:
                print("Datei Exestiert bereits!!!!!!!!!!!!!!!!!!!!!!!!!!")
        except Exception as e:
            print(f"Unexpected error: {e}")     












































    def get_episodenNummer(self):
        active_links = self.htmlsoup.find_all('ul')
        for link in active_links:
            if "<strong>Episoden:</strong>" in str(link) or "<strong>Filme:</strong>" in str(link):
                active_links = link.find_all('a', class_='active')
                for link in active_links:
                    return link.text



    def get_german(self):                   
        element = self.htmlsoup.find(class_="changeLanguageBox")
        if element:
            if "German, Deutsch, Flagge, Sprache" in (str(element)):
                return True
            else:
                return False

        
    

    

