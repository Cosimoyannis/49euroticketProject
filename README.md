

Hierbei handelt es sich um ein "gecleantes" Projekt bei dem nur die nötigsten Dateien enthalten sind.

------------------------------------

Vorbereitung 

Python Umgebung
-> $ conda activate "pythonumgebung"

requirements.txt installieren
    -> $ pip install -r requirements.txt

------------------------------------

Was befindet sich wo?


In dem Ordner: Data_Scraping
    Python Code der zum Erlangen der CSV Dateien benötigt wurde.
    Hier wurden Twitter und Youtube mit Hilfe der jeweiligen API abgefragt.
    Der Code für das Twitter Scraping befindet sich direkt im Ordner.
    Der Code für das Youtube Scraping befindet sich im Unterordner YouTubeScraping.


In dem Ordner: Sentiment_Analysis
    Python Code um die finalen Kommentare zu analisieren. 
    -> $ conda activate "pythonumgebung"
    -> $ python run sentimentAnalysisTrained.py

In dem Ordner: workingCSV
    Finale CSV Datei(en) mit den Kommentaren von Twitter und Youtube zusammengefügt. 
    TheFinalCombinedDataset = CSV Datei mit zwei Spalten für das Öffnen mit Excel oder Numbers.
    TheFinalCombinedDatasetOneLine = CSV Datei, welche im Projekt genutzt wird aber nur eine einzige Spalte hat.

------------------------------------

Wie sind wir zu dem finalen Datensatz gekommen?

1.
Twitter:
$ python run Data_Scraping/ScrapeTwitterUpdatedFull_Archive.py

2.
Youtube:
$ python run Data_Scraping/YouTubeScraping/yt_public.py

3.
Überflüssige Spalten wurden manuell gelöscht in Numbers gelöscht, sodass nur noch zwei Spalten übrig sind.
Eine von den Spalten sollte die Kommentare enthalten und die andere Spalte sollte leer sein.

4.
Kombination von beiden Datensätzen 

4.1 
$cd "Ordner an dem sich die zu kombinierenden CSV Dateien befinden"
4.2
$ cat *.csv >combined.csv

5. 
Die leere Spalte sollte nun gelöscht werden, sodass nur noch eine Spalte übrig bleibt.

6. 
Diese Datei kann nun als Quelle zum analysieren genutzt werden.

------------------------------------

Kommentaranalyse starten: 

-> $ conda activate "pythonumgebung"
-> $ pip install -r requirements.txt
-> $ python run sentimentAnalysisTrained.py