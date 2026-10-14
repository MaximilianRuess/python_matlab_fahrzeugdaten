#Woche-1 / Kapitel 1&2 
#Maximilian Ruess

#--------Leistungsberechnung--------------------

pi = 3.14159
drehmoment_nm = 350 #Nm 
drehzahl_upm = 4000 #1/min

leistung_w = (drehmoment_nm*drehzahl_upm*2*pi)/60 
leistung_kW = leistung_w / 1000

print("Leistung:", round(leistung_kW, 1), "kW")

#--------Operatoren und Divisionen-------------

print(1000/2*5) 
print(1000/(2*5))

print(7/2)
print (7//2)
print(7%2) 
print(10//2)

#-----------Prüfstand------------------

#Testdauer: 2h 3min 4s -> 7384 s

testdauer_s = 7384 #s
volle_stunden = testdauer_s//3600 #h 
rest_s = testdauer_s % 3600 #s
minuten = rest_s // 60 #min 
restliche_sekunden = rest_s % 60 #s 

print(volle_stunden, "h") 
print(rest_s, "sekunden")
print(minuten, "min")
print(restliche_sekunden, "übrige sekunden in s")

print("Testdauer gesamt:", volle_stunden, "h", minuten, "min", restliche_sekunden, "s")