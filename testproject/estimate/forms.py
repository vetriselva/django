from django.forms import ModelForm, Textarea, TextInput, NumberInput, Select ,DateInput
from testapi.models import Estimates
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus import DatePickerInput
class EstimateForm(ModelForm):
	class Meta:
		model   = Estimates
		exclude = ['quote_info','quote_summary']
		widgets = {
            'quote_number'	: NumberInput(attrs={'readonly':'true', 'class':'form-control'}),
            'customer_name'	: TextInput(attrs={'placeholder':'Enter Customer Name', 'class':'form-control'}),
            'salse_person'	: TextInput(attrs={'placeholder':'Enter Sales Person', 'class':'form-control'}),
            'quote_date'	: DatePickerInput(format='%m/%d/%Y'),
            'quote_status'	: Select(attrs={'class':'form-control'}),
        }
		# fields = ['quote_date', 'quote_number',	
				  # 'customer_name', 'salse_person', 'quote_status']
		 