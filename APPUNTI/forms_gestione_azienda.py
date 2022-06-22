from django import forms
from django.contrib.auth.models import Group
from django.forms import ModelForm, Media, MediaDefiningClass, Widget, TextInput, NumberInput,EmailInput, URLInput, PasswordInput, HiddenInput, MultipleHiddenInput, FileInput, ClearableFileInput, Textarea, DateInput, DateTimeInput, TimeInput, CheckboxInput, Select, NullBooleanSelect, SelectMultiple, RadioSelect, CheckboxSelectMultiple, MultiWidget, SplitDateTimeWidget, SplitHiddenDateTimeWidget, SelectDateWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from apps.customer.models import Customer,Fornitori
from apps.items.models import InvoiceItem, offertainternet, cadenzapagamento, metodopagamento, offertavoip
from apps.invoices.models import Invoice,Preventivo,Nota_di_credito, prodotti,prodottipreventivo
from apps.expenses.models import Expense
from localflavor.generic.forms import IBANFormField, BICFormField
from apps.azienda.models import Azienda,Dipendenti,Prodotti_magazzino,Stato_magazzino,Inserimento_automezzi_aziendali,Ingresso_uscita_automezzi,Inserimento_beni_azienda,Inserimento_patrimonio_mobiliare,Inserimento_patrimonio_immoboliare,Inserimento_debiti_patrimonio_azienda,Turni_dipendenti,Ferie_dipendenti,Dipendenti_trasferta_trasferiemnto,Infortuni_malattia_dipendenti,Controversie_dipendenti,Ingresso_uscita_dipendenti,straordinari_dipendenti,sanzioni_dipendenti,Costo_beneficio_dipendenti,
from django.forms import inlineformset_factory



class DateInput(DateInput):
	input_type = 'date'

