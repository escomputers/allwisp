class Prodotti_magazzino (models.Model):
	nome_prodotto = models.CharField(max_length=256)
	codiceprodotto = models.CharField(max_length=256,blank=True)
	prezzo_acquisto_no_iva = models.FloatField( blank=True, null=True)
	iva_percento=models.FloatField( blank=True, null=True)
	prezzo_vendita = models.FloatField( blank=True, null=True)
	colore=models.CharField(max_length=256)
	versione=models.CharField(max_length=256)
	fornitori = models.ForeignKey('customer.Fornitori', on_delete=models.CASCADE)
	data_acquisto = models.DateField(blank=True, null=True)
	quantita = models.FloatField( blank=True, null=True)
	descrizione = models.CharField(max_length=256,blank=True)
	Marca = models.CharField(max_length=256,blank=True)
	note = models.TextField(blank=True)
	codice_campo_prodotto= models.CharField(max_length=256,blank=True)
	file=models.FileField()

	def __str__(self):
		return self.nome_prodotto
		
class Stato_magazzino (models.Model):
	nome_prodotto = models.CharField(max_length=256)
	codiceprodotto = models.CharField(max_length=256,blank=True)
	prezzo_acquisto_no_iva = models.FloatField( blank=True, null=True)
	iva_percento=models.FloatField( blank=True, null=True)
	prezzo_vendita = models.FloatField( blank=True, null=True)
	colore=models.CharField(max_length=256)
	versione=models.CharField(max_length=256)
	quantita = models.FloatField( blank=True, null=True)
	descrizione = models.CharField(max_length=256,blank=True)
	note = models.TextField(blank=True)
	Quantita_residua=models.FloatField( blank=True, null=True)
	codice_campo_prodotto= models.CharField(max_length=256,blank=True)

class Inserimento_automezzi_aziendali (models.Model):
	nome_vettura = models.CharField(max_length=256)
	codicevettura = models.CharField(max_length=256,blank=True)
	targa = models.CharField(max_length=256,blank=True)
	telaio = models.CharField(max_length=256,blank=True)
	Proprietario = models.CharField(max_length=256,blank=True)
	locatore = models.CharField(max_length=256,blank=True, null=True)
	prezzo_acquisto = models.FloatField( blank=True, null=True)
	leasing=models.BooleanField()
	prezzo_leasing = models.FloatField( blank=True, null=True)
	prezzo_rata = models.FloatField( blank=True, null=True)
	colore=models.CharField(max_length=256)
	versione=models.CharField(max_length=256)
	Marca = models.CharField(max_length=256)
	data_acquisto = models.DateField(blank=True, null=True)
	data_vendita = models.DateField(blank=True, null=True)
	data_fine_pagamento = models.DateField(blank=True, null=True)
	quantita = models.FloatField( blank=True, null=True)
	descrizione = models.TextField(blank=True)
	note = models.TextField(blank=True)
	codice_applicazione_vettura= models.CharField(max_length=256,blank=True)
	file=models.FileField()

	def __str__(self):
		return self.nome_vettura


class Ingresso_uscita_automezzi (models.Model):
	codice_automezzo = models.ForeignKey('Inserimento_automezzi_aziendali', on_delete=models.CASCADE)
	dipendente_assegnato=models.ForeignKey('Dipendenti', on_delete=models.CASCADE, related_name='dipendente1')#il related_name serve per distinguere i due campi visto che si indirizzano a una stessa tabella
	piudipendenti=models.ForeignKey('Dipendenti', on_delete=models.CASCADE, null=True,related_name='dipendente2')
	data_uscita = models.DateField(blank=True, null=True)
	data_ingresso = models.DateField(blank=True, null=True)
	quantita = models.FloatField( blank=True, null=True)
	motivo = models.TextField(blank=True)
	note = models.TextField(blank=True)
	quante_ore=models.IntegerField( blank=True, null=True)
	def __str__(self):
		return self.codice_automezzo

