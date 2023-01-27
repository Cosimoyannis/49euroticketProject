

Hierbei handelt es sich um ein "gecleantes" Projekt bei dem nur die nötigsten Dateien enthalten sind.

------------------

Was befindet sich wo?


In dem Ordner: Data_Scraping
    Python Code der zum Erlangen der CSV Dateien benötigt wurde.
    Hier wurden Twitter und Youtube mit Hilfe der jeweiligen API abgefragt.

In dem Ordner: Sentiment_Analysis
    Python Code um die finalen Kommentare zu analisieren. 
    -> $conda activate "pythonumgebung"
    -> $python run sentimentAnalysisTrained.py

In dem Ordner: workingCSV
    Finale CSV Datei(en) mit den Kommentaren von Twitter und Youtube zusammengefügt. 
    TheFinalCombinedDataset = CSV Datei mit zwei Spalten für das Öffnen mit Excel oder Numbers.
    TheFinalCombinedDatasetOneLine = CSV Datei, welche im Projekt genutzt wird aber nur eine einzige Spalte hat.

------------------

Wie sind wir zu dem finalen Datensatz gekommen?

Twitter:
$python run Data_Scraping/ScrapeTwitterUpdatedFull_Archive.py

Youtube:
$python run Data_Scraping/ScrapeYouTube.py