class Fornitori_form(forms.ModelForm):
	class Meta:
		model = Fornitori
		fields=  '__all__'
		
		widgets={
			'supplier_id' : NumberInput(attrs={"class":"form-control","id":"supplier_id", 'placeholder':'supplier_id','required':'True'}),
			'ragionesociale' : TextInput(attrs={"class":"form-control","id":"ragionesociale",'placeholder':'ragione sociale','required':'True'}),
			'codicefiscale' : TextInput(attrs={"class":"form-control","id":"codicefiscale","placeholder":"codice fiscale",'required':'True'}),
			'piva' : TextInput(attrs={"class":"form-control","id":"piva","placehoder":"p.iva"}),
			'codiceunivoco_sdi' : TextInput(attrs={"class":"form-control","id":"codiceunivoco_sdi", "placeholder":"C.univoco fattura"}),
			'indirizzo_sede' : TextInput(attrs={"class":"form-control","id":"indirizzo_sede", 'placeholder':'indirizzo sede','required':'True'}),
			'comune_sede' : TextInput(attrs={"class":"form-control","id":"comune_sede",'placeholder':'comune sede','required':'True'}),
			'cap_sede' : TextInput(attrs={"class":"form-control","id":"cap_sede", 'placeholder':'cap sede','required':'True'}),
			'prov_sede' : TextInput(attrs={"class":"form-control","id":"prov_res", 'placeholder':'provincia sede','required':'True'}),
			'stato_sede' : TextInput(attrs={"class":"form-control","id":"stato_sede", 'placeholder':'stato sede','required':'True'}),
			'indirizzo_sec' : TextInput(attrs={"class":"form-control","id":"indirizzo_sec", 'placeholder':'indirizzo secondario','required':'True'}),
			'comune_sec' : TextInput(attrs={"class":"form-control","id":"comune_sec",'placeholder':'provincia secodnario','required':'True'}),
			'cap_sec' : TextInput(attrs={"class":"form-control","id":"cap_sec", 'placeholder':'cap secodnario','required':'True'}),
			'prov_sec' : TextInput(attrs={"class":"form-control","id":"prov_sec",'placeholder':'provincia secondario','required':'True'}),
			'stato_sec' : TextInput(attrs={"class":"form-control","id":"stato_sec", 'placeholder':'stato secondario','required':'True'}),
			'coordinate_gps' : TextInput(attrs={"class":"form-control","id":"coordinate_gps", 'placeholder':'coordinate gps'}),
			'importo_ingresso' : NumberInput(attrs={"class":"form-control","id":"importo_ingresso", 'placeholder':'importo ingresso','required':'True'}),
			'importo_cauzione_versata' : NumberInput(attrs={"class":"form-control","id":"importo_cauzione_versata", 'placeholder':'importo cauzione'}),
			'codice_iban' : TextInput(attrs={"class":"form-control","id":"codice_iban", 'placeholder':'Iban'}),
			'spese_invio_bolletta' : NumberInput(attrs={"class":"form-control","id":"spese_invio_bolletta",'placeholder':'Spese invio bollette'}),
			'stato_fornitore' : TextInput(attrs={"class":"form-control","id":"stato_fornitore", 'placeholder':'stato fornitore','required':'True', 'value':'attivo'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'recapito_tel': PhoneNumberPrefixWidget(attrs={'placeholder': 'Telefono', 'class': "form-control",'required':'True'}),
			'scelta_fattura' : CheckboxInput(attrs={"id":"scelta_fattura", "class":"form-control"}),
			'email' : EmailInput(attrs={"class":"form-control","id":"email",'placeholder':'email'}),
			'pec' : EmailInput(attrs={"class":"form-control","id":"pec",'placeholder':'pec'}),
			'fax' : PhoneNumberPrefixWidget(attrs={'placeholder': 'Fax', 'class': "form-control"}),
			'metodo_pagamento' : Select(attrs={"class":"custom-select","id":"metodo_pagamento",'required':'True'}),
			'data_inizio_collaborazione' : DateInput(attrs={"class":"date","id":"data_inizio_collaborazione", "required":"true"}),
			'data_fine_collaborazione': DateInput(attrs={"class":"date","id":"data_fine_collaborazione"}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}


class Dipendenti_form(forms.ModelForm):
	class Meta:
		model = Dipendenti
		fields=  '__all__'
		
		widgets={
			'employees_id' : NumberInput(attrs={"class":"form-control","id":"employees_id", 'placeholder':'employees id','required':'True'}),
			'motivo_agevolazioni' : TextInput(attrs={"class":"form-control","id":"motivo_agevolazioni",'placeholder':'motivo agevolazioni'}),
			'nome_cognome' : TextInput(attrs={"class":"form-control","id":"nome_cognome",'placeholder':'nome_cognome','required':'True'}),
			'codicefiscale' : TextInput(attrs={"class":"form-control","id":"codicefiscale","placeholder":"codice fiscale",'required':'True'}),
			'piva' : TextInput(attrs={"class":"form-control","id":"piva","placehoder":"p.iva"}),
			'codiceunivoco_sdi' : TextInput(attrs={"class":"form-control","id":"codiceunivoco_sdi", "placeholder":"C.univoco fattura"}),
			'indirizzo_res' : TextInput(attrs={"class":"form-control","id":"indirizzo_res", 'placeholder':'indirizzo di residenza','required':'True'}),
			'comune_res' : TextInput(attrs={"class":"form-control","id":"comune_res",'placeholder':'comune di residenza','required':'True'}),
			'cap_res' : TextInput(attrs={"class":"form-control","id":"cap_res", 'placeholder':'cap di residenza','required':'True'}),
			'prov_res' : TextInput(attrs={"class":"form-control","id":"prov_res", 'placeholder':'provincia di residenza','required':'True'}),
			'indirizzo_domicilio' : TextInput(attrs={"class":"form-control","id":"indirizzo_domicilio", 'placeholder':'indirizzo di domicilio','required':'True'}),
			'comune_domicilio' : TextInput(attrs={"class":"form-control","id":"comune_domicilio",'placeholder':'provincia di domicilio','required':'True'}),
			'cap_domicilio' : TextInput(attrs={"class":"form-control","id":"cap_domicilio", 'placeholder':'cap di domicilio','required':'True'}),
			'prov_domicilio' : TextInput(attrs={"class":"form-control","id":"prov_domicilio",'placeholder':'provincia di domicilio','required':'True'}),
			'coordinate_gps' : TextInput(attrs={"class":"form-control","id":"coordinate_gps", 'placeholder':'coordinate gps'}),
			'codice_iban' : TextInput(attrs={"class":"form-control","id":"codice_iban", 'placeholder':'Iban'}),
			'stipendio_contratto' : NumberInput(attrs={"class":"form-control","id":"sstipendio_contratto",'placeholder':'stipendio contratto'}),
			'mansione' : TextInput(attrs={"class":"form-control","id":"mansione", 'placeholder':'mansione','required':'True'}),
			'titolo_studio' : TextInput(attrs={"class":"form-control","id":"titolo_studio", 'placeholder':'titolo_studio','required':'True'}),
			'tipo_contratto' : TextInput(attrs={"class":"form-control","id":"tipo_contratto", 'placeholder':'tipo_contratto','required':'True'}),
			'tempo_occupazione' : TextInput(attrs={"class":"form-control","id":"tempo_occupazione",'placeholder':'tempo_occupazione'}),
			'bonus_mensile' : TextInput(attrs={"class":"form-control","id":"bonus_mensile",'placeholder':'bonus_mensile'}),
			'Bonus_annuale' : TextInput(attrs={"class":"form-control","id":"Bonus_annuale",'placeholder':'Bonus_annuale'}),
			'tipo_di_bonus' : TextInput(attrs={"class":"form-control","id":"tipo_di_bonus",'placeholder':'tipo_di_bonus'}),
			'fringe_benefit' : TextInput(attrs={"class":"form-control","id":"fringe_benefit",'placeholder':'fringe_benefit'}),
			'motivo' : Textarea(attrs={"class":"form-control","id":"motivo", 'placeholder':'motivo', 'rows':"2"}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'recapito_tel': PhoneNumberPrefixWidget(attrs={'placeholder': 'Telefono', 'class': "form-control",'required':'True'}),
			'agevolazioni' : CheckboxInput(attrs={"id":"agevolazioni", "class":"form-control"}),
			'email' : EmailInput(attrs={"class":"form-control","id":"email",'placeholder':'email'}),
			'pec' : EmailInput(attrs={"class":"form-control","id":"pec",'placeholder':'pec'}),
			'fax' : PhoneNumberPrefixWidget(attrs={'placeholder': 'Fax', 'class': "form-control"}),
			'metodo_pagamento' : Select(attrs={"class":"custom-select","id":"metodo_pagamento",'required':'True'}),
			'data_inizio_collaborazione' : DateInput(attrs={"class":"date","id":"data_inizio_collaborazione", "required":"true",'value': datetime.now().strftime("%d-%m-%Y")}),
			'data_fine_collaborazione' : DateInput(attrs={"class":"date","id":"data_fine_collaborazione"}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),

		
}





class aziendaForm(forms.ModelForm):
	class Meta:
		model = Azienda
		fields=  '__all__'
		
		widgets={
			'ragionesociale' : TextInput(attrs={"class":"form-control","id":"ragionesociale",'placeholder':'ragione sociale'}),
			'codicefiscale' : TextInput(attrs={"class":"form-control","id":"codicefiscale","placeholder":"codice fiscale"}),
			'piva' : TextInput(attrs={"class":"form-control","id":"piva","placehoder":"p.iva"}),
			'codiceunivoco_sdi' : TextInput(attrs={"class":"form-control","id":"codiceunivoco_sdi", "placeholder":"C.univoco fattura"}),
			'indirizzo_res' : TextInput(attrs={"class":"form-control","id":"indirizzo_res", 'placeholder':'indirizzo di residenza'}),
			'comune_res' : TextInput(attrs={"class":"form-control","id":"comune_res",'placeholder':'comune di residenza'}),
			'cap_res' : TextInput(attrs={"class":"form-control","id":"cap_res", 'placeholder':'cap di residenza'}),
			'prov_res' : TextInput(attrs={"class":"form-control","id":"prov_res", 'placeholder':'provincia di residenza'}),
			'codice_iban' : TextInput(attrs={"class":"form-control","id":"codice_iban", 'placeholder':'Iban'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'recapito_tel': PhoneNumberPrefixWidget(attrs={'placeholder': 'Telefono', 'class': "form-control"}),
			'email' : EmailInput(attrs={"class":"form-control","id":"email",'placeholder':'email'}),
			'pec' : EmailInput(attrs={"class":"form-control","id":"pec",'placeholder':'pec'}),
			'fax' : PhoneNumberPrefixWidget(attrs={'placeholder': 'Fax', 'class': "form-control"}),

		
}

class Inserimento_automezzi_aziendaliForm(forms.ModelForm):
	class Meta:
		model = Inserimento_automezzi_aziendali
		fields=  '__all__'
		
		widgets={
			'nome_vettura' : TextInput(attrs={"class":"form-control","id":"ragionesociale",'placeholder':'ragione sociale'}),
			'codicevettura' : TextInput(attrs={"class":"form-control","id":"codicefiscale","placeholder":"codice fiscale"}),
			'targa' : TextInput(attrs={"class":"form-control","id":"piva","placehoder":"p.iva"}),
			'telaio' : TextInput(attrs={"class":"form-control","id":"codiceunivoco_sdi", "placeholder":"C.univoco fattura"}),
			'Proprietario' : TextInput(attrs={"class":"form-control","id":"indirizzo_res", 'placeholder':'indirizzo di residenza'}),
			'locatore' : TextInput(attrs={"class":"form-control","id":"comune_res",'placeholder':'comune di residenza'}),
			'colore' : TextInput(attrs={"class":"form-control","id":"cap_res", 'placeholder':'cap di residenza'}),
			'versione' : TextInput(attrs={"class":"form-control","id":"prov_res", 'placeholder':'provincia di residenza'}),
			'Marca' : TextInput(attrs={"class":"form-control","id":"codice_iban", 'placeholder':'Iban'}),
			'codice_applicazione_vettura' : TextInput(attrs={"class":"form-control","id":"codice_iban", 'placeholder':'Iban'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'data_acquisto' : DateInput(attrs={"class":"date","id":"data_inizio_collaborazione", "required":"true"}),
			'data_vendita' : DateInput(attrs={"class":"date","id":"data_inizio_collaborazione", "required":"true"}),
			'data_fine_pagamento' : DateInput(attrs={"class":"date","id":"data_inizio_collaborazione", "required":"true"}),
			'prezzo_leasing' : NumberInput(attrs={"class":"form-control","id":"sstipendio_contratto",'placeholder':'stipendio contratto'}),
			'prezzo_rata' : NumberInput(attrs={"class":"form-control","id":"sstipendio_contratto",'placeholder':'stipendio contratto'}),
			'prezzo_acquisto' : NumberInput(attrs={"class":"form-control","id":"sstipendio_contratto",'placeholder':'stipendio contratto'}),
			'quantita' : NumberInput(attrs={"class":"form-control","id":"sstipendio_contratto",'placeholder':'stipendio contratto'}),
			'leasing' : CheckboxInput(attrs={"id":"agevolazioni", "class":"form-control"}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}


class Ingresso_uscita_automezziForm(forms.ModelForm):
	class Meta:
		model = Ingresso_uscita_automezzi
		fields=  '__all__'
		
		widgets={
			'dipendente_assegnato' : Select(attrs={"class":"custom-select","id":"dipendente_assegnato",'required':'True'}),
			'piudipendenti' : Select(attrs={"class":"custom-select","id":"piudipendenti"}),
			'codice_automezzo' : Select(attrs={"class":"custom-select","id":"codice_automezzo",'required':'True'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'motivo' : Textarea(attrs={"class":"form-control","id":"Motivazione", 'placeholder':'Motivazione uscita', 'rows':"2",'required':'True'}),
			'data_uscita' : DateInput(attrs={"class":"date","id":"data_uscita", "required":"true"}),
			'data_ingresso' : DateInput(attrs={"class":"date","id":"data_ingresso", "required":"true"}),
			'quantita' : NumberInput(attrs={"class":"form-control","id":"quantita",'placeholder':'quantita'}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}






class Prodotti_magazzinoForm(forms.ModelForm):
	class Meta:
		model = Prodotti_magazzino
		fields=  '__all__'
		
		widgets={
			'fornitori' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'nome_prodotto' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'codiceprodotto' : TextInput(attrs={"class":"form-control","id":"codiceprodotto","placeholder":"codice prodotto"}),
			'codice_campo_prodotto' : TextInput(attrs={"class":"form-control","id":"codice_campo_prodotto","placehoder":"codice campo prodotto"}),
			'colore' : TextInput(attrs={"class":"form-control","id":"colore", 'placeholder':'colore'}),
			'versione' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'Marca' : TextInput(attrs={"class":"form-control","id":"Marca", 'placeholder':'Marca'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"descrizione", 'placeholder':'descrizione', 'rows':"2"}),
			'data_acquisto' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'prezzo_acquisto_no_iva' : NumberInput(attrs={"class":"form-control","id":"prezzo_acquisto_no_iva",'placeholder':'Prezzo acquisto senza IVA'}),
			'iva_percento' : NumberInput(attrs={"class":"form-control","id":"IVA",'placeholder':'Iva'}),
			'prezzo_vendita' : NumberInput(attrs={"class":"form-control","id":"Prezzo_vendita",'placeholder':'prezzo vendita'}),
			'quantita' : NumberInput(attrs={"class":"form-control","id":"quantita",'placeholder':'quantita'}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}

class Stato_magazzinoForm(forms.ModelForm):
	class Meta:
		model = Stato_magazzino
		fields=  '__all__'
		
		widgets={
			'nome_prodotto' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'codiceprodotto' : TextInput(attrs={"class":"form-control","id":"codiceprodotto","placeholder":"codice prodotto"}),
			'codice_campo_prodotto' : TextInput(attrs={"class":"form-control","id":"codice_campo_prodotto","placehoder":"codice campo prodotto"}),
			'colore' : TextInput(attrs={"class":"form-control","id":"colore", 'placeholder':'colore'}),
			'versione' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'Marca' : TextInput(attrs={"class":"form-control","id":"Marca", 'placeholder':'Marca'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"descrizione", 'placeholder':'descrizione', 'rows':"2"}),
			'data_acquisto' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'prezzo_acquisto_no_iva' : NumberInput(attrs={"class":"form-control","id":"prezzo_acquisto_no_iva",'placeholder':'Prezzo acquisto senza IVA'}),
			'iva_percento' : NumberInput(attrs={"class":"form-control","id":"IVA",'placeholder':'Iva'}),
			'prezzo_vendita' : NumberInput(attrs={"class":"form-control","id":"Prezzo_vendita",'placeholder':'prezzo vendita'}),
			'Quantita_residua' : NumberInput(attrs={"class":"form-control","id":"Quantita_residua"}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}





class Inserimento_beni_aziendaForm(forms.ModelForm):
	class Meta:
		model = Inserimento_beni_azienda
		fields=  '__all__'
		
		widgets={
			'fornitori' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'nome_bene' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'codicebene' : TextInput(attrs={"class":"form-control","id":"codiceprodotto","placeholder":"codice prodotto"}),
			'codice_campo_prodotto' : TextInput(attrs={"class":"form-control","id":"codice_campo_prodotto","placehoder":"codice campo prodotto"}),
			'colore' : TextInput(attrs={"class":"form-control","id":"colore", 'placeholder':'colore'}),
			'versione' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'marca' : TextInput(attrs={"class":"form-control","id":"Marca", 'placeholder':'Marca'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"descrizione", 'placeholder':'descrizione', 'rows':"2"}),
			'data_acquisto' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'data_vendita' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'prezzo_acquisto_no_iva' : NumberInput(attrs={"class":"form-control","id":"prezzo_acquisto_no_iva",'placeholder':'Prezzo acquisto senza IVA'}),
			'iva_percento' : NumberInput(attrs={"class":"form-control","id":"IVA",'placeholder':'Iva'}),
			'prezzo_vendita' : NumberInput(attrs={"class":"form-control","id":"Prezzo_vendita",'placeholder':'prezzo vendita'}),
			'quantita' : NumberInput(attrs={"class":"form-control","id":"quantita",'placeholder':'quantita'}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}





class Inserimento_patrimonio_mobiliareForm(forms.ModelForm):
	class Meta:
		model = Inserimento_patrimonio_mobiliare
		fields=  '__all__'
		
		widgets={
			'nome_titolo' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'codice_titolo' : TextInput(attrs={"class":"form-control","id":"codiceprodotto","placeholder":"codice prodotto"}),
			'codice_campo_prodotto' : TextInput(attrs={"class":"form-control","id":"codice_campo_prodotto","placehoder":"codice campo prodotto"}),
			'istituto' : TextInput(attrs={"class":"form-control","id":"colore", 'placeholder':'colore'}),
			'tipo_titolo' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"descrizione", 'placeholder':'descrizione', 'rows':"2"}),
			'data_emissione' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'data_scadenza' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'importo' : NumberInput(attrs={"class":"form-control","id":"prezzo_acquisto_no_iva",'placeholder':'Prezzo acquisto senza IVA'}),
			'sconto_titolo' : NumberInput(attrs={"class":"form-control","id":"IVA",'placeholder':'Iva'}),
			'prezzo_vendita' : NumberInput(attrs={"class":"form-control","id":"Prezzo_vendita",'placeholder':'prezzo vendita'}),
			'quantita' : NumberInput(attrs={"class":"form-control","id":"quantita",'placeholder':'quantita'}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}




class Inserimento_patrimonio_immoboliareForm(forms.ModelForm):
	class Meta:
		model = Inserimento_patrimonio_immoboliare
		fields=  '__all__'
		
		widgets={
			'nome_bene' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'codice_titolo' : TextInput(attrs={"class":"form-control","id":"codiceprodotto","placeholder":"codice prodotto"}),
			'codice_catastale ' : TextInput(attrs={"class":"form-control","id":"codice_campo_prodotto","placehoder":"codice campo prodotto"}),
			'Documento_possesso' : TextInput(attrs={"class":"form-control","id":"colore", 'placeholder':'colore'}),
			'codice_aziendale_destinazione_uso' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'Comune' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'Prov' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'Stato' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'indirizzo' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'particelle' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"descrizione", 'placeholder':'descrizione', 'rows':"2"}),
			'data_acquisto' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'data_vendita' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'grandezza' : NumberInput(attrs={"class":"form-control","id":"prezzo_acquisto_no_iva",'placeholder':'Prezzo acquisto senza IVA'}),
			'prezzo_acquisto' : NumberInput(attrs={"class":"form-control","id":"IVA",'placeholder':'Iva'}),
			'prezzo_vendita' : NumberInput(attrs={"class":"form-control","id":"IVA",'placeholder':'Iva'}),
			'rate' : NumberInput(attrs={"class":"form-control","id":"IVA",'placeholder':'Iva'}),
			'prezzo_vendita' : NumberInput(attrs={"class":"form-control","id":"Prezzo_vendita",'placeholder':'prezzo vendita'}),
			'quantita' : NumberInput(attrs={"class":"form-control","id":"quantita",'placeholder':'quantita'}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}



class Inserimento_debiti_patrimonio_aziendaForm(forms.ModelForm):
	class Meta:
		model = Inserimento_debiti_patrimonio_azienda
		fields=  '__all__'
		
		widgets={
			'nome_titolo' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'codice_titolo' : TextInput(attrs={"class":"form-control","id":"codiceprodotto","placeholder":"codice prodotto"}),
			'codice_campo_prodotto' : TextInput(attrs={"class":"form-control","id":"codice_campo_prodotto","placehoder":"codice campo prodotto"}),
			'istituto' : TextInput(attrs={"class":"form-control","id":"colore", 'placeholder':'colore'}),
			'tipo_titolo' : TextInput(attrs={"class":"form-control","id":"versione", 'placeholder':'versione'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"descrizione", 'placeholder':'descrizione', 'rows':"2"}),
			'data_emissione' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'data_scadenza' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'importo' : NumberInput(attrs={"class":"form-control","id":"prezzo_acquisto_no_iva",'placeholder':'Prezzo acquisto senza IVA'}),
			'sconto_titolo' : NumberInput(attrs={"class":"form-control","id":"IVA",'placeholder':'Iva'}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}


class Turni_dipendentiForm(forms.ModelForm):
	class Meta:
		model = Turni_dipendenti
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'turno' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'dateapplicazione_turno' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'ora_ingresso' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'ora_uscita' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
}

class Ferie_dipendentiForm(forms.ModelForm):
	class Meta:
		model = Ferie_dipendenti
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'inizio_ferie' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'fine_ferie' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'ferie_a_disposizione' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
}




class Dipendenti_trasferta_trasferiemntoForm(forms.ModelForm):
	class Meta:
		model = Dipendenti_trasferta_trasferiemnto
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'automezzo' : Select(attrs={"class":"custom-select","id":"fornitori"}),
			'trasferta_trasferimento' : TextInput(attrs={"class":"form-control","id":"trasferta_trasferimento",'placeholder':'nome_prodotto'}),
			'partenza' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'rientro' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'costo_alloggio' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'costo_vitto' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),

}



class Infortuni_malattia_dipendentiForm(forms.ModelForm):
	class Meta:
		model = Infortuni_malattia_dipendenti
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'turno' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'inizio_periodo' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'fine_periodo' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'visita_medica' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'rapporto_visita_medica' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'giorni_infortunio_a_disposizione' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'giorni_malattia_a_disposizione' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}


class Controversie_dipendentiForm(forms.ModelForm):
	class Meta:
		model = Controversie_dipendenti
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'tipo_controversia' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'motivo' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'data_inizio' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'appuntamenti_intermedi' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'motivo_incontro_intermedio' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'fine_controversia' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'credito_dipendente' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'debito_dipendente' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'file':FileInput(attrs={"rows": "", "class": "form-control file_upload", 'id':'carica_file'}),
}


class Ingresso_uscita_dipendentiForm(forms.ModelForm):
	class Meta:
		model = Ingresso_uscita_dipendenti
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'orario_ingresso' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'orario_uscita' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'giorno_lavorato' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'rapporto_visita_medica' : TextInput(attrs={"class":"form-control","id":"nome_prodotto",'placeholder':'nome_prodotto'}),
			'conteggio_ore' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
}

class straordinari_dipendentiForm(forms.ModelForm):
	class Meta:
		model = straordinari_dipendenti
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'orario_ingresso' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'orario_uscita' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'giorno_lavorato' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'conteggio_ore_straordinario' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
}

class sanzioni_dipendentiForm(forms.ModelForm):
	class Meta:
		model = sanzioni_dipendenti
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'data_sanzione' : DateInput(attrs={"class":"date","id":"data_acquisto", "required":"true"}),
			'multa' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'motivo' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'sanzione_verbale' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'sanzione_scritta' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'persona_constatato_sanzione' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
}


class Costo_beneficio_dipendentiForm(forms.ModelForm):
	class Meta:
		model = Costo_beneficio_dipendenti
		fields=  '__all__'
		
		widgets={
			'dipendente' : Select(attrs={"class":"custom-select","id":"fornitori",'required':'True'}),
			'stipendio_ogni_mese' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'benefit_ogni_mese' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'benefit_ogni_anno' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'spese_vitto_alloggio_mensile' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'spese_vitto_alloggio_annuale' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'rendita_monetaria_lavoro' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'rendita_da_lavoro_straordinario' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'ore_lavorate' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'ore_in_ferie' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'ore_malattia' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'ore_infortunio' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'anni_di_collaborazione' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'altre_rendite_lavoro' : NumberInput(attrs={"class":"form-control","id":"ferie_a_disposizione",'placeholder':'Iva'}),
			'motivo_vitto_alloggio' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
}

