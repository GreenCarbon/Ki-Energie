pfad = "/Users/ingo/Entwicklung/"
datei = '2021-11-03_LOG.txt'
logdatei = pfad + datei
f = open(logdatei,'r')
zeilen = f.readlines()
f.close()

del zeilen[3]
f = open(logdatei, 'w')

for l in zeilen:
    f.write(l)

f.close()
