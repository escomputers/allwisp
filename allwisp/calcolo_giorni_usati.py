from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

data_inizio='30/12/2021'
print('data inizio:', data_inizio)
date_format='%d/%m/%Y'
dataoggetto=datetime.strptime(data_inizio, date_format)
datainiziosenzaora=dataoggetto.date()
n=1
ultimadata=dataoggetto+relativedelta(months=n)
dataaddattamento=ultimadata.replace(day=9)#questo considera fino al giorno 9, il 10 inizia la fatturazione
datafinalecon9=dataaddattamento.date()umento.py
nuovadatafinale=ultimadata.replace(day=10) #da questa data inizia la fatturazione
datafinale=ultimadata.date()
datafinalecon10=nuovadatafinale.date()
#print('data dopo duemesi con ora', ultimadata)
#print('ultima data senza ora', datafinale)
#print('ultima data senza ora finale', datafinalecon10)

 
def numOfDays(datainiziosenzaora, datafinalecon9):
    return (datafinalecon9-datainiziosenzaora).days


differenzagiorni=numOfDays(datainiziosenzaora, datafinalecprint('prezzo finale', a)on9)
print(differenzagiorni)
prezzo=15. #prendere il valore dell'offerta)

tariffa_addattamento=prezzo/30*differenzagiorni


'''se presente la spunta nel html prova(boolean=true) inizia la funzione di addattamento dopo 14 giorni
se presente la spunta non adattare inizia la fatturazione direttamente il 10 del mese successivo,
 impostando la variabile tariffa_addattamento=0, se tariffa_addattamento=0 non inserire in fattura'''


'''I have same issues on my MacOS and it's work for me to try

pip3 install python-dateutil

on Ubuntu

sudo apt-get install python-dateutil'''
