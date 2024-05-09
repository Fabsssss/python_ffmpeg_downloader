import os

from Download.serie import Serie
#from controll import Controll
#import m3u8_To_MP4
#from functions import entferne_string_aus_datei, entferne_und_gebe_doppelte_aus, correctString

    

#pfad = 'G:\\Serien\\Anime\\Classroom of the Elite\\Staffel 2\\3.mp4'
#rrr = "G:\\Serien\\Anime\\Classroom of the Elite\\Staffel 2\\Classroom of the Elite_2_2_Es gibt zwei menschliche Hauptsünden, aus welchen sich alle anderen ableiten  Ungeduld und Lässigkeit.There are two main human sins from which all the others derive  impatience and indolence._German.mp4"
#os.rename(pfad, rrrr)
#while 1 == 0:
#    i = 0


#kontrollpfad = 'G:\\Serien\\Anime\\kontroll.txt'
dateipfad = 'F:\\Serien\\Anime\\serien.txt'
#entferne_und_gebe_doppelte_aus(dateipfad)
#with open(dateipfad, 'r') as datei:
#    for zeile in datei:
#        inhalt = (zeile.replace('\n','')).strip()
#        d = Controll(kontrollpfad, str(inhalt))

with open(dateipfad, 'r') as datei:
    for zeile in datei:
        inhalt = (zeile.replace('\n','')).strip()
        d = Serie(str(inhalt), os.path.dirname(dateipfad))
        #entferne_string_aus_datei(kontrollpfad, zeile)







