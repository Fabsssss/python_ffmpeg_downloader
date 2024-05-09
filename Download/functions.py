from bs4 import BeautifulSoup
import requests
import os



def get_html(url):
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            raise ValueError("Failed to retrieve the webpage. Status code:", response.status_code)
            

def correctString(string):
        ersetzte_string = ""
        ersetzungszeichen = "/\\:*?\"<>|"
        for char in string:
            if char in ersetzungszeichen:
                ersetzte_string += ' '
            else:
                ersetzte_string += char
        return (ersetzte_string.strip())


def erstelle_ordner_wenn_nicht_vorhanden(verzeichnis):
    if not os.path.exists(verzeichnis):
        os.makedirs(verzeichnis)
        print(f"Ordner {verzeichnis} wurde erstellt.")
    else:
         return


def erstelle_datei_wenn_nicht_vorhanden(dateipfad, inhalt=None):
    if not os.path.exists(dateipfad):
        with open(dateipfad, 'w') as datei:
            if inhalt is not None:
                datei.write(inhalt)
            print(f"Datei {dateipfad} wurde erstellt.")
    else:
        return
    

def entferne_und_gebe_doppelte_aus(dateipfad):
    try:
        with open(dateipfad, 'r') as datei:
            zeilen = datei.readlines()
        doppelte_zeilen = [zeile for zeile in zeilen if zeilen.count(zeile) > 1]
        if not doppelte_zeilen:
            print('Keine doppelten Zeilen gefunden.')
        else:
            print('Doppelte Zeilen:')
            for zeile in set(doppelte_zeilen):
                print(zeile.strip())
            bereinigte_zeilen = list(set(zeilen))
            with open(dateipfad, 'w') as datei:
                datei.writelines(bereinigte_zeilen)
            print(f'Doppelte Zeilen in {dateipfad} wurden entfernt.')
    except FileNotFoundError:
        print(f'Die Datei {dateipfad} wurde nicht gefunden.')


def entferne_string_aus_datei(dateipfad, zu_entfernender_string):
    with open(dateipfad, 'r') as datei:
        inhalt = datei.read()
    neuer_inhalt = inhalt.replace(zu_entfernender_string, '')
    with open(dateipfad, 'w') as datei:
        datei.write(neuer_inhalt)
    print("Link entfernt")













def add_test_to_mp4_filenames(directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith('.mp4'):
                    
                    original_path = os.path.join(root, file)
                    try:
                        spl = file.split("_")
                        new_filename = os.path.dirname(os.path.join(root, file))+"\\"+spl[0]+"_"+spl[1]+"_"+spl[2]+"_"+(correctString(spl[3])).strip()+"_"+spl[4]
                        #print("original "+original_path)
                        #print("Not orig "+new_filename)
                    except Exception as e:
                        new_filename = os.path.dirname(os.path.join(root, file))+"\\"+"Name nicht vorhanden.mp4"
                        print(original_path)
                        print(new_filename)
                    if 1 == 1:
                        try:
                            os.rename(original_path, new_filename)
                            print(f"Renamed: {original_path} to {new_filename}")
                        except Exception as e:
                            print(f"Error renaming {original_path}: {e}")
   

#o = 'G:\\Serien\\Anime\\The Disastrous Life of Saiki K\\Staffel 1\\1.mp4'
#r = correctString('G:\\Serien\\Anime\\The Disastrous Life of Saiki K\\Staffel 1\\The Disastrous Life of Saiki K._1_19_Hurray! Tsundere Grandpa + Hip, Hip, Hurray! Tsundere Grandpa + Welcome to the Farthest Amusement Park! + See You Again! Saying Goodbye to the Grandparents + Congratulations on the Video Game Release! Kunio Saitou s Horror Stories_GermanSub.mp4')
#os.rename(o, r)
#while 1 == 1:
#    print("e")
#test = "https://delivery-node-ipaibnrz5uui2crj.voe-network.net/engine/hls2-c/01/00218/un4k4bbtfu05_,n,.urlset/master.m3u8?t=mbS0bO2lMkS6imfMu_txoBlK0uQaoZbKeH_rplrYdFU&s=1703887259&e=14400&f=1093524&node=delivery-node-xqrgj99p8krmzj4e.voe-network.net&i=213.196&sp=2500&asn=8422"
#m3u8_To_MP4.multithread_download(test,"test.mp4")
#add_test_to_mp4_filenames('G:\\Serien\\Anime')
                            
                            