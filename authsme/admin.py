from django.contrib import admin
from .models import MailOrPhone, MailPass, PhoneNum
from .forms import PhoneNumForm
# Register your models here.


admin.site.register(MailOrPhone)
admin.site.register(MailPass)
admin.site.register(PhoneNum)
class ContactAdmin(admin.ModelAdmin):
    form = PhoneNumForm