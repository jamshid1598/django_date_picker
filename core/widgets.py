from datetime import date
from django import forms 


# first method
class CustomeDateTimePicker(forms.DateInput):
	DATE_INPUT_WIDGET_REQUIRED_FORMAT = "%d-%m-%Y"

	def __init__(self, attrs={}, format=None):
		attrs.update(
			{
				"class":"form-control",
				"type":"date",
			}
		)
		self.format = self.DATE_INPUT_WIDGET_REQUIRED_FORMAT
		super().__init__(attrs, format=self.format)


class PastCustomeDateTimePicker(CustomeDateTimePicker):
	def __init__(self, attrs={}, format=None):
		attrs.update({'max':date.today()})
		super().__init__(attrs, format=format)




# second method
class CustomDatePickerInput(forms.DateInput):
    template_name = "core/widgets/custom_datepicker.html"

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/datepicker/0.6.5/datepicker.min.css",
            )
        }
        js = (
            "https://code.jquery.com/jquery-3.4.1.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/datepicker/0.6.5/datepicker.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/datepicker/0.6.5/i18n/datepicker.es-ES.min.js",
        )