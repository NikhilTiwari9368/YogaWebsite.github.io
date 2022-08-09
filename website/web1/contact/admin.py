from django.contrib import admin
from contact.models import contact

class contactAdmin(admin.ModelAdmin):
    list_display = ('contact_name' ,'contact_email' , 'contact_comment')

admin.site.register(contact , contactAdmin)
# Register your models here.
