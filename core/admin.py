from django.contrib import admin
from django.db import models

# Register your models here.
from .models import MyBirthDay
from .widgets import PastCustomeDateTimePicker, CustomDatePickerInput

class MyBirthDayAdmin(admin.ModelAdmin):
	list_display=('name', 'birthday')
	formfield_overrides={
		models.DateField: {'widget': PastCustomeDateTimePicker}
	}



admin.site.register(MyBirthDay, MyBirthDayAdmin)