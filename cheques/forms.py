from django import forms
from cheques.models import Cheque
from django.forms.widgets import TextInput, Select,Textarea, DateTimeInput
from django.utils.translation import ugettext_lazy as _
from dal import autocomplete


class ChequeForm(forms.ModelForm):
    
    class Meta:
        model = Cheque
        exclude = ['creator','updater','is_deleted','date_added','date_updated','shop','is_notified']
        widgets = {
            'date' : DateTimeInput(attrs={'placeholder': '*Enter date','class':'required form-control'}),
            'vendor': autocomplete.ModelSelect2(url='vendors:vendor-autocomplete',attrs={'data-placeholder': 'Select Vendor','data-minimum-input-length': 1}),
            'cheque_number' : TextInput(attrs={'placeholder': 'Cheque Number','class':'required form-control'}),
            'name' : TextInput(attrs={'placeholder': '*Name','class':'required form-control'}),
            'account_number' : TextInput(attrs={'placeholder': 'Account Number','class':'required form-control'}),
            'amount' : TextInput(attrs={'placeholder': '*Amount','class':'required form-control'}),
            'details': Textarea(attrs={'class': 'form-control','placeholder' : 'Details'}),
        }
        error_messages = {
            'date' : {
                'required' : _("Date field is required."),
            },
            'name' : {
                'required' : _("Name field is required."),
            },
            'amount' : {
                'required' : _("Amount field is required."),
            },
                                      
        }
        labels ={
            'date' :'Processing date'
        }