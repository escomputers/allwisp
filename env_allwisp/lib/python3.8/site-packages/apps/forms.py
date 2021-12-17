from django import forms 
from django.contrib.auth.models import Group
from django.forms import ModelForm, Media, MediaDefiningClass, Widget, TextInput, NumberInput,EmailInput, URLInput, PasswordInput, HiddenInput, MultipleHiddenInput, FileInput, ClearableFileInput, Textarea, DateInput, DateTimeInput, TimeInput, CheckboxInput, Select, NullBooleanSelect, SelectMultiple, RadioSelect, CheckboxSelectMultiple, MultiWidget, SplitDateTimeWidget, SplitHiddenDateTimeWidget, SelectDateWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .customer.models import Customer, statocliente
from .items.models import InvoiceItem, offertainternet, cadenzapagamento, metodopagamento, offertavoip
from .invoices.models import Invoice
from .expenses.models import Expense
from .attachment.models import InvoiceAttachment, ExpenseAttachment



class clientiForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields=  '__all__'
		
		widgets={
			'stato_cliente' : Select(attrs={"class":"custom-select md-form","id":"stato_cliente"}),
			'customer_id' : NumberInput(attrs={"class":"form-control","id":"customer_id", 'placeholder':'Customer id'}),
			'ragionesociale' : TextInput(attrs={"class":"form-control","id":"ragionesociale",'placeholder':'ragione sociale'}),
			'codicefiscale' : TextInput(attrs={"class":"form-control","id":"codicefiscale","placeholder":"codice fiscale"}),
			'piva' : TextInput(attrs={"class":"form-control","id":"piva","placehoder":"p.iva"}),
			'codiceunivoco_sdi' : TextInput(attrs={"class":"form-control","id":"codiceunivoco_sdi", "placeholder":"C.univoco fattura"}),
			'indirizzo_res' : TextInput(attrs={"class":"form-control","id":"indirizzo_res", 'placeholder':'indirizzo di residenza'}),
			'comune_res' : TextInput(attrs={"class":"form-control","id":"comune_res",'placeholder':'comune di residenza'}),
			'cap_res' : TextInput(attrs={"class":"form-control","id":"cap_res", 'placeholder':'cap di residenza'}),
			'prov_res' : TextInput(attrs={"class":"form-control","id":"prov_res", 'placeholder':'provincia di residenza'}),
			'indirizzo_inst' : TextInput(attrs={"class":"form-control","id":"indirizzo_inst", 'placeholder':'indirizzo di installazione'}),
			'comune_inst' : TextInput(attrs={"class":"form-control","id":"comune_inst",'placeholder':'provincia di installazione'}),
			'cap_inst' : TextInput(attrs={"class":"form-control","id":"cap_inst", 'placeholder':'cap di installazione'}),
			'prov_inst' : TextInput(attrs={"class":"form-control","id":"prov_inst",'placeholder':'provincia di installazione'}),
			'coordinate_gps' : TextInput(attrs={"class":"form-control","id":"coordinate_gps", 'placeholder':'coordinate gps'}),
			'importo_attivazione' : NumberInput(attrs={"class":"form-control","id":"importo_attivazione", 'placeholder':'importo attivazione'}),
			'importo_offerta_dedicata' : NumberInput(attrs={"class":"form-control","id":"importo_offerta_dedicata", 'placeholder':'Importo offerta dedicata'}),
			'codice_iban' : TextInput(attrs={"class":"form-control","id":"codice_iban", 'placeholder':'Iban'}),
			'spese_invio_bolletta' : NumberInput(attrs={"class":"form-control","id":"spese_invio_bolletta",'placeholder':'Spese invio bollette'}),
			'nodo' : TextInput(attrs={"class":"form-control","id":"nodo", 'placeholder':'Nodo'}),
			'mac_adress' : TextInput(attrs={"class":"form-control","id":"mac_adress", 'placeholder':'Mac address'}),
			'note' : Textarea(attrs={"class":"form-control","id":"note", 'placeholder':'inserisci note', 'rows':"2"}),
			'recapito_tel': PhoneNumberPrefixWidget(attrs={'placeholder': 'Telefono', 'class': "form-control"}),
			'scelta_fattura' : CheckboxInput(attrs={"id":"scelta_fattura", "class":"form-control"}),
			'email' : EmailInput(attrs={"class":"form-control","id":"email",'placeholder':'email'}),
			'pec' : EmailInput(attrs={"class":"form-control","id":"pec",'placeholder':'pec'}),
			'fax' : PhoneNumberPrefixWidget(attrs={'placeholder': 'Fax', 'class': "form-control"}),
			'offerta_voip' : Select(attrs={"class":"custom-select md-form","id":"offerta_voip"}),
			'numero_voip' : PhoneNumberPrefixWidget(attrs={'placeholder': 'Numero Voip', 'class': "form-control"}),
			'ip_statico' : TextInput(attrs={"class":"form-control","id":"ip_statico",'placeholder':'Ip statico'}),
			'offerta_internet' : Select(attrs={"class":"custom-select md-form","id":"offerta_internet", 'placeholder':'Offerta internet'}),
			'cadenza_pagamento' : Select(attrs={"class":"custom-select md-form","id":"cadenza_pagamento", "class":"form-control"}),
			'metodo_pagamento' : Select(attrs={"class":"custom-select","id":"metodo_pagamento"}),
			'data_inizio_contratto' : DateInput(attrs={"class":"form-control","id":"data inizio contartto"}),

		
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

class statoclienteForm(forms.ModelForm):
	class Meta:
		model = statocliente
		fields= '__all__'
		
		widgets={
		
			'stato_del_cliente' : TextInput(attrs={"class":"form-control","id":"stato_cliente",'placeholder':'stato del cliente'}),
			
		}

