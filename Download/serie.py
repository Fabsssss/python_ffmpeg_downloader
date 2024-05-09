from bs4 import BeautifulSoup
from Download.staffel import Staffel
from Download.functions import get_html, correctString, erstelle_ordner_wenn_nicht_vorhanden, erstelle_datei_wenn_nicht_vorhanden


class Serie:
    def __init__(self, url, path):
        self.path = path
        self.url = url
        self.staffel = []
        self.html = get_html(self.url)
        self.titleOfTheSeries = self.getTitleOfTheSeries()
        print("Serie: "+self.titleOfTheSeries)
        self.checkpath()
        self.get_list()


    def getTitleOfTheSeries(self):
        spanObjects = self.html.find_all('h1')
        for h1 in spanObjects:
            return correctString(h1.text)

    def checkpath(self):
        erstelle_ordner_wenn_nicht_vorhanden(self.path+"\\"+self.titleOfTheSeries)
        erstelle_datei_wenn_nicht_vorhanden(self.path+"\\"+self.titleOfTheSeries+"\\information.txt", self.url)
        self.path = self.path+"\\"+self.titleOfTheSeries


    def get_list(self):
        stream_element = self.html.find(id='stream')
        li_elements = stream_element.find_all('li')
        for li in li_elements:
            a_element = li.find('a')
            if a_element:
                if "episode" not in str(a_element):
                    i = 0
                    print ("https://aniworld.to"+a_element.get('href'))
                    staff = Staffel("https://aniworld.to"+a_element.get('href'), self)
                    self.staffel.append(staff)
        return
    


    def get_url(self):
        return self.url
    
    def get_title(self):
        return self.titleOfTheSeries

    def get_path(self):
        return self.path

