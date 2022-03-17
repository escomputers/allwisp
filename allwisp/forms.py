from django import forms
from django.contrib.auth.models import Group
from django.forms import ModelForm, Media, MediaDefiningClass, Widget, TextInput, NumberInput,EmailInput, URLInput, PasswordInput, HiddenInput, MultipleHiddenInput, FileInput, ClearableFileInput, Textarea, DateInput, DateTimeInput, TimeInput, CheckboxInput, Select, NullBooleanSelect, SelectMultiple, RadioSelect, CheckboxSelectMultiple, MultiWidget, SplitDateTimeWidget, SplitHiddenDateTimeWidget, SelectDateWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from apps.customer.models import Customer
from apps.items.models import InvoiceItem, offertainternet, cadenzapagamento, metodopagamento, offertavoip
from apps.invoices.models import Invoice,Preventivo,Nota_di_credito
from apps.expenses.models import Expense
from localflavor.generic.forms import IBANFormField, BICFormField
from apps.azienda.models import Azienda

# per il formset
class prodottiFatturaForm(forms.ModelForm):
	class Meta:
		model= Invoice
		exclude=['invoice_id','customer','date','status','documento']
		
		widgets={
		'qta' : NumberInput(attrs={"class":"form-control fattura-qta","id":"qta", 'placeholder':'quantità','required':'True'}),
		'prodotto' : TextInput(attrs={"class":"form-control fattura-prodotto","id":"prodotto", 'placeholder':'prodotto','required':'True'}),
		'descrizione' : TextInput(attrs={"class":"form-control fattura-descrizione","id":"descrizione", 'placeholder':'descrizione','required':'True'}),
		'prezzo' : NumberInput(attrs={"class":"form-control fattura-prezzo","id":"prezzo", 'placeholder':'prezzo','required':'True'}),
		'prezzo_subtot' : NumberInput(attrs={"class":"form-control fattura-prezzo_subtot","id":"prezzo_subtot", 'placeholder':'Sub totale','disabled':'True'}),
		'tax' : NumberInput(attrs={"class":"form-control fattura-tax","id":"tax", 'placeholder':'Tasse','required':'True'}),
		'total' : NumberInput(attrs={"class":"form-control fattura-total","id":"total", 'placeholder':'Totale','disabled':'True'}),
		}


class prodotti_preventivoForm(forms.ModelForm):
	class Meta:
		model= Preventivo
		exclude=['invoice_id','customer','date','status','documento']
		
		widgets={
		'qta' : NumberInput(attrs={"class":"form-control preventivo-qta","id":"qta", 'placeholder':'quantità','required':'True'}),
		'prodotto' : TextInput(attrs={"class":"form-control preventivo-prodotto","id":"prodotto", 'placeholder':'prodotto','required':'True'}),
		'descrizione' : TextInput(attrs={"class":"form-control preventivo-descrizione","id":"descrizione", 'placeholder':'descrizione','required':'True'}),
		'prezzo' : NumberInput(attrs={"class":"form-control preventivo-prezzo","id":"prezzo", 'placeholder':'prezzo','required':'True'}),
		'prezzo_subtot' : NumberInput(attrs={"class":"form-control preventivo-prezzo_subtot","id":"prezzo_subtot", 'placeholder':'Sub totale','disabled':'True'}),
		'tax' : NumberInput(attrs={"class":"form-control preventivo-tax","id":"tax", 'placeholder':'Tasse','required':'True'}),
		'total' : NumberInput(attrs={"class":"form-control preventivo-prezzo_total","id":"total", 'placeholder':'Totale','disabled':'True'}),
		}


