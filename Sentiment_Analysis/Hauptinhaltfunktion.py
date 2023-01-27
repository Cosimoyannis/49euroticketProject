from turtle import pd

from textblob import TextBlob
import pandas as pd

# Define the text
#text = "This is an example of a text. It contains some random sentences. The main content of this text is the example and the random sentences."
comments = pd.read_csv('../workingCSV/TheFinalCombinedDatasetOneLine.csv', header=None, names=["comments"],sep='\t')
df_list = []
# Create a TextBlob object
#blob = TextBlob(text.to_string())# Extract the main content
for comment in comments["comments"]:
    blob = TextBlob(comment)
    main_content = comment + " Thema: "
    if "Auto" in comment:
        main_content += str('Man diskutiert über 49euro Ticket in Sinne von Autofahrer')
    elif "Klima" in comment or "umweltfreundlich" in comment or "Energiekrise" in comment:
        main_content += str('Es geht um Thema Klimaschutz')
    elif "Entlastung" in comment:
        main_content += str('Man findet 49Euro Ticket als Entlastung von Ausgabe')
    elif "Preis" in comment or "günstig" in comment or "teuer" in comment or "sparsam" in comment or "sparen" in comment or "Finanzen" in comment or "Geld" in comment or "Finanzierung" in comment:
        main_content += str('Man diskutiert über Preis')
    elif "Politik" in comment or "politisch" in comment or "Bundesregierung" in comment or "Regierung" in comment:
        main_content += str('Man redet von Politik')
    elif "Arbeit" in comment or "Job" in comment:
        main_content += str('Man redet von Fahrt zu/von Arbeit')
    elif "9 Euro Ticket" in comment or "9euro" in comment:
        main_content += str('Man vergleicht 49 Euro Ticket mit 9 Euro Ticket')
    elif "Digitalisierung" in comment or "digital" in comment:
        main_content += str('Thema ist Digitalisierung')
    elif "Stau" in comment or "Maske" in comment or "Maskenpflicht" in comment or "Impfung" in comment:
        main_content += str('Man diskutiert über mögliche Probleme')
    else: main_content += str('Random Content')
    print(main_content)
    df = pd.DataFrame({'main_content': [main_content]})
    df_list.append(df)

result = pd.concat(df_list)

# Write the DataFrame to a CSV file
result.to_csv('main_content.csv', index=False)


# Output: "This is an example of a text. It contains some random sentences."




# blob = TextBlob(text.to_string())
# main_content = " ".join(blob.noun_phrases)
#print(main_content)