class Inserimento_beni_azienda (models.Model):
	nome_bene = models.CharField(max_length=256)
	codicebene = models.CharField(max_length=256,blank=True)
	prezzo_acquisto_no_iva = models.FloatField( blank=True, null=True)
	iva_percento=models.FloatField( blank=True, null=True)
	prezzo_vendita = models.FloatField( blank=True, null=True)
	colore=models.CharField(max_length=256)
	versione=models.CharField(max_length=256)
	fornitori = models.ForeignKey('customer.Fornitori', on_delete=models.CASCADE)
	marca=models.CharField(max_length=256)
	data_acquisto = models.DateField(blank=True, null=True)
	data_vendita = models.DateField(blank=True, null=True)
	quantita = models.FloatField( blank=True, null=True)
	descrizione = models.CharField(max_length=256,blank=True)
	note = models.TextField(blank=True)
	codice_campo_prodotto= models.CharField(max_length=256,blank=True)
	file=models.FileField()

	def __str__(self):
		return self.nome_bene

class Inserimento_patrimonio_mobiliare (models.Model):
	nome_titolo = models.CharField(max_length=256)
	codice_titolo = models.CharField(max_length=256,blank=True)
	importo = models.FloatField( blank=True, null=True)
	sconto_titolo = models.FloatField( blank=True, null=True)
	istituto=models.CharField(max_length=256)
	tipo_titolo=models.CharField(max_length=256)
	data_emissione_apertura = models.DateField(blank=True, null=True)
	data_scadenza = models.DateField(blank=True, null=True)
	descrizione = models.CharField(max_length=256,blank=True)
	note = models.TextField(blank=True)
	codice_campo_prodotto=models.CharField(max_length=256,blank=True)
	file=models.FileField()

	def __str__(self):
		return self.nome_titolo

class Inserimento_patrimonio_immoboliare (models.Model):
	nome_bene = models.CharField(max_length=256)
	codice_titolo = models.CharField(max_length=256,blank=True)
	codice_catastale = models.CharField(max_length=256,blank=True)
	grandezza = models.FloatField( blank=True, null=True)
	Documento_possesso = models.CharField(max_length=256,blank=True)
	prezzo_acquisto=models.CharField(max_length=256,default=0.00)
	prezzo_vendita=models.CharField(max_length=256,default=0.00)
	rate=models.FloatField( blank=True, null=True)
	data_acquisto = models.DateField(blank=True, null=True)
	data_vendita = models.DateField(blank=True, null=True)
	descrizione = models.CharField(max_length=256,blank=True)
	note = models.TextField(blank=True)
	codice_aziendale_destinazione_uso=models.CharField(max_length=256,blank=True)
	Comune = models.CharField(max_length=256,blank=True)
	Prov = models.CharField(max_length=256,blank=True)
	Stato = models.CharField(max_length=256,blank=True)
	indirizzo = models.CharField(max_length=256,blank=True)
	particelle = models.CharField(max_length=256,blank=True)
	file=models.FileField()

	def __str__(self):
		return self.nome_bene


class Inserimento_debiti_patrimonio_azienda (models.Model):
	nome_titolo = models.CharField(max_length=256)
	codice_titolo = models.CharField(max_length=256,blank=True)
	importo = models.FloatField( blank=True, null=True)
	sconto_titolo = models.FloatField( blank=True, null=True)
	istituto=models.CharField(max_length=256)
	tipo_titolo=models.CharField(max_length=256)
	data_emissione_apertura = models.DateField(blank=True, null=True)
	data_scadenza = models.DateField(blank=True, null=True)
	descrizione = models.CharField(max_length=256,blank=True)
	note = models.TextField(blank=True)
	codice_campo_prodotto=models.CharField(max_length=256,blank=True)
	file=models.FileField()

	def __str__(self):
		return self.nome_titolo


