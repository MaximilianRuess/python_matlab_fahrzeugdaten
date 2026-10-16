# Woche 1 / Kapitel 3
#Maximilian Ruess 

# # --- Indentation --- 

# kuehlmittel_temp = 105

# if kuehlmittel_temp > 100: 
#     print("Warnung: Motor zu heiss")
#     print("Leistung wird reduziert")
# print("Pruefung abgeschlossen")

# if kuehlmittel_temp > 100: 
#     print("Warnung: Motor zu heiss")
#     print("Leistung wird reduziert")
#     print("Pruefung abgeschlossen")

# # --- Temperaturklassifizierung ---

kuehlmittel_temp2 = float(input("Kuehlmitteltemperatur: "))

if kuehlmittel_temp2 < 60: 
    print("Motor kalt!")

elif 60 <= kuehlmittel_temp2 <= 105:
    print("Betriebstemperatur erreicht!")

else: 
    print("Ueberhitzung")