class nota_di_creditoForm(forms.ModelForm):
	class Meta:
		model= Nota_di_credito
		fields='__all__'
		
		widgets={
		'qta' : NumberInput(attrs={"class":"form-control notadicredito-qta","id":"qta", 'placeholder':'quantità'}),
		'prodotto' : TextInput(attrs={"class":"form-control notadicredito-prodotto","id":"prodotto", 'placeholder':'prodotto'}),
		'descrizione' : TextInput(attrs={"class":"form-control notadicredito-descrizione","id":"descrizione", 'placeholder':'descrizione'}),
		'prezzo' : NumberInput(attrs={"class":"form-control notadicredito-prezzo","id":"prezzo", 'placeholder':'prezzo'}),
		'prezzo_subtot' : NumberInput(attrs={"class":"form-control notadicredito-prezzo_subtot","id":"prezzo_subtot", 'placeholder':'Sub totale','disabled':'True'}),
		'tax' : NumberInput(attrs={"class":"form-control notadicredito-tax","id":"tax", 'placeholder':'Tasse'}),
		'total' : NumberInput(attrs={"class":"form-control notadicredito-total","id":"total", 'placeholder':'Totale','disabled':'True'}),
		}







class DateInput(DateInput):
	input_type = 'date'

class clientiForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields=  '__all__'
		
		widgets={
			'customer_id' : NumberInput(attrs={"class":"form-control","id":"customer_id", 'placeholder':'Customer id','required':'True'}),
			'stato_cliente_dato' : TextInput(attrs={"class":"form-control","id":"stato_cliente_dato","hidden":"True"}),
			'ragionesociale' : TextInput(attrs={"class":"form-control","id":"ragionesociale",'placeholder':'ragione sociale','required':'True'}),
			'codicefiscale' : TextInput(attrs={"class":"form-control","id":"codicefiscale","placeholder":"codice fiscale",'required':'True'}),
			'piva' : TextInput(attrs={"class":"form-control","id":"piva","placehoder":"p.iva"}),
			'codiceunivoco_sdi' : TextInput(attrs={"class":"form-control","id":"codiceunivoco_sdi", "placeholder":"C.univoco fattura"}),
			'indirizzo_res' : TextInput(attrs={"class":"form-control","id":"indirizzo_res", 'placeholder':'indirizzo di residenza','required':'True'}),
			'comune_res' : TextInput(attrs={"class":"form-control","id":"comune_res",'placeholder':'comune di residenza','required':'True'}),
			'cap_res' : TextInput(attrs={"class":"form-control","id":"cap_res", 'placeholder':'cap di residenza','required':'True'}),
			'prov_res' : TextInput(attrs={"class":"form-control","id":"prov_res", 'placeholder':'provincia di residenza','required':'True'}),
			'indirizzo_inst' : TextInput(attrs={"class":"form-control","id":"indirizzo_inst", 'placeholder':'indirizzo di installazione','required':'True'}),
			'comune_inst' : TextInput(attrs={"class":"form-control","id":"comune_inst",'placeholder':'provincia di installazione','required':'True'}),
			'cap_inst' : TextInput(attrs={"class":"form-control","id":"cap_inst", 'placeholder':'cap di installazione','required':'True'}),
			'prov_inst' : TextInput(attrs={"class":"form-control","id":"prov_inst",'placeholder':'provincia di installazione','required':'True'}),
			'coordinate_gps' : TextInput(attrs={"class":"form-control","id":"coordinate_gps", 'placeholder':'coordinate gps'}),
			'importo_attivazione' : NumberInput(attrs={"class":"form-control","id":"importo_attivazione", 'placeholder':'importo attivazione','required':'True'}),
			'importo_offerta_dedicata' : NumberInput(attrs={"class":"form-control","id":"importo_offerta_dedicata", 'placeholder':'Importo offerta dedicata'}),
			'codice_iban' : TextInput(attrs={"class":"form-control","id":"codice_iban", 'placeholder':'Iban'}),
			'spese_invio_bolletta' : NumberInput(attrs={"class":"form-control","id":"spese_invio_bolletta",'placeholder':'Spese invio bollette'}),
			'nodo' : TextInput(attrs={"class":"form-control","id":"nodo", 'placeholder':'Nodo','required':'True'}),
			'mac_adress' : TextInput(attrs={"class":"form-control","id":"mac_adress", 'placeholder':'Mac address','required':'True'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'recapito_tel': PhoneNumberPrefixWidget(attrs={'placeholder': 'Telefono', 'class': "form-control",'required':'True'}),
			'scelta_fattura' : CheckboxInput(attrs={"id":"scelta_fattura", "class":"form-control"}),
			'email' : EmailInput(attrs={"class":"form-control","id":"email",'placeholder':'email'}),
			'pec' : EmailInput(attrs={"class":"form-control","id":"pec",'placeholder':'pec'}),
			'fax' : PhoneNumberPrefixWidget(attrs={'placeholder': 'Fax', 'class': "form-control"}),
			'offerta_voip' : Select(attrs={"class":"custom-select md-form","id":"offerta_voip"}),
			'numero_voip' : PhoneNumberPrefixWidget(attrs={'placeholder': 'Numero Voip', 'class': "form-control"}),
			'ip_statico' : TextInput(attrs={"class":"form-control","id":"ip_statico",'placeholder':'Ip statico'}),
			'offerta_internet' : Select(attrs={"class":"custom-select md-form","id":"offerta_internet", 'placeholder':'Offerta internet','required':'True'}),
			'cadenza_pagamento' : Select(attrs={"class":"custom-select md-form","id":"cadenza_pagamento", "class":"form-control"}),
			'metodo_pagamento' : Select(attrs={"class":"custom-select","id":"metodo_pagamento",'required':'True'}),
			'data_installazione' : DateInput(attrs={"class":"date","id":"data_installazione", "required":"true"}),
			'data_inizio_contratto' : DateInput(attrs={"class":"date","id":"data_inizio_contratto"}),
			'data_fine_contratto': DateInput(attrs={"class":"date","id":"data_fine_contratto", 'readonly':'true'}),
			'data_contattato': DateInput(attrs={"class":"date","id":"data_contattato"}),
			'data_contattare_stabilito_cliente': DateInput(),
			'data_da_contattare': DateInput(attrs={"class":"date","id":"data_contattato", 'readonly':'true'})

		
}

class offertainternetForm(forms.ModelForm):
	class Meta:
		model = offertainternet
		fields= '__all__'
		
		widgets={
			'nomeofferta' : TextInput(attrs={"class":"form-control","id":"nomeofferta",'placeholder':'nome offerta'}),
			'prezzo' : TextInput(attrs={"class":"form-control","id":"prezzo",'placeholder':'prezzo'}),
			'iva' : TextInput(attrs={"class":"form-control","id":"iva",'placeholder':'iva'}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"descrizione",'placeholder':'descrizione', 'rows':"1"}),
			'totaleivato' : HiddenInput(attrs={"class":"form-control","id":"totaleivato",'placeholder':'totaleivato'}),
		}

class offertavoipForm(forms.ModelForm):
	class Meta:
		model = offertavoip
		fields= '__all__'
		
		widgets={
			'nomeofferta' : TextInput(attrs={"class":"form-control","id":"nomeofferta",'placeholder':'nome offerta'}),
			'prezzo' : TextInput(attrs={"class":"form-control","id":"prezzo",'placeholder':'prezzo'}),
			'iva' : TextInput(attrs={"class":"form-control","id":"iva",'placeholder':'iva'}),
			'descrizione' : Textarea(attrs={"class":"form-control","id":"descrizione",'placeholder':'descrizione', 'rows':"1"}),
			'totaleivato' : HiddenInput(attrs={"class":"form-control","id":"totaleivato",'placeholder':'totaleivato'}),
		}

class cadenzapagamentoform(forms.ModelForm):
	class Meta:
		model = cadenzapagamento
		fields= '__all__'
		
		widgets={
			'nome_mese':TextInput(attrs={"class":"form-control","id":"nome_mese",'placeholder':'inserisci il nome del periodo mensile'}),
			'periodi' : TextInput(attrs={"class":"form-control","id":"periodi",'placeholder':'periodo pagamento'}),
			'numero_mese' : TextInput(attrs={"class":"form-control","id":"numero_mese",'placeholder':'mesi in numeri'}),
			
		}

class metodopagamento(forms.ModelForm):
	class Meta:
		model = metodopagamento
		fields= '__all__'
		
		widgets={
		
			'metodo' : TextInput(attrs={"class":"form-control","id":"metodo_pagamento",'placeholder':'metodo di pagamento'}),
			
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


class interessatiForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields=  ('data_contattato','customer_id', 'data_contattare_stabilito_cliente', 'data_da_contattare','ragionesociale','codicefiscale','piva','codiceunivoco_sdi', 'indirizzo_res','comune_res', 'cap_res','prov_res','indirizzo_inst', 'comune_inst','prov_inst','cap_inst','email','pec','recapito_tel', 'fax', 'note', 'coordinate_gps',)
		widgets={
			'customer_id' : NumberInput(attrs={"class":"form-control","id":"customer_id1", 'placeholder':'Customer id', 'required':'True'}),
			'ragionesociale' : TextInput(attrs={"class":"form-control","id":"ragionesociale1",'placeholder':'ragione sociale', 'required':'True'}),
			'codicefiscale' : TextInput(attrs={"class":"form-control","id":"codicefiscale2","placeholder":"codice fiscale", 'required':'True'}),
			'piva' : TextInput(attrs={"class":"form-control","id":"piva1","placehoder":"p.iva"}),
			'codiceunivoco_sdi' : TextInput(attrs={"class":"form-control","id":"codiceunivoco_sdi1", "placeholder":"C.univoco fattura"}),
			'indirizzo_res' : TextInput(attrs={"class":"form-control","id":"indirizzo_res1", 'placeholder':'indirizzo di residenza','required':'True'}),
			'comune_res' : TextInput(attrs={"class":"form-control","id":"comune_res1",'placeholder':'comune di residenza','required':'True'}),
			'cap_res' : TextInput(attrs={"class":"form-control","id":"cap_res1", 'placeholder':'cap di residenza','required':'True'}),
			'prov_res' : TextInput(attrs={"class":"form-control","id":"prov_res1", 'placeholder':'provincia di residenza','required':'True'}),
			'indirizzo_inst' : TextInput(attrs={"class":"form-control","id":"indirizzo_inst1", 'placeholder':'indirizzo di installazione','required':'True'}),
			'comune_inst' : TextInput(attrs={"class":"form-control","id":"comune_inst1",'placeholder':'provincia di installazione','required':'True'}),
			'cap_inst' : TextInput(attrs={"class":"form-control","id":"cap_inst1", 'placeholder':'cap di installazione','required':'True'}),
			'prov_inst' : TextInput(attrs={"class":"form-control","id":"prov_inst1",'placeholder':'provincia di installazione','required':'True'}),
			'coordinate_gps' : TextInput(attrs={"class":"form-control","id":"coordinate_gps1", 'placeholder':'coordinate gps','required':'True'}),
			'codice_iban' : TextInput(attrs={"class":"form-control","id":"codice_iban1", 'placeholder':'Iban'}),
			'nodo' : TextInput(attrs={"class":"form-control","id":"nodo1", 'placeholder':'Nodo'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note1", 'placeholder':'inserisci note', 'rows':"2"}),
			'recapito_tel': PhoneNumberPrefixWidget(attrs={'placeholder': 'Telefono', 'class': "form-control",'required':'True'}),
			'email' : EmailInput(attrs={"class":"form-control","id":"email1",'placeholder':'email'}),
			'pec' : EmailInput(attrs={"class":"form-control","id":"pec1",'placeholder':'pec'}),
			'fax' : PhoneNumberPrefixWidget(attrs={'placeholder': 'Fax', 'class': "form-control"}),
			'data_contattato': DateInput(attrs={"class":"date","id":"data_contattato",'required':'True'}),
			'data_contattare_stabilito_cliente': DateInput(),
			'data_da_contattare': DateInput(attrs={"class":"date","id":"data_contattato", 'readonly':'true'})

		
}