class Dipendenti (models.Model):
	employees_id=models.IntegerField(unique=True)
	agevolazioni=models.BooleanField()
	motivo_agevolazioni=models.TextField(blank=True)
	nome_cognome = models.CharField(max_length=256, blank=True)
	codicefiscale = models.CharField(max_length=256,blank=True)
	piva = VATNumberField(max_length=256, blank=True)
	codiceunivoco_sdi = models.CharField(max_length=20, blank=True)
	pec = models.EmailField(blank=True, null=True)
	indirizzo_res = models.CharField(max_length=256,blank=True)
	comune_res = models.CharField(max_length=256,blank=True)
	cap_res = models.CharField(max_length=256,blank=True)
	prov_res = models.CharField(max_length=256,blank=True)
	indirizzo_domicilio = models.CharField(max_length=256, blank=True)
	comune_domicilio = models.CharField(max_length=256, blank=True)
	cap_domicilio = models.CharField(max_length=256, blank=True)
	prov_domicilio = models.CharField(max_length=256, blank=True)
	email = models.EmailField(blank=True, null=True)
	recapito_tel = PhoneNumberField(default='+39', blank=True, null=True)
	fax = PhoneNumberField(blank=True, default='+39', null=True)
	coordinate_gps = models.CharField(max_length=512, blank=True, null=True)
	metodo_pagamento = models.ForeignKey(metodopagamento, on_delete=models.CASCADE, blank=True, null=True,  related_name="tags") 
	codice_iban = IBANField(blank=True)
	note = models.TextField(blank=True)
	mansione = models.TextField(blank=True)
	titolo_studio = models.TextField(blank=True)
	tipo_contratto = models.CharField(max_length=256,blank=True)
	licenziamento_dimissioni = models.CharField(max_length=256,blank=True)
	motivo=models.TextField(blank=True)
	tempo_occupazione= models.TextField(blank=True)
	stipendio_contratto=models.FloatField( blank=True, null=True)
	bonus_mensile=models.CharField(max_length=256,blank=True)
	Bonus_annuale=models.CharField(max_length=256,blank=True)
	tipo_di_bonus=models.CharField(max_length=256,blank=True)
	fringe_benefit=models.CharField(max_length=256,blank=True)
	data_inizio_collaborazione=models.DateField(blank=True, null=True)
	data_fine_collaborazione=models.DateField(blank=True, null=True)
	file=models.FileField()

	def __str__(self):
		return self.nome_cognome

class Turni_dipendenti (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	turno = models.CharField(max_length=256,blank=True)
	ora_ingresso = models.DateField(blank=True, null=True)
	ora_uscita = models.DateField(blank=True, null=True)
	dateapplicazione_turno=models.DateField(blank=True, null=True)
	note = models.TextField(blank=True)

	def __str__(self):
		return self.dipendente.nome_cognome

class Ferie_dipendenti (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	inizio_ferie = models.DateField(blank=True, null=True)
	fine_ferie = models.DateField(blank=True, null=True)
	ferie_a_disposizione = models.FloatField( blank=True, null=True)

	def __str__(self):
		return self.dipendente.nome_cognome

class Dipendenti_trasferta_trasferiemnto (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	trasferta_trasferimento = models.CharField(max_length=256,blank=True)
	partenza = models.DateField(blank=True, null=True)
	rientro = models.DateField(blank=True, null=True)
	automezzo=models.ForeignKey('Inserimento_automezzi_aziendali', on_delete=models.CASCADE)
	costo_alloggio=models.FloatField( blank=True, null=True)
	costo_vitto = models.FloatField( blank=True, null=True)
	note = models.TextField(blank=True)
	file=models.FileField()

	def __str__(self):
		return self.dipendente.nome_cognome

class Infortuni_malattia_dipendenti (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	inizio_periodo = models.DateField(blank=True, null=True)
	fine_periodo = models.DateField(blank=True, null=True)
	giorni_infortunio_a_disposizione = models.FloatField( blank=True, null=True)
	giorni_malattia_a_disposizione = models.FloatField( blank=True, null=True)
	visita_medica=models.DateField(blank=True, null=True)
	rapporto_visita_medica=models.CharField(max_length=256)
	file=models.FileField()

	def __str__(self):
		return self.dipendente.nome_cognome

class Controversie_dipendenti (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	tipo_controversia = models.CharField(max_length=256,blank=True)
	motivo = models.TextField(blank=True)
	data_inizio=models.DateField(blank=True, null=True)
	appuntamenti_intermedi=models.DateField(blank=True, null=True)
	motivo_incontro_intermedio=models.TextField(blank=True)
	fine_controversia=models.DateField(blank=True, null=True)
	credito_dipendente=models.FloatField( blank=True, null=True)
	debito_dipendente=models.FloatField( blank=True, null=True)
	file=models.FileField()

	def __str__(self):
		return self.dipendente.nome_cognome

class Ingresso_uscita_dipendenti (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	orario_ingresso=models.DateField(blank=True, null=True)
	orario_uscita = models.DateField(blank=True, null=True)
	conteggio_ore = models.FloatField( blank=True, null=True)
	giorno_lavorato=models.DateField(blank=True, null=True)
	note = models.TextField(blank=True)

	def __str__(self):
		return self.dipendente.nome_cognome

class straordinari_dipendenti (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	orario_ingresso=models.DateField(blank=True, null=True)
	orario_uscita = models.DateField(blank=True, null=True)
	conteggio_ore_straordinario = models.FloatField( blank=True, null=True)
	giorno_lavorato=models.DateField(blank=True, null=True)
	note = models.TextField(blank=True)

	def __str__(self):
		return self.dipendente.nome_cognome

class sanzioni_dipendenti (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	multa=models.FloatField( blank=True, null=True)
	sanzione_verbale = models.TextField(blank=True)
	sanzione_scritta = models.TextField(blank=True)
	data_sanzione=models.DateField(blank=True, null=True)
	motivo=models.TextField(blank=True)
	note = models.TextField(blank=True)
	persona_constatato_sanzione=models.TextField(blank=True)

	def __str__(self):
		return self.dipendente.nome_cognome		


class Costo_beneficio_dipendenti (models.Model):
	dipendente = models.ForeignKey('Dipendenti', on_delete=models.CASCADE)
	stipendio_ogni_mese = models.FloatField( blank=True, null=True)
	benefit_ogni_mese = models.FloatField( blank=True, null=True)
	benefit_ogni_anno = models.FloatField( blank=True, null=True)
	spese_vitto_alloggio_mensile=models.FloatField( blank=True, null=True)
	spese_vitto_alloggio_annuale=models.FloatField( blank=True, null=True)
	motivo_vitto_alloggio=models.TextField(blank=True)
	rendita_monetaria_lavoro = models.FloatField( blank=True, null=True)
	rendita_da_lavoro_straordinario=models.FloatField( blank=True, null=True)
	ore_lavorate=models.FloatField( blank=True, null=True)
	ore_in_ferie=models.FloatField( blank=True, null=True)
	ore_malattia=models.FloatField( blank=True, null=True)
	ore_infortunio=models.FloatField( blank=True, null=True)
	anni_di_collaborazione=models.FloatField( blank=True, null=True)
	altre_rendite_lavoro=models.FloatField( blank=True, null=True)
	note = models.TextField(blank=True)
	def __str__(self):
		return self.dipendente.nome_cognome
		
class Fornitori (models.Model):
	supplier_id=models.IntegerField(unique=True)
	ragionesociale = models.CharField(max_length=256, blank=True)
	scelta_fattura = models.BooleanField(null=True)
	codicefiscale = models.CharField(max_length=256,blank=True)
	piva = VATNumberField(max_length=256, blank=True)
	codiceunivoco_sdi = models.CharField(max_length=20, blank=True)
	pec = models.EmailField(blank=True, null=True)
	indirizzo_sede = models.CharField(max_length=256,blank=True)
	comune_sede = models.CharField(max_length=256,blank=True)
	cap_sede = models.CharField(max_length=256,blank=True)
	prov_sede = models.CharField(max_length=256,blank=True)
	stato_sede = models.CharField(max_length=256,blank=True)
	indirizzo_sec = models.CharField(max_length=256, blank=True)
	comune_sec = models.CharField(max_length=256, blank=True)
	cap_sec = models.CharField(max_length=256, blank=True)
	prov_sec = models.CharField(max_length=256, blank=True)
	stato_sec = models.CharField(max_length=256,blank=True)
	email = models.EmailField(blank=True, null=True)
	recapito_tel = PhoneNumberField(default='+39', blank=True, null=True)
	fax = PhoneNumberField(blank=True, default='+39', null=True)
	coordinate_gps = models.CharField(max_length=512, blank=True, null=True)
	metodo_pagamento = models.ForeignKey(metodopagamento, on_delete=models.CASCADE, blank=True, null=True) 
	importo_ingresso = models.FloatField(blank=True, null=True)
	importo_cauzione_versata = models.FloatField(blank=True,null=True)
	codice_iban = IBANField(blank=True)
	spese_invio_bolletta = models.FloatField(blank=True,null=True)
	stato_fornitore=models.CharField(max_length=128, blank=True) 
	note = models.TextField(blank=True)
	data_inizio_collaborazione=models.DateField(blank=True, null=True)
	data_fine_collaborazione=models.DateField(blank=True, null=True)

	

	def __str__(self):
		return self.ragionesociale